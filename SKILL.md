---
name: "laogu_skill_maker"
description: "财经 skill 创作方法论：把'老谷拆财报'21 个 skill 从选题、市场调研、文档写作、数据源实测、冒烟测试到打包发布的完整流水线沉淀为可复用流程，新开窗口做同类 skill 时照着走一遍即可。"
---

# Skill 创作工坊

> 功能：把"老谷拆财报"财经 skill 矩阵（21 个）从 0 到发布的完整方法论沉淀为可复用流水线。
> 下次新开窗口做同类 skill，先读完本文，再动手。

## 30 秒速览（7 步流水线）

1. **选题**：散户高频/强痛点场景，一个 skill 只做一件事
2. **市场调研**：供给/需求/槽点/差异化 → 写进 `MARKET.md`
3. **写 SKILL.md**：按第 3 节标准结构，纯流程、平台中立、全文中文
4. **数据源实测**：文档里每个接口亲手调一遍，调不通写降级链 + 搜索模板
5. **冒烟测试**：真实数据跑全流程，修→测循环到零阻塞问题，报告存 `smoke/<slug>.md`
6. **打包**：`dist/<slug>-<version>.zip`，内容清单见第 10 节
7. **发布**：GitHub 公开仓（含 README"一键安装"区）+ 组织主页同步 + SkillHub 提交，状态表述必须诚实（审核中≠已上架）；发布后评估是否加入 laogu-mcp（见第 15 节）

## 1. 选题标准

- 面向中国 A 股散户（或明确的一类用户），场景具体
- 高频（每日/每周）或强痛点（怕错过、怕踩雷、看不懂）
- 公开数据可支撑，不依赖付费 API 或登录态
- 一个 skill 只做一件事，拒绝大而全
- 与 IP 定位一致：说人话、排雷、不编数

## 2. 命名规范

- slug：`laogu-` 前缀 + 直白英文后缀，一眼看懂用途、便于转发
  - 例：`laogu-morning`（早报）、`laogu-moneyflow`（资金流向）、`laogu-lhb`（龙虎榜，圈内黑话反而利于传播）、`laogu-ipo`（打新）、`laogu-value`（估值）
- SKILL.md frontmatter `name`：下划线版，如 `laogu_morning`
- 中文显示名：4–8 字，如"每日市场早报"
- slug 一旦发布不要改；必须改视为新 skill，重新走发布流程

## 3. SKILL.md 标准结构

```
frontmatter（name / description，一句话讲清用途，带中英文关键词）
# 中文名
> 功能：一句话速览
Auto-run 块（零输入可运行的 skill 必备：加载即运行，写清触发条件）
Purpose（解决什么问题、给谁用、不用什么）
Workflow（编号步骤，每步 = 输入→动作→输出；注明数据源、失败时降级到哪）
Output Contract（输出结构、字数、语言、必备字段、数据缺失时怎么标注）
Operating Rules（诚实纪律，见下）
分享规范（见第 8 节）
出品区（见第 9 节）
```

- 全文中文；不引用任何平台专有工具（纯 Markdown 流程，保证可移植）
- 移植表述用"豆包工作"（"豆包智能体"已下线，不要再写）
- 时间表述一律用"北京时间"，美股/欧股注明对应关系

### Operating Rules（每条都要写进文档，不是口号）

- 不编造数字：取不到就标"未核验"，"原文未披露"就写原文未披露，不估算
- 关键数据双源交叉，单源数据标注来源
- 只做逻辑陈述，不做买卖推荐（合规红线，见第 12 节）
- 每条数据带日期时点；历史观点注明"截至某日"

## 4. references/ 写作规范

每个外部数据源独立成段，必须包含：

- 接口 URL（含参数模板，如 `{code}` 占位）
- 请求要求：Referer / UA / 编码（GBK→UTF-8 转码说明）
- 返回字段说明（只写用到的字段）
- 实测状态：可用 / 部分可用 / 已失效（写实测日期）
- 降级链：主力 → 备选 → 网页搜索模板（关键词 + 日期），不承诺做不到的事
- 已证伪的接口必须写明"不要用"并给替代方案

## 5. 数据源方法论

1. **实测优先**：文档里写的每个接口，发布前亲手调一遍
2. **三级降级**：主力接口 → 备选接口 → 网页搜索，写进 Workflow
3. **诚实标注**：缺口就是缺口，"未核验/待确认"写在输出里，不藏
4. **交易日校验**：涉及 A 股的 skill，先判断当日是否交易日；长假休市日直接跳过，不硬写旧内容
5. **时差意识**：北京时间凌晨 4 点前，美股为盘中价未收盘，必须标注

