# Omasheet — Positioning, Target Markets and Unique Selling Propositions

## 1. Vision and philosophy

**Omarchy: We can fix everything.**

**Omasheet: We can fix spreadsheets.**

Omasheet takes inspiration from the Omarchy philosophy that we no longer need to accept the limitations of established tools. With open technology, modern data architectures and increasingly capable AI agents, we can rethink and improve the tools we use every day.

Spreadsheets are an important part of technical and analytical workflows, but their underlying architecture has accumulated decades of compromises.

Omasheet asks a different question:

**What would a spreadsheet look like if we designed it today, for the way technical professionals actually work?**

The answer is a text-native, programmable spreadsheet that brings together readable data, declarative calculations, exact arithmetic, physical units, scientific uncertainty, version control and AI-assisted workflows.

The objective is not simply to replace Excel. It is to make spreadsheets a natural part of modern technical computing.

---

## 2. Core positioning

### The spreadsheet for technical workflows

Omasheet is a text-native, programmable spreadsheet for developers, scientists and engineers who want their data and calculations to work naturally alongside code, Git, modern data tools and AI agents.

It combines:

- The readability and composability of Markdown.
- The structure and computational model of columnar data.
- The numerical rigour of scientific computing.
- The transparency and reproducibility of software development.
- The accessibility and familiarity of spreadsheets.

### Short positioning statement

**Omasheet — We can fix spreadsheets.**

Text-native. Exact. Programmable. Scientific. AI-friendly.

For developers, scientists and engineers who believe spreadsheets can be better.

---

## 3. Target markets

Omasheet targets technical professionals who:

- Use Excel adjacent to their main workflow.
- Are embracing AI for workflow automation.
- Understand the limitations of conventional spreadsheets.
- Work with structured data, calculations and transformations.
- Value transparency, precision and reproducibility.
- Are comfortable with code, technical tools and modern data formats.
- Prefer to improve their tools rather than accept unnecessary limitations.

The initial target market comprises three niches.

### 3.1 Developers

**The spreadsheet as code.**

Developers use spreadsheets for configuration, data inspection, calculations, test data, reporting and ad hoc analysis.

They increasingly want spreadsheet workflows to integrate with their existing software development practices.

Their needs include:

- Text-based source files.
- Git version control and meaningful diffs.
- Readable and maintainable formulas.
- Command-line automation.
- Integration with programming languages and APIs.
- AI-assisted creation and modification.
- Reproducible calculations.

**Omasheet proposition:**

Bring spreadsheet workflows into the software development lifecycle.

### 3.2 Physicists and Engineers

**The spreadsheet as a scientific and computational tool.**

Physicists and engineers use spreadsheets for experimental data, numerical calculations, modelling, measurement analysis and technical reporting.

They need more than approximate arithmetic and unqualified numbers.

Their needs include:

- Exact decimal and rational arithmetic.
- SI units as built-in data types.
- Automatic dimensional analysis.
- Scientific notation.
- Measurement uncertainty.
- Transparent calculation logic.
- Reproducible numerical results.
- Interoperability with scientific software and programming environments.

**Omasheet proposition:**

A spreadsheet that understands the physical meaning of the numbers it contains.

### 3.3 Data Scientists

**The spreadsheet as a data interface.**

Data scientists work with structured datasets, transformations and analytical pipelines.

They already think in terms of columns, schemas and expressions rather than individual spreadsheet cells.

Their needs include:

- Typed, named columns.
- Declarative column calculations.
- Array-oriented expressions.
- Interoperability with CSV, JSON and XLSX.
- Alignment with modern dataframe architectures.
- Integration opportunities with Polars, Pandas and Apache Arrow.
- Version-controlled data transformations.
- AI-assisted data manipulation.

**Omasheet proposition:**

A lightweight, human-readable bridge between spreadsheets and modern data tooling.

---

## 4. Markets not specifically targeted

Omasheet is not primarily designed for conventional business-administration spreadsheet users.

Initial non-target markets:

- Sales: CRM, pipeline tracking and sales forecasting.
- HR: employee records, recruitment and administrative workflows.
- Accounts: bookkeeping, general accounting and conventional financial administration.

This is a positioning decision, not necessarily a technical restriction.

Professionals in these fields who work with technical calculations, data engineering or automation may still find Omasheet useful.

The distinction is between using a spreadsheet as a business application and using a spreadsheet as part of a technical workflow.

---

## 5. Unique Selling Propositions (USPs)

### USP 1 — Text-native spreadsheets

**Spreadsheets can be plain-text documents, just like Markdown.**

Omasheet makes spreadsheet data and formulas readable and editable in ordinary text files.

Benefits:

- Human-readable source.
- Easy editing in any suitable text editor.
- Natural integration with Git.
- Meaningful textual diffs.
- Easy searching and scripting.
- Straightforward AI-agent interaction.
- Data and calculations can live alongside project documentation.

The spreadsheet becomes a first-class document in a software or technical repository.

### USP 2 — Column-oriented data model

**Think in columns, not cell coordinates.**

