---
layout: single
permalink: /
title: "Omasheet"
author_profile: true
---

<img src="{{ '/assets/images/header.png' | relative_url }}" alt="Omasheet">

What Markdown is to text, Omasheet is to numbers.

📄 **Text as the source of truth**

The spreadsheet becomes a readable, diffable and composable document, not just a binary workbook.

📊 **Columns as the computational model**

Named, typed data and array expressions connect spreadsheet authoring to dataframe-style transformations.

🔢 **Exact arithmetic as a semantic guarantee**

Numeric values retain their exact decimal or rational meaning instead of floating-point approximations.

_The app automatically follows system dark/light mode._

```omx
const TaxRate = 20%

sheet Sales

| Month | Revenue | Cost | Profit | Tax | Running |
| ----- | ------- | ---- | ------ | --- | ------- |
| Jan   | 10000   | 6000 | *      | *   | *       |
| Feb   | 12000   | 7000 | *      | *   | *       |
| Mar   | 15000   | 8000 | *      | *   | *       |

Profit  := Revenue - Cost
Tax     := Profit * TaxRate
Running := [Revenue; 0..*].sum()
```

<img src="{{ '/assets/images/screenshot.png' | relative_url }}" alt="The Omasheet app, showing the Sales sheet above">

An `.omx` file is plain text: constants, functions and sheets, in any order. A line that starts with `#` is a comment. Formulas are written once per column and apply down every row, so a sheet reads like a small, typed program over its own data.

See [Getting Started](/getting-started/) to install and run Omasheet, and the [Guide](/guide/) for the file format, expressions, the app & CLI, and import/export.
