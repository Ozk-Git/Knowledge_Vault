# Papers/AGENTS.md

論文執筆ワークスペースの操作規約です。
Vault全体の規約（`../AGENTS.md`）に加えて、このディレクトリ内ではこちらの規約に従います。

---

## このディレクトリの構造

```
Papers/
└── [paper-slug]/
    ├── 00_overview.md   # 主張・ターゲットジャーナル・現在のフェーズ
    ├── 01_claims.md     # 主張ツリー
    ├── 02_evidence.md   # 証拠・Permanentリンク・解析結果・コードの対応表
    ├── 03_gaps.md       # 未解決・追加実験が必要な箇所
    ├── protocols/       # 実験・解析プロトコール（手順書・バージョン管理）
    ├── experiments/     # 実験ノート（日付付き実施記録・プロトコルへの参照）
    ├── scripts/         # 解析コード（Python, R, Shell等）
    ├── results/         # 解析結果のサマリー・図表
    └── drafts/          # 本文の下書き
```

- `protocols/` と `experiments/` は役割が異なる。手順書は `protocols/` が正本。`experiments/` はプロトコルを参照するだけにして内容の重複を避ける。

新しい論文プロジェクトを始めるときは、`../templates/paper-overview.md` を使って
`[paper-slug]/00_overview.md` を作成することを促す。

---

## 原則

- **主張（claim）と証拠（evidence）を常に対応させる**
  根拠のない主張を `01_claims.md` に書かない。
  証拠が不十分な主張には `[要証拠]` を明示する。
- **未解決事項は消さず `03_gaps.md` に残す**
  解決済みになったら打ち消し線（`~~`）で記録し、削除しない。
- **Vault外のデータは移動・編集しない**
  `02_evidence.md` からの相対パスリンクで参照するのみ。
- **論文から生まれた知見は必ず `../Permanent/` に還元する**
  Papers/ は執筆の場。知識の蓄積場所は Permanent/ である。

---

## 操作定義

### 新規プロジェクトの開始

1. `../templates/paper-overview.md` を使って `[slug]/00_overview.md` を作成する
2. `01_claims.md` `02_evidence.md` `03_gaps.md` の空ファイルを作成する
3. `../index.md` の Papers/ セクションに追記する

### 主張の追加・整理（01_claims.md）

記載形式:
```
## [C-XX] 主張のタイトル
内容: （主張を1文で）
状態: 確定 / 検討中 / 要証拠
関連Evidence: E-XX, E-XX
```

- 主張間の依存関係を階層で示す
- `状態: 要証拠` の主張が残っている場合は作業完了としない

### 証拠の追加（02_evidence.md）

記載形式:
```markdown
| ID | 証拠の概要 | Permanent リンク | 解析結果・図表 | 解析コード | プロトコール | zotero_key |
|---|---|---|---|---|---|---|
| E-01 | ProteinX は条件 Y でのみ発現増加 | [ProteinX の発現制御](../../Permanent/ProteinX-発現制御.md) | ./results/fig1a.png | ./scripts/plot_exp.py | ./protocols/exp_v2.md | Smith2024 |
```

- `Permanent リンク` は必ず記載する。なければ Promote 操作を先に行う
- `解析結果・図表` `解析コード` `プロトコール` は `Papers/[slug]/` 内の相対パスを記載する
- Vault 外の大規模データ等は、`../../analysis/` のように Vault 外への相対パスリンクで参照する
- `zotero_key` は Claude Code + Zotero MCP で取得・管理する
- `References/` 内のPDF移動時は、`References/_index.md` の `zotero_key` または `DOI` を用いて最新の相対パスへ更新する

### 未解決事項の管理（03_gaps.md）

記載形式:
```
## [G-XX] 未解決事項のタイトル
内容: （何が不足しているか）
関連Claim: C-XX
対応策: （追加実験・文献調査など）
状態: 未着手 / 対応中 / 解決済み
```

- 解決済みになったら `状態: 解決済み` に変更し、削除はしない
- `状態: 未着手 / 対応中` の項目は `../Permanent/` に `#open-question` として反映する

### 健全性チェック（Paper-Lint）

以下を確認して報告する:

- `01_claims.md` に `状態: 要証拠` の主張が残っていないか
- `02_evidence.md` の解析結果パスが実際に存在するか
- `03_gaps.md` の未解決事項が `../Permanent/` に `#open-question` として反映されているか
- `00_overview.md` のフェーズと実際のファイル状態が一致しているか
- `drafts/` の内容と `01_claims.md` の主張に齟齬がないか
- `References/` へのリンク切れがあれば、`References/_index.md` の `zotero_key` / `DOI` で再同定し、見つかれば `02_evidence.md` の相対パスを修正する

### 実験サイクル（experiments/）

1. 実験前: `templates/pre-experiment.md` で計画と設計の弱点を確認する
2. 実施中: `experiments/YYYY-MM-DD_xxx.md` で記録する
3. 実験後: `templates/post-experiment.md` で解釈対話を行う
4. 還元: 解釈から得た知見を `Permanent/` に還元し、`01_claims.md` と `02_evidence.md` を更新する

### 知見の還元（Permanent への書き戻し）

論文執筆中に生まれた知見を Permanent/ に還元するタイミング:

- 新しいデータ解析の結果が出たとき
- 文献調査で重要な概念が整理されたとき
- `03_gaps.md` の未解決事項が解決されたとき
- 査読コメントへの対応で理解が深まったとき

還元する際は `../templates/permanent-note.md` を使い、`#paper-relevant` タグを付ける。

---

## ディレクトリ別の追加規約

このディレクトリにサブ規約は現在存在しない。

---

## サンプルプロジェクト

`Papers/example-project/` は新規ユーザー向けのサンプルです。
実際の作業を始める際は削除して構いません。`#example` タグが付いています。