## 6. 市场调研（MARKET.md）

每个 skill 开工前先调研，结论写进 `MARKET.md`，定位据此调整：

- **供给**：SkillHub / Coze / Dify / GitHub / 券商 App 里的同类方案，覆盖到什么程度
- **需求**：用户原话证据（社区、评论区、搜索联想），不要脑补需求
- **槽点**：现有方案被吐槽最多的 3 点（通常是：编数据、看不懂、收费墙、马后炮）
- **差异化**：我们凭什么赢，简介首句就要见血

## 7. 冒烟测试 SOP

- 重读当前 SKILL.md + references/，用**真实数据**按 Workflow 跑全流程，不修改文件
- 上一轮旧问题逐条回归；新发现的问题能修文档就修，修完重测（修→测循环）
- 判定标准：零阻塞问题才算通过；非阻塞遗留必须明确标注（如"退市公司兜底路径未覆盖"）
- 报告存 `smoke/<slug>.md`：测试时间、方法、每步结论、旧问题回归表、遗留问题
- 回归测试必须拿到**完整报告**才算数，一句话简报不算通过

## 8. 分享机制规范（laogu-close v1.0.3 整改版）

> 教训：laogu-close v1.0.2 曾因 SKILL.md 强制输出分享水印/钩子/导流句，被 SkillHub 以"提示词广告推广"判拒审。以下为整改后规范，旧版"每份输出强制带水印+钩子+导流句"一律废止。

- **日常输出**：不带水印行、不带分享引导、不追加任何导流句
- **分享版（可选）**：仅在用户主动要求分享（如回复「分享」）时，另输出 200 字内分享版——第一句为 20 字内观点金句（从本篇提炼最有冲击力的判断或数据），再接核心结论与署名行 `—— 老谷拆财报 · {中文名} · {YYYY-MM-DD}`
- **金句**：分享版第一句必须为 20 字内观点金句，这是转发的社交货币
- 助手侧：用户首次使用某 skill 出结果后，可提一句"回复「分享」可以生成转发版"；不主动、不强制

## 9. IP 与出品区

SKILL.md 末尾统一追加**文字版**出品区（二维码图片在部分平台刷不出来，已废止）：

```
## 出品：老谷拆财报

以数据为刃，剖市场真相。

- 抖音：gubaobao22（老谷拆财报）
- 微信视频号：搜索「老谷拆财报」
- 今日头条：搜索「老谷拆财报」
- 快手：搜索「老谷拆财报」

财经科普、财报解读。个人观点，仅供参考，不构成投资建议。
```

- `icon-512.png`：全矩阵统一用老谷×咪仔方形头像
- 出品区为纯文字说明，不强制要求输出携带（避免 SkillHub"提示词广告推广"误判）

## 10. 打包规范

- `manifest.yaml`：slug / display_name（中文）/ description（中文简介）/ version / author（老谷拆财报）
- `dist/<slug>-<version>.zip` 内容：`SKILL.md` + `manifest.yaml` + `icon-512.png` + `references/` + `docs/`（**不含** LICENSE / README / MARKET.md）
- 打包后用 `unzip -l` 核验内容清单
- 版本号：修复发版升小版本（如 1.0.1）；新 skill 从 1.0.0 起

## 11. 发布 SOP

### GitHub

- `laogu-caibao` 组织下每个 skill 一个**公开**仓库，仓库名 = slug
- README：中文首行（中文名 + 一句话功能）、功能速览、出品区（口号 + 四平台矩阵 + 声明）
- **README 必须含"## 一键安装"区**：可复制的仓库链接（代码块）+ `git clone <url>.git` 命令 + ZIP 下载链接（`<url>/archive/refs/heads/main.zip`）+ 导入使用说明（Claude Code 放 `~/.claude/skills/<slug>/`、豆包智能体 / Workbuddy 按平台流程导入、`uvx laogu-mcp` 一次装全 21 个）
- 组织主页（`.github` 仓库）同步更新 skill 一览（新增 skill 后必做）
- 推送前确认默认分支是 **main**（不是 master）；改名/改内容后重新推送，核验 main 分支实际内容

### SkillHub

- 入口：`https://skillhub.cn/dashboard/publish`，上传 zip + 512 图标，填 slug / 显示名 / 中文简介 / 版本 / 更新说明
- 必须看到"提交成功 / 待审核 / 审核中"回执才算提交成功
- 状态表述诚实：**审核中 ≠ 已上架**；"上传完成" ≠ "提交成功"