Omasheet uses named columns and computed-column expressions.

For example:

`Profit := Revenue - Cost`

This expresses a calculation in terms of meaningful data fields rather than cell addresses.

Benefits:

- More readable formulas.
- Less dependence on row and column positions.
- Natural expression of whole-column transformations.
- Conceptual alignment with dataframe processing.
- Easier maintenance and review.
- A natural bridge to modern data-processing tools.

This architecture aligns conceptually with Polars, Pandas and Apache Arrow.

### USP 3 — Exact-precision arithmetic

**Numbers should mean what they say.**

Omasheet supports exact decimal and rational representations.

Benefits:

- Avoids binary floating-point representation errors for supported exact values.
- More predictable equality comparisons.
- Reliable decimal and fractional calculations.
- Reduced need for arbitrary numerical tolerances.
- Better foundations for financial, engineering and scientific calculations.

Exact arithmetic is particularly valuable wherever numerical representation matters.

### USP 4 — SI units as built-in types

**Physical quantities should carry their units.**

Omasheet includes SI units as built-in types.

Units are part of the data and calculation model rather than merely text in column headings.

Benefits:

- Dimensional analysis.
- Detection of incompatible quantities.
- Meaningful physical calculations.
- Systematic unit conversion.
- Reduced risk of unit-related errors.
- More transparent scientific and engineering models.

For example, adding a length to a mass should be identified as dimensionally invalid.

Omasheet brings unit-aware computation directly into the spreadsheet.

### USP 5 — Scientific notation and measurement uncertainty

**Scientific numbers should retain their scientific meaning.**

Omasheet supports scientific notation with uncertainty.

This allows scientific values to be represented with their associated precision and uncertainty rather than being reduced to ordinary unqualified decimal numbers.

Benefits:

- Natural representation of scientific measurements.
- Explicit numerical uncertainty.
- More appropriate handling of significant precision.
- Representation of fundamental physical constants.
- Support for scientific calculations and verification.

An important application is the direct representation of the CODATA 2022 recommended values of fundamental physical constants, including their associated uncertainties.

Reference: https://physics.nist.gov/cuu/Constants/

Combined with SI units and dimensional analysis, this gives Omasheet a particularly strong proposition for scientific computing.

### USP 6 — Declarative formulas

**Describe the calculation, not the cell location.**

Omasheet formulas operate on named columns rather than relying exclusively on conventional cell-coordinate references.

Benefits:

- Greater readability.
- More maintainable calculations.
- Reduced dependence on spreadsheet layout.
- Easier review of calculation logic.
- More natural AI-assisted formula generation.

The spreadsheet becomes a description of the data and its transformations.

### USP 7 — Git-native version control

**Spreadsheet changes should be reviewable.**

Because Omasheet uses text-based source files, spreadsheet changes can participate in normal software version-control workflows.

Benefits:

- Meaningful diffs.
- Change tracking.
- Branching and merging.
- Reviewable formula changes.
- Reproducible project history.
- Easier collaboration through established development tools.

Data, assumptions and calculations can be versioned together.

### USP 8 — AI-native authoring and automation

**AI agents should be able to work directly with spreadsheets.**

Text-native source and declarative formulas make Omasheet a natural fit for AI-assisted workflows.

Benefits:

- AI-generated spreadsheets.
- AI-assisted formula development.
- Automated data transformations.
- Easier inspection and explanation of calculations.
- Small, reviewable source changes.
- Integration with coding-agent workflows.

Rather than requiring an agent to manipulate a graphical spreadsheet interface, Omasheet offers a representation that can be read and modified directly.

### USP 9 — CLI-first automation

**Spreadsheets should participate in automated workflows.**

Omasheet supports command-line-oriented operations and conversion workflows.

Benefits:

- Scriptable spreadsheet processing.
- Automated evaluation.
- Report generation.
- Integration into build and CI pipelines.
- Repeatable data-processing workflows.
- Reduced dependence on manual GUI operations.

This makes spreadsheets useful components of larger technical systems.

### USP 10 — Interoperability

**Use a better source format without abandoning existing tools.**

Omasheet supports exchange with familiar formats including XLSX, CSV and JSON.

Benefits:

- Lower barriers to adoption.
- Reuse of existing spreadsheet data.
- Exchange with established business tools.
- Integration with programming environments.
- A practical migration path from conventional spreadsheets.

Omasheet can complement Excel and Google Sheets rather than requiring immediate replacement.

---

## 6. Features and benefits by audience

| Feature | Developers | Physicists / Engineers | Data Scientists |
|---|---|---|---|
| Text-native format | Git and code integration | Document calculations | Version datasets and transformations |
| Named columns | Readable expressions | Understand calculation inputs | Natural dataframe model |
| Exact arithmetic | Predictable calculations | Numerical precision | Reliable numeric transformations |
| SI unit types | Structured technical data | Dimensional correctness | Typed physical quantities |
| Scientific notation and uncertainty | Structured numerical representations | Scientific measurement | Scientific datasets |
| Declarative formulas | Maintainable logic | Transparent models | Column transformations |
| Git compatibility | Code review | Reproducibility | Data pipeline history |
| AI-friendly source | Coding agents | Calculation assistance | Data automation |
| CLI automation | Build pipelines | Repeatable analysis | Data processing |
| XLSX / CSV / JSON | Existing systems | Experimental data exchange | Data interoperability |

