---
name: paperdesk-evidence
description: Use this skill when the user asks whether a scientific claim has evidence, whether a statement is supported by papers, wants an evidence check for health/science claims, asks to verify a claim for an article or manuscript, or mentions PaperDesk Mode D / evidence-check. Follow the Vault's PaperDesk Mode D workflow using Consensus as the main entry point and PubMed, Semantic Scholar, Zotero, or OpenAlex as needed.
---

# PaperDesk Evidence Check

Read `templates/paperdesk-evidence.md` (relative to the Vault root / current working directory) and follow it as the primary workflow.

If the source file is unavailable, perform a concise evidence check:

- Break the user's statement into testable scientific claims.
- Use Consensus as the main entry point when available.
- Use PubMed, Semantic Scholar, Zotero, or OpenAlex as needed to verify primary literature.
- Classify the evidence as: 支持される / 限定的に支持 / 矛盾あり / 根拠不足 / 根拠なしに近い.
- Do not automatically create Literature notes or Ingest records; propose Vault integration only when useful.
- For medical, health, legal, or financial topics, avoid overclaiming and state limitations clearly.
