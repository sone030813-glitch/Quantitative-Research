import numpy as np

# annualized_return(returns of asset in each bars, bars quantity annual )
def annualized_return(series, freq_per_year):
    """
    series: 策略每个bar的收益率 (例如每小时的策略收益)
    freq_per_year: 一年包含多少个bar (例如小时线用 24*252)
    返回: 年化收益率 (复利)
    """
    s = series.dropna()
    if len(s) == 0:
        return np.nan

    total_ret = (1 + s).prod() - 1
    n = len(s)
    return (1 + total_ret)**(freq_per_year / n) - 1

# annualized_vol(returns of asset in each bars, bars quantity annual):
def annualized_vol(series, freq_per_year):
    """
    年化波动率 = 单bar收益标准差 * sqrt(freq_per_year)
    """
    s = series.dropna()
    if len(s) == 0:
        return np.nan

    return s.std() * np.sqrt(freq_per_year)

# sharpe_ratio(returns of asset in each bars, bars quantity annual, risk free rate)
def sharpe_ratio(series, freq_per_year, rf=0.0):
    """
    Sharpe = (年化收益 - 无风险利率) / 年化波动率
    rf 默认 0，方便先看策略质量
    """
    ar = annualized_return(series, freq_per_year)
    av = annualized_vol(series, freq_per_year)

    if av == 0 or np.isnan(av):
        return np.nan

    return (ar - rf) / av

# max_drawdown(equity_curve)
def max_drawdown(equity_curve):
    """
    最大回撤 (作为负数，比如 -0.25 = 回撤25%)
    equity_curve: 策略净值曲线，例如 (1 + strategy_ret).cumprod()
    """
    curve = equity_curve.dropna()
    peak = curve.cummax()
    dd = curve / peak - 1.0
    return dd.min()



