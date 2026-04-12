# References/AGENTS.md

`References/` 配下の資料管理規約です。
Vault全体の規約（`../AGENTS.md`）に加えて、このディレクトリ内ではこちらの規約に従います。

---

## このディレクトリの役割

論文PDF・書籍の永続保管庫。**削除しない。Done/へ移動しない。**
Clippings/（一時置き場）とは役割が根本的に異なる。

- `References/_index.md` に文献IDと現在パスの対応表をAIが管理する
- Ingest時にLiterature/に文献ノートを作成し、元PDFはここに残す
- `Papers/[slug]/02_evidence.md` からここへの相対パスリンクを張る
- 年別・プロジェクト別などのサブディレクトリや孫ディレクトリ
  （例: `References/2025/`, `References/project-a/review/`）は任意で使用する
- PDFを移動した場合は、`References/_index.md` を正本として現在パスを更新する

---

## Ingest 時の扱い

- **論文 PDF**: `References/` 配下の任意の場所に置いてよい
  - `templates/paperdesk.md` の**モード A（読解）**を適用する
- **書籍・その他**: `References/` 配下の任意の場所に置いてよい
  - 標準の Ingest 手順で `Literature/` ノート化する

---

## 文献ID管理

### References/_index.md の役割

`References/_index.md` は単なる一覧ではなく、安定IDと現在パスの対応表である。

- `zotero_key` を第一キーとして扱う（Zotero 内部キー。Zotero MCP またはローカル API から取得した8文字英数字）
- `DOI` を第二キーとして扱う
- 書籍など DOI がない資料は `DOI` を空欄可とする

### 更新形式

論文PDFを `References/` の配下に追加・処理した際は、`References/_index.md` を以下の形式で更新する：

`| 現在パス | zotero_key | DOI | タイトル | 著者 | 年 |`

### 移動時の扱い

- PDF を `References/` 内で移動した場合は、`zotero_key` または `DOI` で既存行を特定し、`現在パス` を更新する
- `Papers/[slug]/02_evidence.md` や `Literature/` ノートの古いパスは、再同定できた場合は現在パスへ修正する

### リンク切れ時の扱い

- `References/` へのリンク切れを検出した場合、`References/_index.md` の `zotero_key` / `DOI` で再同定する
- 見つかった場合は、参照しているノートや `02_evidence.md` のリンク先を修正する

---

## MCP連携

> **注意**: 各 MCP サーバーは別途セットアップが必要です。利用可能な場合、以下のツールを使用して文献検索・引用管理を行います。

### 利用可能な MCP サーバーと用途

- **PubMed MCP**: キーワード・概念による医学・生物学文献検索
- **Consensus MCP**: エビデンス検索・科学的主張の裏付け確認
- **Scholar Gateway**: 広範な学術論文の探索とメタデータ取得
- **Zotero MCP**: 引用キー取得・ライブラリ管理・参考文献フォーマット生成

### Zotero ライブラリからの文献取得

Zotero を使っている場合、ライブラリ内の PDF を直接 Vault で利用できる。

**接続方法（優先順）**

1. **Zotero MCP**（インストール済みの場合）: ライブラリを直接検索し、メタデータと PDF パスを取得する
2. **Zotero ローカル API**（MCP 不要・Zotero 起動中のみ）: `http://localhost:23119/api/` に WebFetch でアクセスする。Zotero の設定で「ローカル API を有効にする」をオンにする必要がある

**PDF の扱い方針**

| 用途 | 方針 |
|---|---|
| 1回限りの参照・読解 | Zotero ストレージのパスから直接読む。`References/` にコピーしない |
| Papers/ のキー文献として確定した場合 | `References/` にコピーし、`_index.md` に登録する |

PDF のパスは必ず Zotero MCP またはローカル API から取得してから Read ツールで読む。
デフォルトストレージ（`~/Zotero/storage/[KEY]/`）とは異なる場所にある場合（ZotMoov 等のリンクファイル管理を使用している場合）も、API が実際のパスを返すため問題ない。パスを推測しない。

**読解時の適用ルール**
Zotero から取得した論文 PDF を読む場合は、`References/` にコピーするかどうかに関わらず、以下を実行する:

1. `templates/paperdesk.md` の**モード A（読解）**を適用する
2. `Literature/[著者名][年]-[キーワード].md` に文献ノートを作成する。`source:` の代わりに `zotero_key:` を主キーとして記録する
3. `References/_index.md` にエントリを追加する。`現在パス` は Zotero API から取得した実際のパスを記録する。後から `References/` にコピーした場合はパスを更新する

### 引用操作の標準手順

1. **探索**: Zotero ライブラリ / PubMed / Consensus / Scholar Gateway を用いて文献を特定
2. **読解**: PDF を直接読むか `References/` にコピーして `paperdesk.md` モード A を適用する
3. **登録**: Zotero MCP でライブラリに追加し、一意の引用キー（Citekey）を取得
4. **記録**: `Papers/[slug]/02_evidence.md` に引用キーと `References/` 内の相対パスを記載する
5. **出力**: 執筆時に Zotero MCP から指定ジャーナル形式の参考文献リストを生成