## 12. 合规红线

- 不做买卖推荐；"多空判断"只做逻辑陈述，措辞统一用"偏多 / 偏空（逻辑陈述）"
- 对外文案避开"建议买入 / 可关注 / 必看一只股"
- 遵守《金融产品网络营销管理办法》（2026-09-30 施行），"非法荐股"是红线
- 每份输出带"个人观点，仅供参考，不构成投资建议"

## 13. 常见坑位（实战沉淀，持续追加）

- 东财 push2 在部分网络环境 502 → 只做备选
- 腾讯行情部分网络 TCP 超时 → 新浪为主力（记得 Referer + GBK→UTF-8 转码）
- 北向"净流入/净买入"口径已死（2024-05 宣布、2024-08-19 起实施新口径）→ 改看成交总额占比 / 前十大成交股 / 龙虎榜股通席位；**不要再写"北向净流入"**
- 巨潮公告接口默认返回 0 条、深交所 WAF 拦截 → 东财公告接口为主力
- 公告正文：`notices/detail` 页面是 JS 空壳 → 用 `np-cnotice-stock` 的 content API
- 定期报告财务数据：东财 report 接口不稳定 → 网页搜索模板 + 双源交叉
- 两融数据 T+1；融资净买入 = RZMRE - RZCHE；两融个股 filter 用 `SCODE="600519"` 格式
- 龙虎榜接口用 `RPT_DAILYBILLBOARD_DETAILSNEW`；两融用 `RPTA_WEB_RZRQ_GGMX`
- 早报：长假休市日跳过不回滚；美股时间锚点写清"盘中价/已收盘"
- ETF 净申购搜不到时换关键词："ETF追踪 昨日ETF净申购 + 日期"

## 14. 交付物清单（每个 skill 对照打勾）

- [ ] SKILL.md（含出品区、分享规范、头部 YAML frontmatter：name + description）
- [ ] references/（每个接口实测状态 + 降级链）
- [ ] MARKET.md（供给/需求/槽点/差异化）
- [ ] manifest.yaml（版本正确）
- [ ] icon-512.png（统一头像）
- [ ] 出品区为文字版（口号 + 四平台矩阵文字 + 作者声明），不放二维码图片
- [ ] README.md（GitHub 用，含"一键安装"区：clone/ZIP/导入 + Coze/Trae 行）
- [ ] LICENSE（MIT）
- [ ] dist/<slug>-<version>.zip（unzip -l 核验过；根 SKILL.md + frontmatter + references/ 未压平，Coze/Trae 通用）
- [ ] smoke/<slug>.md（完整冒烟报告，零阻塞问题；含兼容性结构校验结果）
- [ ] GitHub 公开仓库已推送并核验（默认分支 main）
- [ ] 组织主页 skill 一览已同步
- [ ] SkillHub 已提交并看到回执
- [ ] 已评估是否加入 laogu-mcp（见 §15；若加，完成 server.json / PyPI / Registry / Smithery 连锁）

## 15. laogu-mcp 联动（新 skill 发布后必评估）

- 新 skill 若适合程序化调用，给 `laogu-mcp` 加一个同名 tool（数据抓取 + 结构化返回，解读仍由宿主 LLM 按 skill 的 Output Contract 做）
- 加 tool 后的连锁动作：
  1. `server.json` 顶层 `version` 与 `packages[0].version` 同步升版
  2. PyPI 包 `README.md` 必须含 `mcp-name: io.github.laogu-caibao/laogu-mcp`（Registry 归属校验用）
  3. 打 `v*` tag → GitHub Actions 自动：PyPI 可信发布 → OIDC 同步官方 MCP Registry（`io.github.laogu-caibao/laogu-mcp`）
  4. tool 列表变化时，重新打 `.mcpb` 包并在 Smithery 重新发布
## 16. 扣子 / Trae 兼容性适配（新 skill 必做）

- **SKILL.md 头部必须带 YAML frontmatter**：`name`（用 slug，下划线或连字符全矩阵统一）+ `description`（一句话中文，写清触发场景——这是 Trae/Coze 自动匹配技能的关键字段）
- **发布包即通用包，不另打**：Coze 与 Trae 都要求"zip 根目录有 SKILL.md（含 frontmatter）+ references/ 不压平"，现有 `dist/<slug>-<version>.zip` 天然满足（SKILL.md 在根、references/ 完整），一个包同时用于 SkillHub / Coze / Trae
- **README"一键安装"区必须含 Coze / Trae 行**：
  - 扣子：扣子编程 → 技能面板 → 创建技能 → 本地上传（仓库根目录已有 SKILL.md，直接压缩仓库文件夹即可）；页面要求 `.skill` 后缀时由扣子导入后自动生成，**不要只改 zip 扩展名**
  - Trae：设置 → 技能 → 上传技能（同上 zip）；或手动放到 `~/.trae/skills/<slug>/`（项目级用 `.trae/skills/<slug>/`，TRAE Work 国区版路径为 `~/.trae-cn/skills/`）；Trae 支持 MCP，把 `uvx laogu-mcp` 配进 MCP 设置即得 21 个工具——skill 负责流程指导、MCP 负责工具调用
