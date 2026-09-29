# 扣子 / Trae 兼容性冒烟报告（2026-09-29）

## 结论
- 本地 16 个 dist 发布包结构校验：**16/16 通过**
- GitHub 16 个仓库 SKILL.md frontmatter 抽查：**16/16 通过**
- 真机导入（Coze 需登录 / Trae 需装 IDE）：**待用户侧验证**，未声称已测

## 校验项
1. zip 根目录有 SKILL.md
2. SKILL.md 头部 YAML frontmatter 的 name / description 非空
3. references/ 目录未被压平

## 适配动作
- 16 个仓库 README"一键安装"区新增 Coze / Trae 安装行（含 .skill 后缀警告、Trae MCP 路线）
- skill-maker 方法论新增第 16 节（兼容性适配要求）

## 待用户
- Coze：登录后在扣子编程技能面板实际上传一次任一 skill 包
- Trae：安装 Trae IDE 后实际导入一次
