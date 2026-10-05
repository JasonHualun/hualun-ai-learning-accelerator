# Feishu Image Delivery Patterns

## Current Status (2026-05-26)
Image delivery to Feishu is inconsistent. Multiple approaches have been tried with mixed results.

## What Works in Cron Jobs
From cron output analysis, these patterns appear in successful cron deliveries:

```
MEDIA:/absolute/path.png
```

Example from hualun-life-game cron (2026-05-20):
```
MEDIA:/tmp/life-game-2026-05-19.png
```
This successfully delivered the image.

Example from hualun-life-game cron (2026-05-18):
```
![昨日插图](~/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260518_090237_186b4749.png)

MEDIA:~/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260518_090237_186b4749.png
```
Both formats were used, but the cron noted "飞书文档内嵌图片因本地路径不可下载而失败".

## What Doesn't Work (Direct Conversation)
In direct conversation (not cron), these attempts failed:

1. Using `send_message` tool with `MEDIA:/path` in message text
2. Including `![alt](path)` markdown syntax in message text
3. Including `MEDIA:/path` in direct response text

User feedback: "你发了个寂寞" (you sent nothing), "还是没有" (still nothing)

## Hypothesis
- Cron jobs may have different delivery pipeline than direct conversation
- The `MEDIA:` syntax may only work in specific contexts
- Feishu image upload may require the image to be accessible via URL, not just local path

## Next Steps to Investigate
1. Check if `send_message` tool supports `media_files` parameter
2. Test with images in `/tmp/` directory (which worked in cron)
3. Check if images need to be uploaded to a URL first
4. Review the Feishu adapter code for image sending methods

## Related GitHub Issues
- NousResearch/hermes-agent#14049 - fix: route media files to Feishu send_message pipeline
- NousResearch/hermes-agent#8774 - Can I let Hermes send a picture file through messaging
- NousResearch/hermes-agent#15576 - Feishu and WeChat images fail with 'Invalid image source'

## User Preference
User expects images to display inline in Feishu chat, not as file attachments. The current workaround is to send text descriptions when images fail to deliver.
