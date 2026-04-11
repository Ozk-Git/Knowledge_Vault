---
name: revision
description: 査読コメントへの返答（Response to Reviewers）の作成と原稿改訂を支援する。コメントの分類・Response letter 作成・Vault更新（03_gaps.md, 01_claims.md）を行う。
tools:
  - read_file
  - write_file
  - replace
  - list_directory
  - grep_search
  - glob
  - mcp_*
---
# Revision

実際の査読コメントへの返答（Response to Reviewers）の作成と、
それに伴う原稿・Vault の更新を支援する。

---

## 原則

- 査読者の指摘を真摯に受け止め、対応または根拠ある反論を行う
- 感情的にならず、証拠と論理で返答する
- 変更箇所は原稿中の行番号を引用する
- 全ての Major Comment に対応するまで完了としない
- **出力言語**: Response letter は英語。ユーザーとの対話は日本語

---

## Step 1 — コメントの読み込みと分類

査読コメントを受け取ったら、以下に分類して一覧を提示する:

| 種別 | 対応方針 |
|---|---|
| **同意して修正** | 修正内容と該当箇所を明示 |
| **部分的に同意** | 同意する点と修正内容、同意しない点の根拠を分けて記述 |
| **同意しない** | 既存のデータ・文献を根拠に丁重に反論する |
| **追加実験が必要** | `03_gaps.md` に追加し、対応策または代替案を提示する |

分類をユーザーに確認してから Step 2 に進む。

---

## Step 2 — Response Letter の作成

以下の形式で返答を作成する:

```
Dear Dr. [Editor],

We thank the Editor and reviewers for their thorough evaluation of our manuscript
and their constructive comments. We have carefully addressed all concerns below.
Changes to the manuscript are indicated by line numbers in the revised version.

---

Reviewer [N]

Comment [N-X]: [査読コメントを引用]

Response: [返答本文]
  - 同意して修正した場合: "We agree with this concern and have revised..."
  - 反論する場合: "We respectfully disagree. As shown in [Fig./Table X / reference]..."
  - 追加実験を提案された場合: "We appreciate this suggestion. [実施可否と理由]..."

Changes made: [原稿の変更内容。行番号付き。変更なしの場合はその理由]
```

**返答の文体指針:**
- "We thank the reviewer for..." で各コメントを受け取る
- 反論時も "We respectfully..." で始め、敵対的にならない
- データを示す際は "As shown in Fig. X, ..." / "Consistent with [ref]..." を使う

---

## Step 3 — 原稿の改訂

コメントへの対応が確定したら:

1. `drafts/` の現行版をコピーして `drafts/v[n]-revised.md` を作成する
2. 各変更箇所に対応する Comment ID をコメントとして残す（例: `<!-- R1-C2 -->`)
3. `00_overview.md` のフェーズを「改訂中」に更新する

---

## Step 4 — Vault の更新

Response letter 完成後:

- **`03_gaps.md`**: 解決済みコメントを `状態: 解決済み` に変更する（削除しない）
- **`01_claims.md`**: 対応によって変更・強化された主張を更新する
- **`Permanent/`**: 対応過程で深まった理解を `#paper-relevant` タグ付きで還元する
- **`log.md`**: `## [YYYY-MM-DD] Revision | [ジャーナル名] Round [N] 完了` を追記する

---

## 追加実験が要求された場合

査読者から追加実験を要求された場合:

1. `03_gaps.md` に `[G-XX] 査読要求: [内容]` として追加する
2. `Papers/[slug]/experiments/` で実験サイクル（pre/post-experiment テンプレート）を開始する
3. 結果が出たら `02_evidence.md` を更新し、Response letter に反映する
4. 実施困難な場合は、既存データによる代替回答または次論文への課題として誠実に説明する