---

## 7. The underlying rationale

### The spreadsheet has outgrown its original architecture

Conventional spreadsheets were designed around an interactive grid of cells.

That model is familiar and useful, but it creates limitations when spreadsheets become part of increasingly sophisticated technical workflows.

Some examples:

- Cell coordinates are a poor abstraction for structured data.
- Binary workbook formats are inconvenient for version control.
- Floating-point arithmetic is not always appropriate.
- Units are often disconnected from numerical values.
- Measurement uncertainty is not naturally represented.
- Manual spreadsheet operations are difficult to automate.
- Spreadsheet logic is difficult for AI agents to manipulate reliably through graphical interfaces.

These are not necessarily failures of Excel or Google Sheets. They reflect design decisions made for a different era and a different primary use case.

### Modern technology changes what is possible

Several developments make a different spreadsheet architecture practical:

1. **Git and text-based development:** Version-controlled documents are now normal technical artefacts.
2. **Modern data architectures:** Columnar data and dataframe expressions provide better abstractions for structured data.
3. **Scientific computing:** Exact numerical representations, unit-aware types and uncertainty handling can be incorporated into spreadsheet semantics.
4. **AI agents:** Text-native, structured files are much easier to inspect and modify than opaque binary workbooks.
5. **Open tooling:** Command-line interfaces and interoperable formats allow spreadsheets to participate in larger automated workflows.

Omasheet brings these ideas together.

---

## 8. Competitive positioning

Omasheet is not primarily competing with Excel and Google Sheets on the breadth of their interactive spreadsheet features.

Instead, it is addressing a different use case.

| Dimension | Excel / Google Sheets | Omasheet |
|---|---|---|
| Primary paradigm | Interactive cell grid | Text-native structured spreadsheet |
| Source representation | Workbook-oriented | Human-readable text |
| Formula model | Primarily cell-oriented | Named-column expressions |
| Version control | Additional tooling required | Natural text-based workflow |
| AI interaction | GUI, APIs and integrations | Direct source-file interaction |
| Numerical semantics | Conventional spreadsheet arithmetic | Exact arithmetic for supported types |
| Physical units | Generally require additional modelling | Built-in SI unit types |
| Scientific uncertainty | Requires additional modelling | Scientific notation with uncertainty |
| Automation | Extensive established ecosystems | Text and CLI-oriented workflows |
| Interoperability | Extensive | XLSX, CSV and JSON exchange |

The intended relationship is complementary:

- Excel remains excellent for general-purpose interactive spreadsheets.
- Google Sheets remains excellent for collaborative cloud spreadsheets.
- Omasheet is designed for technical, scientific and programmable spreadsheet workflows.

---

## 9. Go-to-market messaging

The three audiences should share one product identity but have different entry points.

### Developers

**Stop treating spreadsheets as binary blobs.**

Make spreadsheet data and formulas readable, versionable and programmable.

### Physicists and Engineers

**Your numbers have meaning. Your spreadsheet should understand it.**

Exact arithmetic, SI units, dimensional analysis and scientific uncertainty.

### Data Scientists

**Think in columns, not cells.**

A text-native spreadsheet aligned with modern data-processing concepts.

---

## 10. Brand philosophy and messaging

The connection to Omarchy should be explicit.

Omarchy's philosophy:

**We can fix everything.**

Omasheet's interpretation:

**We can fix spreadsheets.**

The underlying beliefs:

- We don't have to accept unnecessary limitations in established tools.
- We can make data and calculations more transparent.
- We can use better computational abstractions.
- We can make scientific calculations more rigorous.
- We can make spreadsheets work naturally with code and AI.
- We can own and understand the source of our data and calculations.
- We can build tools that work the way we want to work.

This is not about adding more features to a conventional spreadsheet.

It is about rethinking what a spreadsheet can be.

---

## 11. Summary

### Omasheet in one sentence

**Omasheet is a text-native, programmable and scientifically capable spreadsheet for developers, physicists, engineers and data scientists who want spreadsheets to work naturally with modern data tools, version control and AI agents.**

### Three fundamental differentiators

1. **Text as the source of truth:** Readable, editable, versionable and AI-friendly.
2. **Columns as the computational model:** Structured, typed data and declarative expressions.
3. **Scientific correctness as a first-class concern:** Exact arithmetic, SI units, dimensional analysis and scientific uncertainty.

### The ultimate proposition

Omasheet is for people who understand the limitations of conventional spreadsheets and believe those limitations are not inevitable.

It is for people who want to build better tools, embrace AI, work with modern data architectures and retain control over their data and calculations.

**Omarchy: We can fix everything.**

**Omasheet: We can fix spreadsheets.**