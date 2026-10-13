# Reproduce the pinned delivery

The source is the frozen IRC export `d360a5d5a5cd70fe1bcdc05dccf273bf0cccdb003f14810c9c5a008f596108ca`, checkpoint `ec0486f9909de73ff2e3fa5d802e0d914c7c9608` of `arxohq/arxo-corpus`. The original edition is `USCODE-2024-title26`. [source-pin.json](../source-pin.json) keeps original file hashes; those original bytes address `historical/sources.tar.gz` and frozen model objects, not the edited current source paths.

The original release's 198 recorded import-hash discrepancies remain historical evidence. They are not claimed as 198 repaired independently published registry packages. The authoring dependency graph includes cycles; this GitHub delivery therefore freezes native compiler interface snapshots and independently pinned **reader worlds**, rather than advertising individual resolver releases or a single 63-package tax calculator.

## Current migration

Every delivered compiler unit was rebuilt natively as model `0.1.1`, IR `law.core.ir/0.7`, exact semantics `law.core/0.2.11`, using the published `@arxo/cli@0.2.4`.

- Native `law fix imports` repaired explicit self-import declarations in owned source copies.
- The 133 initially reported negative-calendar diagnostics represented **148 calls in 142 rules**. These now read `civil_calendar_boundary_before` inputs; forward steps remain model operations. [Per-rule input inventory](../reports/backward-boundary-migration.json).
- Two declared collection-financial-standards publication hashes were corrected to the actual unchanged pinned publisher bytes. [Hash repairs](../reports/source-hash-corrections.json).
- Completion-sensitive rules and their strict consumers were moved to the native defeasible producer stratum; formulas and supplied expected answers were retained. [28 rule repairs](../reports/producer-stratum-repairs.json).

The three worlds are built by native `law engine link --merge concat`. A native question cone selects owner snapshots, with supplied fact owners and source-only parameter providers retained explicitly. [worlds/pin.json](../worlds/pin.json) names every exact input and output hash. A selected world includes entire owner packages, so unrelated warnings/positions remain visible.

## Reproduce source lowering

```sh
npm install -g @arxo/cli@0.2.4
node tools/prepare.mjs
python3.12 tools/rebuild.py --package us.irc.core --package us.irc.credits
```

Choose any name in [current-models.json](../reports/current-models.json). This compiles current source with its frozen, native-generated import context and compares the exact output hash. Contexts reference the retained `build-inputs/compiler-seed.tar.gz`; the seed is a compiler input, not an independently admitted resolver closure. The helper contains no tax evaluator or calendar calculator.

Cases and questions were captured by native `law engine lower-ask` from the published `.lawcase` statements and `.lawql` question text. Their full canonical inputs and canonical result documents ship together. The standalone `law eval` vectors use the three exact world receipts. No private resource paths are needed.

## Evidence limits

Original scenario declarations, frozen recorded execution, fresh source compilation and the 15 freshly replayed examples are distinct evidence. Package scenario suites and full corpus acceptance were not run. Full acceptance remains deferred: `releaseVerified: false`, corpus `not_checked`.

The historical report classifies recorded disposition rows with the existing classifier. It does not measure fresh structural section depth; unsupported measures remain `not_measured`. The exact original model and publisher object hashes stay in the frozen manifest. The original private commit is an identity record, not a public link the reader must open.
