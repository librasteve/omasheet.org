---
files: [bank.omx]
---
# Current Account Report: August – October 2026

## Summary

| | |
|---|---|
| Opening balance (1 Aug) | **£{{ OpeningBalance }}** |
| Closing balance (31 Oct) | **£{{ Transactions.Balance.last() }}** |
| Total money in | £{{ Transactions.MoneyIn.sum() }} |
| Total money out | £{{ Transactions.MoneyOut.sum() }} |
| Net change | **£{{ Transactions.Net.sum() }}** |
| Transferred to savings | £{{ Transactions.MoneyOut.sum() - Spending.Total.sum() }} |
| Spending (excluding savings) | £{{ Spending.Total.sum() }} |
| Average monthly spending | £{{ round(Spending.Total.sum() / Monthly.len(), 2) }} |
| Transactions | {{ Transactions.len() }} |

Over the quarter the balance rose by £{{ Transactions.Net.sum() }}, while another
£{{ Transactions.MoneyOut.sum() - Spending.Total.sum() }} went to savings. The monthly
surplus is getting smaller, though: it fell from £{{ Monthly[Net; 0] }} in August to
£{{ Monthly[Net; 2] }} in October.

## Month by month

```omx
sheet MonthByMonth := Monthly
```

## Where the money went

Spending by category, excluding transfers to savings. Rent alone takes
{{ ByCategory[Share; 0] }} of spending.

```omx
sheet Categories := ByCategory
```

## Top 10 merchants

Excluding rent and transfers.

```omx
sheet Merchants10 := TopMerchants
```

## Largest discretionary purchases

Excluding rent, bills, utilities and transfers.

```omx
sheet Biggest := Largest
```

## How payments were made

```omx
sheet Methods := ByPaymentType
```

## Observations

- **Eating out** had the most transactions of any category
  ({{ (Spending |> filter(Category == 'Eating Out'))[Count; 0] }}), averaging only
  £{{ (Spending |> filter(Category == 'Eating Out'))[Average; 0] }} each, but they add up to
  £{{ (Spending |> filter(Category == 'Eating Out'))[Total; 0] }} over the quarter.
- **Groceries** are the largest spend you can control, at
  £{{ round((Spending |> filter(Category == 'Groceries'))[Total; 0] / Monthly.len(), 2) }} a month.
- **Contactless** payments were the most frequent
  ({{ (ByPaymentType |> filter(Type == 'Contactless'))[Count; 0] }} payments) but totalled just
  £{{ (ByPaymentType |> filter(Type == 'Contactless'))[Total; 0] }}.
- **October** spending was £{{ Monthly[MoneyOut; 2] - Monthly[MoneyOut; 0] }} higher than in August.
