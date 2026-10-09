# belligerent

**The aggressive / hedge-fund book capstone — `bulkhead`'s opposite number.**

Where [`bulkhead`](https://github.com/blaquebaux/bulkhead) is preservation (positive skew, shallow
drawdown), belligerent is the aggressive posture: lever the return-seeking keepers for an absolute-return
mandate that tolerates deep drawdowns. The corpus already says these sleeves are mostly **beta**, so the
honest aggressive edge isn't new alpha — it's **disciplined leverage**: vol-target the return-seekers to
extract return per unit of *controlled* risk, instead of the naive-leverage ruin shape `bravado` flagged.

## Verdict

**KEEPER (aggressive mandate), regime-flattered.** Vol-targeted leverage beats the index on return,
Sharpe, *and* Calmar, and it crushes naive leverage — the vol-target turns a would-be ruin shape into a
survivable aggressive book. The honest costs are negative skew and a single bull regime that flatters
leverage; the true test is 2008 (`belligerent_2`).

| book | Sharpe | CAGR | vol | maxDD | worst mo | skew | Calmar |
|---|---|---|---|---|---|---|---|
| **BELLIGERENT** (vol-tgt, ~1.4× avg) | **+1.02** | **+19.3%** | 19% | −30% | −12.3% | −0.56 | **+0.65** |
| return-seekers (unlevered) | +0.99 | +15.8% | 16% | −28% | −10.6% | −0.28 | +0.57 |
| UPRO (naive 3× SPY) | +0.75 | +29.1% | 52% | **−77%** | **−48.1%** | −0.40 | +0.38 |
| QQQ | +0.93 | +19.9% | 22% | −35% | −13.6% | −0.20 | +0.57 |
| SPY | +0.88 | +15.0% | 18% | −34% | −12.6% | −0.35 | +0.44 |

*Book: 40 QQQ / 30 MTUM / 15 GLD / 15 EMB, vol-targeted to 18% (cap 2×), causal, financed at BIL, 2 bp/side. 2016-01 … 2026-07 (10.5y).*

## What the leverage discipline buys

- **Beats the index on every axis** — +19.3% vs SPY's +15.0% CAGR, Sharpe +1.02 vs +0.88, Calmar +0.65
  vs +0.44 — at a drawdown (−30%) *shallower* than SPY's (−34%). The return came from leverage; the
  survivability came from the vol-target cutting exposure when vol rose.
- **It is not naive leverage.** UPRO (3×) posts a bigger CAGR (+29%) but a **−77% drawdown and a −48%
  month** — a textbook `bravado` ruin shape. BELLIGERENT gets two-thirds of the return at *under half*
  the drawdown and a far higher Sharpe. Disciplined vs naive leverage is the whole point.
- **It de-levers into crises.** COVID 2020-03: BELLIGERENT −7.2% vs UPRO −48.1% vs SPY −12.6% — the
  vol-target had already cut exposure as vol spiked. Same mechanism, 2022.

## The honest costs

- **Negative skew (−0.56)** — worse than SPY's −0.35. Leverage always thickens the left tail; the
  vol-target bounds it but can't erase it. This is the aggressive mandate's accepted price.
- **One bull regime.** 2016–2026 was the best possible decade for a QQQ/MTUM-heavy levered book; leverage
  flatters a bull. A 1.4× tech-growth book in 2008 is a different story — the vol-target helps, but levered
  beta in a secular bear is brutal.
- **Idealized financing.** Leverage is financed at `BIL` (T-bill); a real book pays a spread over that and
  borrow on the levered portion. Modest here, material at scale.

## `belligerent_2`

Full-cycle on Massive's 2003+ history **through 2008** (where levered beta gets its true test), with real
financing/borrow costs and a crypto-trend sleeve added (it belongs in the aggressive book but truncates
the Alpaca window). Until then, read the keeper verdict as "in a bull decade, with honest caveats."

## Capstone pair

`belligerent` (aggressive) and `bulkhead` (preservation) are the two mandate poles over the same keeper
set: one levers the return-seekers to +19% at −30% and negative skew; the other dampens to +7.6% at −12%
and positive skew. Same ingredients, opposite postures — which is the capstone thesis: the sleeves are
ingredients, the archetype is how you size them.

## Reproduce

```bash
export ALPACA_KEY_ID=... ALPACA_SECRET_KEY=...
python3 research/belligerent_1.py
```

---

*Blaque Baux — a Carter Warrens research initiative. Research only; not investment advice. The verdict
falls where the data puts it — and leverage always looks best in the decade that didn't crash.*
