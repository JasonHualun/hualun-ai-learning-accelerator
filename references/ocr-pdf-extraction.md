# 扫描版 PDF 的 OCR 提取流程

## 问题描述

部分经典书籍（尤其是老版 PDF）是扫描版，没有文字层，pdfplumber 直接提取返回空。

## 诊断方法

```python
import pdfplumber
with pdfplumber.open(path) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    if not text or len(text.strip()) < 10:
        print("扫描版，需要 OCR")
    images = page.images
    print(f"图片数: {len(images)}")  # 扫描版通常只有1张大图
```

## 解决方案：Tesseract OCR

### 安装

```bash
apt-get install -y tesseract-ocr tesseract-ocr-eng
pip install pytesseract
```

### 提取流程

```python
import pdfplumber
import pytesseract
from PIL import Image
import io

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        # 页面转图片（300 DPI 适合 OCR）
        img = page.to_image(resolution=300)
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        # OCR 提取
        pil_img = Image.open(img_bytes)
        text = pytesseract.image_to_string(pil_img, lang='eng')
```

## 注意事项

- **分辨率**：300 DPI 是 OCR 最佳平衡点；低于 200 识别率下降，高于 600 内存暴涨
- **语言**：英文书籍用 `lang='eng'`；中文书籍需要 `tesseract-ocr-chi-sim`
- **速度**：每页约 2-3 秒（300 DPI），整本书需要几分钟
- **质量**：老版扫描件可能有污渍、倾斜，OCR 结果需要人工校对
- **目录定位**：先找目录页（搜索 "CONTENTS"），再按页码范围提取各章

## 实战经验：维纳《控制论》

- 书有 231 页，全是扫描图
- 目录在第 16 页（搜索 "CONTENTS" 找到）
- Chapter I 实际从第 49 页开始（目录写的第 30 页是原书页码，不是 PDF 页码）
- 提取 14 页约 30 秒

## 何时使用

当 `pdfplumber.extract_text()` 返回空或极短文本，且 `page.images` 显示有大图时，切换到 OCR 流程。
