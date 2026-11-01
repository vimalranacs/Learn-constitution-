# Source policy

`source-check.json` records the local PDF SHA-256, publisher, edition, URL, page, review date and narrow comparison method. `atlas-web/content/parliament.json` is the reviewed export. The checked passage is Article 79 only; do not claim all legacy text has been verified or that this edition necessarily represents every subsequent legal development.

The official URL was located on the Legislative Department domain. Local PDF preface and page 67 were extracted for review. No page numbers were guessed. Educational paragraphs, analogies and diagram relations are authored explanations of the checked passage, not quotations or judicial holdings.

`data/legacy-quarantine.json` preserves all 635 nodes and assigns deterministic IDs to 1,255 legacy edges with `needs_review` status. It is deliberately outside the deployed content tree. Original assertions remain available for audit, but are not promoted by their old labels.

Next source gate: generalize checks into page/span evidence records; audit truncated clauses and footnotes, then review Articles 74–75 and 80–81 with their relevant qualifiers. Do not reuse the old universal source-reference mapping.
