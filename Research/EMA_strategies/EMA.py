import pandas as pd
import numpy as np
import math
from Research.research_tools.performance import (
    annualized_return,
    annualized_vol,
    sharpe_ratio,
    max_drawdown,
)
# --------------------
# Params
# --------------------
atr_lookback = 20
ER_lookback = 20
ER_stan = 0.25
stop_muti = 2

entry_slow = 50    # window for slow entry breakout
exit_slow  = 25    # window for slow exit (trailing channel)
entry_fast = 20
exit_fast  = 10

target_risk_per_bar = 0.005
max_leverage = 10

# --------------------
# Data
# --------------------
csv_path = "Research/EMA_strategies/GC_1h_cleaned.csv"  # 确保这个是实际路径
df = pd.read_csv(csv_path)

close = df['Close']
high  = df['High']
low   = df['Low']
close_q = close.shift(1)

# --------------------
# ATR
# --------------------
TR1 = (high - low).abs()
TR2 = (high - close_q).abs()
TR3 = (low  - close_q).abs()

TR  = pd.concat([TR1, TR2, TR3], axis=1).max(axis=1)
df['ATR'] = TR.rolling(window=atr_lookback, min_periods=atr_lookback).mean()

# --------------------
# Efficiency Ratio (ER)
# ER = |Close_t - Close_(t-n)| / sum(|Close_i - Close_(i-1)|, i=t-n+1..t)
# --------------------
df['move_sum'] = close.diff().abs().rolling(window=ER_lookback, min_periods=ER_lookback).sum()
df['net_move'] = (close - close.shift(ER_lookback)).abs()
df['ER'] = df['net_move'] / df['move_sum']

# --------------------
# Channels (Donchian-like)
# --------------------
df['entry_slow_max'] = close.rolling(window=entry_slow).max()
df['entry_slow_min'] = close.rolling(window=entry_slow).min()
df['exit_slow_max']  = close.rolling(window=exit_slow).max()
df['exit_slow_min']  = close.rolling(window=exit_slow).min()

df['entry_fast_max'] = close.rolling(window=entry_fast).max()
df['entry_fast_min'] = close.rolling(window=entry_fast).min()
df['exit_fast_max']  = close.rolling(window=exit_fast).max()
df['exit_fast_min']  = close.rolling(window=exit_fast).min()

# --------------------
# Backtest state
# --------------------
position_dir_list = []   # -1 / 0 / +1
position_size_list = []  # scaled position with leverage
stop_level_list    = []  # trailing stop for current position (NaN if flat)

position_dir = 0        # current direction: -1 short, 0 flat, +1 long
entry_price  = None     # price at entry
entry_atr    = None     # ATR at entry
stop_level   = None     # trailing stop level

start_idx = max(entry_fast, entry_slow, exit_fast, exit_slow, atr_lookback, ER_lookback)

