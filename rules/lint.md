# Lint Rules

Vault 健全性チェックの詳細規約。

## チェック項目

- 孤立ノート（被リンクゼロ）の検出と報告
- `#llm-draft` タグが2週間以上放置されているノートの報告
- `Inbox/` の2週間以上の滞留を報告
- 矛盾する記述が複数ノートにまたがっていないかを確認
- `Papers/*/03_gaps.md` の `#open-question` が `Permanent/` に反映されているかを確認
- `References/` へのリンク切れを検出した場合、`References/AGENTS.md` の規約に従って再同定と修正を行う

## 集計除外対象

- 隠しファイル（`.*`）および `.gitkeep`
- OS 生成ファイル: `.DS_Store`（macOS）、`Thumbs.db`・`desktop.ini`（Windows）
- `Done/` 配下のファイル
- 未処理件数は `Inbox/` `Clippings/` **直下の可視ファイルのみ**を対象とする（上記除外対象を含まない）
- 孤立ノートの定義: `[...](...)` 形式の相対パスリンクによる被リンクが 0 件の `Permanent/` ノート
