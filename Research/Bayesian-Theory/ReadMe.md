# 🎓 Bayesian Theory (W1–W10)

This course builds the **computational engine** from static inference to dynamic sampling. Mastering **W8–W10 (MCMC)** is critical for high-dimensional financial models.

---

## I. Theory & Foundational Inference (W1–W5)

| Week | Core Topic | Quant Example |
| --- | --- | --- |
| **W1** | **Bayes’ Theorem** | Asset returns: update beliefs via `p(theta | y) ∝ p(y | theta) * p(theta)` |
| **W2–W4** | **Priors & Hierarchical Modeling** | Use hierarchical models (Sec. 2.5.2) for **shrinkage** to avoid small-sample overfitting across assets. |
| **W5** | **Posterior Analysis** | Use **HPDI (Sec. 3.2.2)** as a conservative threshold for stop-loss or risk gating. |

---

## II. Computational Challenges & the MCMC Core (W6–W10)

When analytic solutions fail, **sampling is essential**.

| Week | Technique | Mechanism | Finance Use |
| --- | --- | --- | --- |
| **W6–W7** | Approximate / Independent MC | Laplace approximation; rejection & importance sampling | Fast validation in low-dim models; tail-prob estimation (e.g., VaR). |
| **W8–W9** | Metropolis–Hastings (MH) | Proposal `q(.))` -> accept with MH ratio `alpha` | General solver for high-dim, non-conjugate models (e.g., heavy-tailed GARCH). |
| **W10** | Gibbs Sampling | Cycle through full conditionals | Efficient for hierarchical & regime-switching models (acceptance ~100%). |
| **W9–W10** | MCMC Diagnostics | Trace plots, R-hat (`R̂`), ESS | Ensure convergence and sufficient effective sample size for trustworthy outputs. |

**MH ratio (schematic):**

/Bayesian-Quant-Notes
├── README.md                 # 总体概览、项目愿景、研究方向（如我们之前所写）
├── /01_Theory_Fundamentals
│   ├── W1_W5_Static_Inference/
│   │   ├── W1_Bayes_Basics.md      # 贝叶斯定理、先验与后验预测
│   │   ├── W2_W4_Priors_and_Hierarchical.md # 共轭、Jeffreys、层级先验应用
│   │   └── W5_Decision_Theory.md   # 后验均值/中位数/贝叶斯因子 (BF)
│   ├── W6_W7_Monte_Carlo_I/
│   │   └── W7_Rejection_Importance_Sampling.ipynb # 拒绝/重要性抽样实现
│   └── W8_W10_MCMC_Engine/
│       ├── W9_Metropolis_Hastings.ipynb     # MH 算法实现（用飓风数据或其他案例）
│       ├── W10_Gibbs_Sampler.ipynb          # Gibbs 抽样实现（用煤矿灾难变点模型）
│       └── W9_MCMC_Diagnostics.md           # R-hat、ESS、迹图的理解与代码实现
│
├── /02_Quant_Modeling_Bridge       # 从理论到金融应用的过渡
│   ├── DBM_01_State_Space_Models.md # 动态贝叶斯模型（DLM, SSM）理论介绍
│   ├── DBM_02_Stochastic_Volatility.ipynb # 随机波动率 (SV) 模型实现 (使用 W10 Gibbs)
│   └── PPL_Tools_Review.md          # PyMC/Stan/Pyro 等概率编程语言对比
│
├── /03_Advanced_Applications
│   ├── App_01_Transformer_Bayes_Fusion/
│   │   └── Transformer_MC_Dropout.ipynb # 使用 MC-Dropout 为 Transformer 预测增加不确定性
│   ├── App_02_TDA_Risk_Modeling/
│   │   └── TDA_Asset_Correlation_Risk.ipynb # 拓扑数据分析（TDA）应用于资产相关性分析
│   └── App_03_Bayesian_Portfolio/
│       └── Bayesian_Portfolio_Optimization.ipynb # 贝叶斯投资组合优化或收缩估计
│
└── /data                         # 存放代码所需的示例数据