for i in range(start_idx, len(df)):
    atr_now  = df['ATR'].iloc[i]
    er_now   = df['ER'].iloc[i]

    es_m = df['entry_slow_max'].iloc[i]
    es_l = df['entry_slow_min'].iloc[i]
    xs_m = df['exit_slow_max'].iloc[i]
    xs_l = df['exit_slow_min'].iloc[i]

    ef_m = df['entry_fast_max'].iloc[i]
    ef_l = df['entry_fast_min'].iloc[i]
    xf_m = df['exit_fast_max'].iloc[i]
    xf_l = df['exit_fast_min'].iloc[i]

    clp = df['Close'].iloc[i]

    # 1. Entry logic (only if we're flat)
    if position_dir == 0:
        if er_now > ER_stan:
            # detect breakout signals
            long_entry_signal  = False
            short_entry_signal = False

            # Long breakout: price > recent max (fast OR slow)
            if (not np.isnan(es_m)) and (clp > es_m):
                long_entry_signal = True
            if (not np.isnan(ef_m)) and (clp > ef_m):
                long_entry_signal = True

            # Short breakout: price < recent min (fast OR slow)
            if (not np.isnan(es_l)) and (clp < es_l):
                short_entry_signal = True
            if (not np.isnan(ef_l)) and (clp < ef_l):
                short_entry_signal = True

            # Decide direction (no hedging)
            if short_entry_signal and (not long_entry_signal):
                position_dir = -1
                entry_price  = clp
                entry_atr    = atr_now
                stop_level   = clp + stop_muti * atr_now

            elif long_entry_signal and (not short_entry_signal):
                position_dir = 1
                entry_price  = clp
                entry_atr    = atr_now
                stop_level   = clp - stop_muti * atr_now

            else:
                # either both True (conflict) or both False (no signal)
                position_dir = 0
                entry_price  = None
                entry_atr    = None
                stop_level   = None
        else:
            # ER太低，不许开仓
            position_dir = 0
            entry_price  = None
            entry_atr    = None
            stop_level   = None

    else:
        # 2. Exit / manage open position
        exit_now = False

        # 2A. Hard ATR stop
        if position_dir == 1:
            # long -> price falls below stop_level
            if (stop_level is not None) and (clp < stop_level):
                exit_now = True
        elif position_dir == -1:
            # short -> price rises above stop_level
            if (stop_level is not None) and (clp > stop_level):
                exit_now = True

        # 2B. Channel exit: break opposite side of fast/slow exit channels
        if position_dir == 1:
            cond_fast = (not np.isnan(xf_l)) and (clp < xf_l)
            cond_slow = (not np.isnan(xs_l)) and (clp < xs_l)
            if cond_fast or cond_slow:
                exit_now = True

        elif position_dir == -1:
            cond_fast = (not np.isnan(xf_m)) and (clp > xf_m)
            cond_slow = (not np.isnan(xs_m)) and (clp > xs_m)
            if cond_fast or cond_slow:
                exit_now = True

        # Apply exit or trail stop
        if exit_now:
            position_dir = 0
            entry_price  = None
            entry_atr    = None
            stop_level   = None
        else:
            # tighten trailing stop
            if position_dir == 1:
                new_stop = clp - stop_muti * atr_now
                if (stop_level is None) or (new_stop > stop_level):
                    stop_level = new_stop
            elif position_dir == -1:
                new_stop = clp + stop_muti * atr_now
                if (stop_level is None) or (new_stop < stop_level):
                    stop_level = new_stop

    # 3. Position sizing by ATR
    if (atr_now is not None) and (not np.isnan(atr_now)) and (atr_now > 0):
        position_scale = target_risk_per_bar / atr_now
    else:
        position_scale = 0.0

    if position_scale > max_leverage:
        position_scale = max_leverage

    position_size = position_dir * position_scale

    # store results for this bar
    position_dir_list.append(position_dir)
    position_size_list.append(position_size)
    stop_level_list.append(stop_level if stop_level is not None else np.nan)

# --------------------
# Attach results back to df
# 注意：只从 start_idx 往后填，保证长度对齐
# --------------------
df.loc[start_idx:, 'position_dir'] = position_dir_list
df.loc[start_idx:, 'position']     = position_size_list
df.loc[start_idx:, 'stop_level']   = stop_level_list

# 用下一根bar的收益计算策略PnL
df['ret_asset'] = df['Close'].pct_change()
df['position_shifted'] = df['position'].shift(1).fillna(0.0)
df['strategy_ret'] = df['position_shifted'] * df['ret_asset']
df['equity_curve'] = (1 + df['strategy_ret']).cumprod()

ann_ret = annualized_return(df['strategy_ret'], hours_per_year)
ann_vol = annualized_vol(df['strategy_ret'], hours_per_year)
sharpe  = sharpe_ratio(df['strategy_ret'], hours_per_year)
mdd     = max_drawdown(df['equity_curve'])
final_eq = df['equity_curve'].iloc[-1]
