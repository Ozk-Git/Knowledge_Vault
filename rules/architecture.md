# Vault アーキテクチャ

## 情報フロー

```
[外部ソース]
  Web記事・SNS → Clippings/    ← 一時置き場。処理後 Done/ へ
  論文PDF      → References/   ← 永続保管庫。読み取り専用
  気づき・メモ → Inbox/ Daily/ ← 未整理のまま投入
                    ↓ Ingest操作
              Literature/       ← 文献ノート（AIが叩き台）
                    ↓ Promote操作
              Permanent/        ← 知識ノート（原子的アイデア + Wiki統合）
                    ↓
                Papers/                       ← アウトプット層
                             ↑
                    [データ解析ディレクトリ（Vault外）]
                    解析結果 → 02_evidence.md に相対パスリンク
```

## Papers/ 構造

```
Papers/[paper-slug]/
├── 00_overview.md   # 主張・ターゲットジャーナル・現在のフェーズ
├── 01_claims.md     # 主張ツリー
├── 02_evidence.md   # 証拠・Permanentリンク・解析結果・コードの対応表
├── 03_gaps.md       # 未解決・追加実験が必要な箇所
├── protocols/       # 実験・解析プロトコール
├── scripts/         # 解析コード
├── results/         # 解析結果のサマリー・図表
└── drafts/          # 本文の下書き（VS Code でも編集可）
```
