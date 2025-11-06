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
