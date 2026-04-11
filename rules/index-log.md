# Index And Log Rules

`index.md` と `log.md` の管理規約。

## index.md

`index.md` は AI が管理する。以下の構成で維持する:

```markdown
# Vault Index
最終更新: YYYY-MM-DD

## 統計
- Permanent/: XX件（うち #wiki: XX件、#llm-draft: XX件）
- Literature/: XX件
- References/: XX件
- Inbox/未処理: XX件 / Clippings/未処理: XX件

## Permanent/ — カテゴリ別
### [カテゴリ名]
- [ノート名](relative/path.md) — 1行の概要

## Papers/ — 進行中の論文
| スラッグ | フェーズ | 次のアクション |
|---|---|---|
| [paper-slug] | [執筆中/査読中/etc.] | [次にすべきこと] |
```

## log.md

- `log.md` は append-only の操作履歴として扱う
- 形式: `## [YYYY-MM-DD] {操作} | {内容}`
- どのエージェントが操作しても記録を残し、セッションをまたいだ継続作業を可能にする
