# AGENTS.md

このVaultは、情報の集積（Capture）→ 知識への醸成（Knowledge）→ アウトプット（Output）
を支援する研究者の外部知識システムです。

root `AGENTS.md` は入口です。詳細手順は `rules/` と各ディレクトリの `AGENTS.md` に委譲します。

---

## セッション

### セッション開始

**トリガー**: 「セッションを開始してください」

`rules/workflows.md#セッション開始` に従い、`index.md` / `log.md` / 未処理件数 / Probe を確認して、今セッションで着手できる作業を3件以内で提案する。

### セッション終了

**トリガー**: 「セッションを終了してください」

`rules/workflows.md#セッション終了` に従い、必要に応じて `index.md` と `log.md` を更新し、終了報告を3行以内でまとめる。

---

## ディレクトリ運用

Vault全体の構造と各ディレクトリの役割は `rules/architecture.md` を参照する。

サブディレクトリに `AGENTS.md` が存在する場合、そのディレクトリを操作する前に読む。

- `Literature/` → `Literature/AGENTS.md`
- `Permanent/` → `Permanent/AGENTS.md`
- `Papers/` → `Papers/AGENTS.md`
- `References/` → `References/AGENTS.md`

---

## 最重要原則

- **AIは叩き台を作る。最終判断と編集は人間が行う**
- AIが生成したノートには必ず `#llm-draft` タグを付ける
- 既存ノートの上書き・削除は必ずユーザー確認をとる
- `References/` は読み取り専用。移動・削除しない
- 推測を含む場合はノート内に `【推測】` を明示する
- 長文を勝手に生成しない。**提案 → 確認 → 実行** の順で動く
- 1ノート1アイデア（Atomicity）の原則を守る
- 知識に関する対話では、応答の末尾に「次の問い」を1つ添える。作業指示への対応中は省略する

---

## 操作

- Ingest — ソース取り込み: `rules/workflows.md#ingest`
- Promote — 永久ノート作成: `Permanent/AGENTS.md`
- Wiki-Update — 知識統合ページ更新: `Permanent/AGENTS.md`
- Paper-Work — 論文執筆管理: `Papers/AGENTS.md`
- PaperDesk — 論文精査: `rules/workflows.md#paperdesk`
- Lint — Vault健全性チェック: `rules/lint.md`
- Probe — 能動的問いかけ: `rules/workflows.md#probe`
- Connect — セレンディピティ探索: `rules/workflows.md#connect`
- Remember — 議論の記憶保存: `rules/workflows.md#remember`

---

## PaperDesk 概要

論文の検索・読解・査読・横断サーベイ・科学的根拠確認には PaperDesk を使う。
詳細なモード選択と実行範囲は `rules/workflows.md#paperdesk` に従う。

- Mode A / read: 他者の論文1本を読解・Vault統合する
- Mode B / review: 自分の原稿を投稿前に批判的評価する
- Mode C / survey: 複数論文を横断して調べる
- Mode D / evidence-check: 科学的主張の支持状況を確認する

## システム改善

AGENTS.md・テンプレートの変更依頼があった場合:

1. 変更対象ファイルを読む
2. 変更内容を提案し、ユーザーの確認を得る
3. 確認後に書き込む
4. `log.md` に記録する（形式: `## [YYYY-MM-DD] System | {変更内容}`）

- 変更の影響が他の AGENTS.md に波及する場合は、その旨を明示する
- テンプレート変更は既存ノートに遡及適用しない

---

## 任意参照

- `rules/architecture.md` — Vault の情報フロー・Papers/ 構造図
- `rules/workflows.md` — Probe・Connect の詳細手順
- `rules/lint.md` — Lint の詳細基準
- `rules/tags.md` — タグ体系
- `rules/index-log.md` — `index.md` と `log.md` の管理規約
