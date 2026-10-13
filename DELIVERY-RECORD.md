# IRC GitHub delivery 0.1.0

Destination: public `arxohq/arxo-irc`. Models are distributed on GitHub, without a model npm package. Runtime: published `@arxo/cli@0.2.4`, Node.js 20+, exact semantics `law.core/0.2.11`.

The frozen checkpoint and original byte identities remain in `source-pin.json`, `frozen/manifest.json`, `frozen/objects/` and `historical/sources.tar.gz`. Current source/compile revision is 0.1.1. Source changes occur in the delivery-owned copies; the private authoring checkpoint is not rewritten.

Addressed evidence:

- All 63 source roots compile natively; own-node inventories and exact output/context hashes are retained.
- All 2,515 frozen objects and 3,575 original source files are hash checked. 371 original projection inputs were directly compared; this does not assert checking all 2,712 original projection inputs.
- 15 reader examples have canonical replay, expected decimal amounts, native `BOTH`, missing-parameter behavior, wash-sale ±30/31 boundaries and explicit/absent §1042 backward dates.
- Native query proof rules and their snapshot annotations are verified separately from direct proof-node anchors. EITC parameter selections are retained. Two selected 2025 IRS parameter cells were spot checked against the official Revenue Procedure.
- Original source and original runtime evidence remain historical. Cyclic authoring dependencies are reproduced through frozen native compiler inputs; individual resolver closure acceptance is not promised.
- README, cover, two flow diagrams and the native EITC unfold were visually previewed. License and government-source provenance are included.

Full package scenario suites and the full corpus were not executed. `releaseVerified: false`; corpus `not_checked`. This addressed delivery does not claim a complete tax-return calculator or legal acceptance.

Public CI is manual and executes the addressed reader checks with the ordinary published npm CLI. Delivery inventory uses the existing `law.canon-publication/1` / `law.canon-manifest/1` exporter and exact file allowlist.
