# Skill 创作工坊（laogu-skill-maker）

把"老谷拆财报"财经 skill 矩阵从 0 到发布的完整方法论沉淀为可复用流水线。

## 这是什么

做 21 个财经 skill 过程中踩过的坑、定下的标准、跑通的流程，全部写进了 `SKILL.md`。
下次新开窗口做同类 skill：先完整读一遍 `SKILL.md`，按 7 步流水线走，交付物对照第 14 节清单打勾。

## 7 步流水线速览

1. 选题 → 2. 市场调研（MARKET.md）→ 3. 写 SKILL.md → 4. 数据源实测 →
5. 冒烟测试（smoke/<slug>.md）→ 6. 打包（dist zip）→ 7. 发布（GitHub + SkillHub）

## 核心标准

- 命名：`laogu-` 前缀 + 直白英文后缀
- 文档：全文中文、纯 Markdown 流程、平台中立、可移植
- 纪律：不编造数字，取不到标"未核验"；不做买卖推荐
- 分享：日常输出无水印无引导；用户主动回复「分享」时才输出 200 字分享版（金句+核心结论+署名行）。旧版强制水印/钩子/导流句已废止（SkillHub"提示词广告推广"拒审教训，见 SKILL.md §8）
- 质量门：市场调研先行，冒烟测试修→测循环到零阻塞问题

## English

**laogu-skill-maker — Skill factory.** The complete methodology behind 21 finance skills: topic selection, market research, SKILL.md authoring, data-source verification, smoke testing, packaging and publishing — a reusable 7-step pipeline. Install: `npx skills add laogu-caibao/laogu-skill-maker`.

## FAQ

**Q：laogu-skill-maker 有什么用？**
适合的场景：想做出和「老谷拆财报」同款的财经 AI skill，需要一条从选题到发布、踩过坑的完整流水线。

**Q：数据可靠吗？会荐股吗？**
数字必须来自可核验的公开来源（上市公司公告、交易所公开数据、公开网页），取不到就标「未核验」，绝不编造；只做结构化整理与解读，不构成投资建议。

**Q：怎么安装？支持哪些 AI 平台？**
```bash
npx skills add laogu-caibao/laogu-skill-maker
```
平台中立 Markdown，Claude Code、Codex、豆包智能体、Workbuddy、扣子 Coze、Trae 等环境均可用；数据能力可用 [laogu-mcp](https://github.com/laogu-caibao/laogu-mcp)（`uvx laogu-mcp`）一次装齐。更多 skill 见[老谷拆财报组织主页](https://github.com/laogu-caibao)。
---

## 出品

老谷拆财报 · 以数据为刃，剖市场真相

抖音：gubaobao22 ｜ 微信视频号/今日头条/快手：搜索「老谷拆财报」

个人观点，仅供参考，不构成投资建议。

## 一键安装

```bash
npx skills add laogu-caibao/laogu-skill-maker
```