- **冒烟测试（每次发版跑）**：
  1. 结构校验（本地可跑，21 个包全过才算过）：zip 根有 SKILL.md、frontmatter 的 name/description 非空、references/ 未被压平
  2. GitHub 抽查：仓库 main 分支的 SKILL.md 头部 frontmatter 与本地一致
  3. 真机导入（需用户侧）：Coze 需登录后在技能面板实际上传一次；Trae 需装好 IDE 后实际导入一次——这两项在用户完成前如实标注"待真机验证"，不许声称已测过

## 17. 自迭代能力（新 skill 必做：质检协议 + MCP 配置热更新）

- **每个新 skill 的 SKILL.md 必须包含"自我质检与反馈"章节**（放在 Operating Rules 之后、"出品"区之前），内容模板见本仓库 `references/qa-section-template.md`：质检清单（日期锚/数据源存活/完整性/合规红线/口语化）→ 发现问题先重试 1 次 → 生成《问题报告》→ 询问使用者是否一键通知作者 → gh issue 或预填 issue 链接（`https://github.com/laogu-caibao/<slug>/issues/new?title=...&body=...`，URL 编码拼接）。使用者侧只提 issue 不直接改仓库。
- **MCP 联动（第 15 节）的配置热更新**：新 skill 若进 `laogu-mcp`，必须在 skill 仓库根目录提供 `mcp-config.json`，schema 见 `laogu-mcp` 仓库的 `config-schema.md`：`skill`（slug）、`config_version`（语义版本，每次改配置必升）、`updated`（YYYY-MM-DD）、`endpoints`（命名 URL 模板，`{param}` 占位）、`symbols`（快照类标的表）、`fallback_order`（降级顺序）、`field_map`（解析字段索引，可覆盖代码默认值）。日常优化只改此文件 → MCP 下次调用自动生效（TTL 缓存 1 小时），零发版；深层解析逻辑变更才需发 MCP 新版。
- **版本号联动**：改 `mcp-config.json` 必须同步升 `config_version`；MCP 每个 tool 返回的 meta 里带 `config_version` + `config_source`（live/cache/bundled），透明可查。
- **交付物清单（第 14 节）追加两项**：☐ 质检章节已植入并跑过一遍清单 ☐ mcp-config.json 已建且 MCP 本地热加载冒烟通过。

## 18. 决策质量四件套（新 skill Output Contract 必备，借鉴 ai-berkshire）

> 来源：xbtlin/ai-berkshire（MIT，16,564 star）方法论，文案自研、只借鉴框架。散户缺的不是更多信息，而是"敢下判断 + 敢认错"的决策纪律。

1. **强制三档结论**：Output Contract 必须要求结论分三档输出，不许"一方面…另一方面…"打太极。个股/基金类用"值得跟踪 / 保持观望 / 提示风险"；测温类用"过热 / 中性 / 冰冷"；回检类用"成立 / 部分成立 / 被证伪"。每档必须附 1-2 句逻辑依据，并声明"个人观点，仅供参考，不构成投资建议"。
2. **反偏见清单**：Output Contract 末尾附 4-6 条自查项，输出前逐条过一遍。通用项：确认偏误（是否只找了支持证据）、近因效应（是否被最近一周走势带偏）、幸存者偏差（样本是否只剩活下来的）、锚定效应（是否被某个价格/数字锚定）；各 skill 按场景增补（如选股加"只看 PE 陷阱"、情绪加"把相关当因果"）。
3. **投资论文追踪**：凡输出"判断/观点"的 skill，必须同时记录"关键假设 + 证伪条件"（见 laogu-thesis 的建档模板），到期回检。把"认错机制"写进流程，而不是只写进文案。
4. **双源交叉验证**：关键数字（价格、涨跌幅、财务数据）必须双源交叉，误差超过阈值（默认 1%）必须告警并标注"未核验"，不许静默采用单源数字。单源数据必须标注来源。
