#!/usr/bin/python3
# =============================================================================
# belligerent_1.py — the AGGRESSIVE / hedge-fund book capstone (bulkhead's opposite number).
#
# The aggressive posture: lever the return-seeking keepers for an absolute-return mandate that tolerates
# deep drawdowns. The corpus already says these are mostly BETA, so the honest aggressive edge isn't new
# alpha — it is EFFICIENT leverage: vol-target the return-seekers to extract return per unit of
# *controlled* risk, instead of the naive-leverage ruin bravado flagged (UPRO's −77% is a steamroller).
#   Q1  Does vol-targeted leverage beat the index on return — at a drawdown you'd actually survive?
#   Q2  Disciplined leverage vs NAIVE leverage (UPRO 3x) — does the vol-target tame the tail?
#   Q3  The honest cost — skew/worst-month; is it a ruin shape or a survivable aggressive book?
# Judged on RETURN + risk-adjusted (the mandate accepts volatility). Alpaca SIP daily; causal; 2bp/side.
# =============================================================================
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from _belligerent_common import panel, rets

COST = 2e-4; TARGET = 0.18   # 18% annualized vol target

def metrics(r, months):
    r = np.asarray(r, float); c = np.cumprod(1+r); dd = (c/np.maximum.accumulate(c)-1).min()
    sh = r.mean()/r.std()*math.sqrt(252) if r.std()>0 else float("nan"); z=(r-r.mean())/r.std()
    cagr = c[-1]**(252/len(r))-1
    mo = {}
    for m,x in zip(months,r): mo[m]=mo.get(m,1.0)*(1+x)
    return dict(sh=sh, cagr=cagr, dd=float(dd), vol=r.std()*math.sqrt(252), skew=float(np.mean(z**3)),
                worst=min(v-1 for v in mo.values()), calmar=cagr/abs(dd) if dd<0 else float("nan"))

def vol_target(base, cash, target=TARGET, cap=2.0, floor=0.3, w=63):
    n=len(base); lev=np.ones(n)
    for t in range(1,n):
        v = np.std(base[max(0,t-w):t])*math.sqrt(252) if t>w else np.std(base[:t])*math.sqrt(252) if t>5 else target
        lev[t] = min(cap, max(floor, target/v)) if v>0 else 1.0
    switch=np.abs(np.diff(np.concatenate([[1.0],lev])))
    return lev*base - (lev-1)*cash - switch*COST, lev

def main():
    syms = ["QQQ","MTUM","GLD","EMB","SPY","UPRO","BIL"]
    P, dates = panel(syms); R = {s: rets(P[s]) for s in P}
    L = min(len(R[s]) for s in R); months=[d[:7] for d in dates[1:]][-L:]
    r = {s: R[s][-L:] for s in R}
    base = 0.40*r["QQQ"] + 0.30*r["MTUM"] + 0.15*r["GLD"] + 0.15*r["EMB"]   # return-seeking keeper book
    belg, lev = vol_target(base, r["BIL"])
    print("="*94); print("BELLIGERENT — the aggressive / hedge-fund book capstone (vol-targeted leverage)"); print("="*94)
    print(f"  window {dates[-L]}..{dates[-1]}  ({L/252:.1f}y)   book: 40 QQQ / 30 MTUM / 15 GLD / 15 EMB, vol-target {int(TARGET*100)}% (cap 2x)")
    print(f"  avg leverage {lev.mean():.2f}x  (range {lev.min():.2f}–{lev.max():.2f})")
    print(f"\n  {'book':26}{'Sharpe':>8}{'CAGR':>8}{'vol':>7}{'maxDD':>8}{'worstMo':>9}{'skew':>7}{'Calmar':>8}")
    rows = [("BELLIGERENT (vol-tgt)", belg), ("return-seekers (unlevered)", base),
            ("UPRO (naive 3x SPY)", r["UPRO"]), ("QQQ", r["QQQ"]), ("SPY", r["SPY"])]
    for nm, x in rows:
        m = metrics(x, months)
        print(f"  {nm:26}{m['sh']:>+8.2f}{m['cagr']*100:>+7.1f}%{m['vol']*100:>6.0f}%{m['dd']*100:>+7.0f}%{m['worst']*100:>+8.1f}%{m['skew']:>+7.2f}{m['calmar']:>+8.2f}")

    # crisis grid
    print("\n  CRISIS MONTHS (book return)")
    tests=[("2020-03","COVID"),("2022-06","inflation"),("2022-09","rate shock"),("2025-04","tariffs")]
    print(f"    {'book':26}"+"".join(f"{lbl:>12}" for _,lbl in tests))
    for nm,x in (("BELLIGERENT",belg),("UPRO 3x",r["UPRO"]),("SPY",r["SPY"])):
        row=""
        for mm,_ in tests:
            idx=[i for i,m in enumerate(months) if m==mm]; row+=f"{(np.prod([1+x[i] for i in idx])-1)*100 if idx else float('nan'):>+11.1f}%"
        print(f"    {nm:26}{row}")

    print("\n  READ: the aggressive edge is DISCIPLINED leverage, not new alpha. If BELLIGERENT beats SPY on")
    print("  CAGR at a drawdown far shallower than naive UPRO (which is a bravado-style ruin shape), the")
    print("  vol-target earned its keep — a survivable aggressive book. If its skew/DD look like UPRO's, it's")
    print("  just amplified beta. CAVEAT: one bull regime; leverage flatters it. belligerent_2 = full-cycle +")
    print("  real financing/borrow costs (Massive 2003+ across 2008, where levered beta gets its true test).")

if __name__ == "__main__":
    main()
