# AGENTS.md

このVaultは、情報の集積（Capture）→ 知識への醸成（Knowledge）→ アウトプット（Output）
を支援する研究者の外部知識システムです。

---

## セッション開始

**トリガー**: 「セッションを開始してください」

1. `index.md` を読み、Vault全体の概要を把握する
2. 実ファイル数や更新状況が重要な場合は、`index.md` を鵜呑みにせず実ディレクトリを確認する
3. `log.md` の末尾5件を確認し、前回からの継続タスクを識別する
4. `log.md` の記録が不足している可能性があるときは、必要に応じて実ファイルやGit履歴も参照する
5. 以下の情報をもとに、今セッションで着手できる作業を優先度順に提案する（3件以内）:
   - `Inbox/` `Clippings/` の未処理件数（件数も併記する）
   - `#llm-draft` タグが2週間以上放置されているノート
   - `Papers/*/03_gaps.md` の未解決事項（`状態: 未着手 / 対応中`）
   - `log.md` の継続タスク
6. Probe を実行し、結果をセッション開始報告に含める
7. Vault の状況を報告する

## セッション終了

**トリガー**: 「セッションを終了してください」

1. `index.md` は派生サマリとして、必要な範囲で更新する
2. `log.md` は補助的な操作記録として、主要な変更・判断を追記する
   形式: `## [YYYY-MM-DD] {操作} | {内容}`
3. 今セッションで生まれた新しい問いや半形成のアイデアがあれば `Inbox/` へのメモ追加を提案する
4. 終了報告として、今セッションで行った作業の要点を3行以内でまとめる

---

## ディレクトリの役割

### Clippings/
Web記事・SNS保存など軽量な外部ソースの一時置き場。
処理済みは `Clippings/Done/` へ移動する。

### References/
論文PDF・書籍の永続保管庫。**削除しない。Done/ へ移動しない。**
詳細は `References/AGENTS.md` に従う。

### Daily/
日々の気づき・実験所感・会議メモ。
定期的に `Inbox/` または `Literature/` への昇華を促す。
すでに1ノート1アイデアに近い内容なら、`Daily/` から直接 `Permanent/` に Promote してよい。

### Inbox/
思いつき・走り書きメモの投入口。
処理済みは `Inbox/Done/` へ移動する。

### Literature/
`Clippings/` `References/` `Daily/` から生成した文献・ソースノート。
AIが叩き台を作り、人間が編集する。詳細は `Literature/AGENTS.md` に従う。

### Permanent/
知識の中核。永久ノートと Wiki 統合ページを管理する。
詳細は `Permanent/AGENTS.md` に従う。

### Papers/
論文ごとのワークスペース。`Papers/[paper-slug]/` の形で管理する。
詳細は `Papers/AGENTS.md` に従う。

---

## 原則

- **AIは叩き台を作る。最終判断と編集は人間が行う**
- AIが生成したノートには必ず `#llm-draft` タグを付ける
- 既存ノートの上書き・削除は必ずユーザー確認をとる
- `References/` は読み取り専用。移動・削除しない
- 推測を含む場合はノート内に `【推測】` を明示する
- 長文を勝手に生成しない。**提案 → 確認 → 実行** の順で動く
- 1ノート1アイデア（Atomicity）の原則を守る
- 知識に関する対話では、応答の末尾に「次の問い」を1つ添える。作業指示への対応中は省略する

---

## 操作定義

### Ingest — ソース取り込み
対象: `Clippings/` の未処理ファイル、`References/` 配下の論文PDF・書籍、`Daily/` のメモ

ソースのタイプに応じてプロンプトを使い分ける:
- **論文 PDF**（`References/papers/` 配下）
  → `templates/paperdesk-read.md` を適用する
- **自分の論文の査読シミュレーション**
  → `templates/paperdesk-review.md` を適用する
- **書籍・その他**（`References/books/` 配下 / `Clippings/` / `Daily/`）
  → `Literature/AGENTS.md` の標準手順に従う

### Promote — 永久ノート作成
対象: `Inbox/` `Literature/` または直接昇華可能な `Daily/` ノート
詳細は `Permanent/AGENTS.md` に従う。

### Wiki-Update — 知識統合ページの更新
対象: `Permanent/` 内の概念・エンティティ・比較ページ
詳細は `Permanent/AGENTS.md` に従う。

### Paper-Work — 論文執筆管理
対象: `Papers/[paper-slug]/`
詳細は `Papers/AGENTS.md` に従う。

### Lint — Vault 健全性チェック
定期実行または要求時:

- 詳細チェックは `rules/lint.md` に従う
- **AGENTS.md 肥大チェック**: root `AGENTS.md` が170行を超えている場合、セッション開始時に不要な詳細手順を `rules/workflows.md` へ分離することを提案する

### Probe — 能動的問いかけ
セッション開始時に自動実行する。

- 最近 Ingest されたノートの中から、既存 Permanent ノートと矛盾・補完・拡張する関係を探し報告する
- `状態: 確定` の Claim のうち、証拠が薄いものを指摘する
- `#open-question` の中から、既存知識で答えられそうなものを提案する
- 長期放置の Permanent ノートを1〜2件取り上げ、最近の知識との接続を問いかける

### Connect — セレンディピティ探索
要求時または Lint と同時に実行する。詳細は `rules/workflows.md` を参照する。

### Remember — 議論の記憶保存
**トリガー**: 「議論を記憶してください」
詳細は `rules/workflows.md` を参照する。

---

## ディレクトリ別の追加規約

サブディレクトリに `AGENTS.md` が存在する場合、そのディレクトリを操作する前に読む。

- `Literature/` → `Literature/AGENTS.md`
- `Permanent/` → `Permanent/AGENTS.md`
- `Papers/` → `Papers/AGENTS.md`
- `References/` → `References/AGENTS.md`

---

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
