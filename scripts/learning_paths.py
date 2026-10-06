#!/usr/bin/env python3
"""Read-only learning path planning; never creates directories or writes notes."""
import argparse
import datetime
import json
import os
from pathlib import Path
from urllib.parse import quote

# 笔记库位置：设了环境变量 LEARNING_VAULT 就用它（没装 Obsidian 时可指向任意文件夹，笔记是普通 Markdown）
DEFAULT_VAULT = Path(os.environ.get('LEARNING_VAULT') or Path.home() / 'Documents' / 'Obsidian Vault').expanduser()
LEARNING_ROOT = 'LLM Wiki/wiki/学习/AI学习'
LEARNING_HOME = 'LLM Wiki/wiki/学习/AI学习/00-入口.md'

def safe_relative(value):
    p = Path(value)
    if not value.strip() or value in ('.','..') or p.is_absolute() or any(x in ('..', '.') for x in p.parts) or '\\' in value:
        raise ValueError('学科必须是学习与知识内的相对分类，不得越界')
    if value.startswith(('LLM Wiki', '~')):
        raise ValueError('只传学科相对分类，例如经济学或AI与Agent/设计模式')
    return p

def safe_name(value):
    if not value.strip() or any(x in value for x in '/\\\n\r') or value in ('.', '..'):
        raise ValueError('书名和章节名必须是非空文件名片段')
    return value.strip()

def legacy_targets(vault, legacy):
    prefix = str(DEFAULT_VAULT) + '/'
    if legacy.startswith(prefix):
        legacy = legacy[len(prefix):]
    data = json.loads((vault/'LLM Wiki/迁移路径映射.json').read_text())
    redirects = {x['old_path']:x['new_path'] for x in data.get('corrections', [])}
    def current(path):
        seen = set()
        while path in redirects:
            if path in seen:raise ValueError('迁移映射存在循环')
            seen.add(path);path = redirects[path]
        return path
    if legacy in redirects:return [current(legacy)]
    for item in data['entries']:
        if item['old_path'].removesuffix('.md') == legacy.removesuffix('.md'):
            if Path(legacy).suffix and Path(legacy).suffix != '.md' and item.get('raw_original'):
                return [current(p) for p in item['raw_original']]
            paths = item.get('整理目标', []) + item.get('raw_original', [])
            return list(dict.fromkeys(current(p) for p in paths))
    raise ValueError('旧路径未登记；不得重建旧Library目录，应报告缺口')

def relocate(vault, path):
    """迁移映射里的目标若已随 Wiki 改版移走，只在 wiki/学习 内按文件名找唯一匹配。"""
    if (vault/path).is_file():return path
    hits=[h for h in (vault/'LLM Wiki/wiki/学习').rglob(Path(path).name) if h.is_file()]
    return hits[0].relative_to(vault).as_posix() if len(hits)==1 else None

def plan(vault, subject=None, course=None, chapter=None, date=None, legacy=None):
    vault = Path(vault).resolve()
    result = {'read_only':True,'home':str(vault/LEARNING_HOME),
              'knowledge_root':str(vault/LEARNING_ROOT),
              'cards_dir':str(vault/LEARNING_ROOT/'复习卡'),
              'rules':str(vault/'LLM Wiki/AGENTS.md')}
    if legacy:
        paths = [relocate(vault, p) for p in legacy_targets(vault, legacy)]
        if not paths or any(not p or not (vault/p).is_file() for p in paths):
            raise ValueError('迁移目标缺失，禁止凭旧路径补建')
        result['resolved']=[str(vault/p) for p in paths]
    if subject:
        relative = safe_relative(subject)
        notes = (vault/LEARNING_ROOT/relative).resolve()
        if not notes.is_relative_to((vault/LEARNING_ROOT).resolve()):raise ValueError('路径越界')
        result['notes_dir']=str(notes)
        result['subject_exists']=notes.is_dir()
        if course and chapter:
            date=date or datetime.date.today().isoformat()
            datetime.date.fromisoformat(date)
            stem=f'{safe_name(course)}-{safe_name(chapter)}-{date}'
            card_stem=f'{safe_name(course)}-{safe_name(chapter)}-复习图-{date}'
            result.update(note=str(notes/(stem+'.md')),
                          card_html=str(vault/LEARNING_ROOT/'复习卡'/(card_stem+'.html')),
                          card_png=str(vault/LEARNING_ROOT/'复习卡'/(card_stem+'.png')))
            result['card_html_link']='[查看互动复习卡](<'+quote(Path(result['card_html']).relative_to(vault).as_posix(),safe='/')+'>)'
            result['card_png_link']='![复习图](<'+quote(Path(result['card_png']).relative_to(vault).as_posix(),safe='/')+'>)'
            result['note_exists']=Path(result['note']).exists()
    return result

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--vault',default=str(DEFAULT_VAULT))
    p.add_argument('--subject');p.add_argument('--course');p.add_argument('--chapter')
    p.add_argument('--date');p.add_argument('--legacy')
    args=p.parse_args()
    try:print(json.dumps(plan(**vars(args)),ensure_ascii=False,indent=2))
    except (ValueError,FileNotFoundError,KeyError) as e:p.exit(2,str(e)+'\n')
