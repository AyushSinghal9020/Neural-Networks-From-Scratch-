|Optimizer|Formula|
|---|---|
|Simple Gradient Descent|$$p_{n} = p_{n-1} - \frac {dLoss}{dp}\alpha$$
|Root Mean Sqaure Propogation|$$p_n = p_{n-1} - \frac {\alpha}{\sqrt{\beta v_{t-1} + (1 - \beta)\frac{dLoss}{dp} + e}}\frac{dLoss}{dp}$$
|Adaptive Gradient Descent |$$w = \frac {\alpha g_{n-1}}{\sqrt{g_n + e}}$$
