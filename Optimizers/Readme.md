|Optimizer|Formula|
|---|---|
|Simple Gradient Descent|$$p_{n} = p_{n-1} - \frac {dLoss}{dp}\alpha$$
|Root Mean Sqaure Propogation|$$v_t = \beta v_{t-1} + (1 - \beta)\frac{dLoss}{dp}$$
||$$u = \frac {n}{\sqrt{v_t + e}}\frac{dLoss}{dp}$$
||$$p_n = p_{n-1} - u$$
|Adaptive Gradient Descent |$$w = \frac {\alpha g_{n-1}}{\sqrt{g_n + e}}$$
