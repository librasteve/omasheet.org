---
title: "Video: A Bank Statement Report in Omasheet"
date: 2026-11-09T12:00:00
excerpt: "A short screen recording turning a bank statement CSV into a full quarterly report with Omasheet - and the new librasteve YouTube channel."
header:
  teaser: /assets/images/bank-report-video.png
categories:
  - blog
tags:
  - Omarchy
  - Omasheet
  - video
  - update
published: false
---

[![Omasheet: bank transactions report](/assets/images/bank-report-video.png)](https://youtu.be/PJvYvKeAmqY)

I have started a [YouTube channel](https://www.youtube.com/@librasteve) for Omasheet, and the first video is up. It is a screen recording of building a quarterly current account report from a plain bank statement CSV.

Last time we saw how to embed data in a markdown document. This time it is a real(ish) use case: 146 transactions from August to October, turned into a report with:

1. a summary (opening and closing balance, money in and out, net change)
1. month by month totals
1. spending by category and top merchants
1. the largest discretionary purchases
1. how payments were made

All of the numbers in the report text are computed with `{{...}}` expressions straight from the named columns in the `.omx` file, and the arithmetic is exact decimal. Change the data and `omasheet render report.md --html` gives you a fresh report.

Watch it here: [Omasheet: bank transactions report](https://youtu.be/PJvYvKeAmqY) (about 7 minutes).


~librasteve

PS. Click on `feed` below if you would like to hear more ...
