# Prior and Posterior (Discrete & Continuous)

Setup: three mutually exclusive and exhaustive events $A_1, A_2, A_3$; observed event $B$.

**[Prior]**
$$
P(A_1)=0.2,\quad P(A_2)=0.5,\quad P(A_3)=0.3.
$$

**[Likelihood]**
$$
P(B\mid A_1)=0.8,\quad P(B\mid A_2)=0.3,\quad P(B\mid A_3)=0.1.
$$

**1) [Evidence] — Law of total probability**
$$
P(B)=\sum_{i=1}^{3} P(B\mid A_i)\,P(A_i)
=0.8\times0.2+0.3\times0.5+0.1\times0.3
=0.34.
$$

**2) [Posterior]**
$$
P(A_i\mid B)=\frac{P(B\mid A_i)\,P(A_i)}{P(B)}.
$$
$$
P(A_1\mid B)=\frac{0.8\times0.2}{0.34}\approx 0.4706,\qquad
P(A_2\mid B)=\frac{0.3\times0.5}{0.34}\approx 0.4412,\qquad
P(A_3\mid B)=\frac{0.1\times0.3}{0.34}\approx 0.0882.
$$

---

## B) Continuous (Conjugate: Exponential–Gamma)

Data: independent samples $y_1,\dots,y_n$ given rate $\lambda>0$.

**[Likelihood]** (Exponential)
$$
y_i\mid \lambda \sim \mathrm{Exponential}(\lambda),\qquad
f(y\mid \lambda)=\lambda^{n}\exp\!\bigg(-\lambda\sum_{i=1}^n y_i\bigg).
$$

**[Prior]** (Gamma)
$$
\lambda \sim \mathrm{Gamma}(\alpha,\beta),\qquad
\pi(\lambda)\propto \lambda^{\alpha-1}\exp(-\beta \lambda).
$$

**[Posterior]** (Gamma with updated parameters)
$$
p(\lambda\mid y)\ \propto\ f(y\mid \lambda)\,\pi(\lambda)
\;\Rightarrow\;
\lambda\mid y \sim \mathrm{Gamma}\!\Big(\alpha+n,\ \beta+\sum_{i=1}^n y_i\Big).
$$

**[Evidence]** (normalizing constant)
$$
p(y)=\int_0^\infty f(y\mid \lambda)\,\pi(\lambda)\,d\lambda,
$$
which does **not** depend on $\lambda$; it turns “$\propto$” into a proper posterior density.

**Tiny numeric example**  
Let $\alpha=2,\ \beta=1$, observe $n=3$ with $\sum y_i=6$. Then
$$
\lambda\mid y \sim \mathrm{Gamma}(2+3,\ 1+6)=\mathrm{Gamma}(5,7).
$$

---

### Sanity check
This should render as a centered equation:
$$
\int_0^1 \theta^{4}(1-\theta)^{3}\,d\theta=\mathrm{B}(5,4).
$$
