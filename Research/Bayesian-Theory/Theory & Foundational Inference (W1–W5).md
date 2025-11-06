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




先验与后验预测

## week2-week4
#共轭、Jeffreys、层级先验应用



## week5
#后验均值/中位数/贝叶斯因子
