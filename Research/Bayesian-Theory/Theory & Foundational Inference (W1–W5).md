# week1 Bayes_basics
## Bayes Theorem and Examples
### 1.5.1, Discrete case

$$
\Pr(X = x_i \mid Y = y_j)
= \frac{\Pr(X = x_i, Y = y_j)}{\Pr(Y = y_j)}.
$$

which can be rewritten as (Law of joint_probability)

$$
\Pr(X = x_i \mid Y = y_j)
= \frac{\Pr(Y = y_j \mid X = x_i)\,\Pr(X = x_i)}{\Pr(Y = y_j)}.
$$

which can be rewritten as (Law of total_probability)

$$
\Pr(X = x_i \mid Y = y_j)
= \frac{\Pr(Y = y_j \mid X = x_i)\,\Pr(X = x_i)}
{\displaystyle \sum_{k} \Pr(Y = y_j \mid X = x_k)\,\Pr(X = x_k)}.
$$

### 1.5.2 Continuous case

$$
f(x\mid y)
= \frac{f(x,y)}{g(y)}
= \frac{g(y\mid x)\,f(x)}{\displaystyle \int g(y\mid x)\,f(x)\,dx}.
$$

**Joint density surface** $f_{X,Y}(x,y)$ can be viewed as a “surface” standing over the $(x,y)$-plane, where the **height** represents the density.

**Numerator** $f_{X,Y}(x,y)$: fixing both $x$ and $y$ means you take the height at a single point on that surface (just a number). Since we want the **conditional density at a specific $x$**, no integration is needed in the numerator.

**Denominator** $f_Y(y)=\int f_{X,Y}(x,y)\,dx$: fixing $y$ means you sweep along the $x$-direction and add up the area under that slice curve (a one-dimensional integral). More precisely,




## Prior and Posterior (Discrete & Continuous)

> Labels: **Prior**, **Likelihood**, **Evidence**, **Posterior**  
> Minimal formulas + one discrete numeric example + one continuous conjugate example.

---

### A) Discrete

Setup: three mutually exclusive and exhaustive events $A_1, A_2, A_3$; observed event $B$.

**[Prior]**
$$
P(A_1)=0.2,\quad P(A_2)=0.5,\quad P(A_3)=0.3.
$$

**[Likelihood]**
$$
P(B\mid A_1)=0.8,\quad P(B\mid A_2)=0.3,\quad P(B\mid A_3)=0.1.
$$

**1) [Evidence] Law of total probability**
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

### B) Continuous (Conjugate: Exponential–Gamma)

Data: independent samples $y_1,\dots,y_n$ given rate $\lambda>0$.

**[Likelihood]** (Exponential)
$$
y_i\mid \lambda \sim \mathrm{Exponential}(\lambda),\qquad
f(y\mid \lambda)=\lambda^{n}\exp\!\Big(-\lambda\sum_{i=1}^n y_i\Big).
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

### One-line takeaway
$$
\boxed{\text{Posterior}=\dfrac{\text{Likelihood}\times \text{Prior}}{\text{Evidence}}},\qquad
\boxed{p(\theta\mid y)\ \propto\ f(y\mid\theta)\,\pi(\theta)}.
$$



## week2-week4
#共轭、Jeffreys、层级先验应用



## week5
#后验均值/中位数/贝叶斯因子
