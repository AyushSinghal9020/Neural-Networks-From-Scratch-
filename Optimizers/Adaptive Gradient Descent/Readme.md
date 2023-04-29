# Adaptive Gradient Boost

Adagrad (Adaptive Gradient Descent) is an optimization algorithm used in machine learning for gradient-based optimization of a cost function. Adagrad adapts the learning rate of each parameter based on the historical gradient information, effectively giving larger updates to parameters that are less frequently updated and smaller updates to parameters that are frequently updated.

The Adagrad algorithm maintains a separate learning rate for each parameter of the model, which is inversely proportional to the square root of the sum of the squared gradients of that parameter over time. This means that parameters with large gradients will have a smaller learning rate, while parameters with small gradients will have a larger learning rate.

Adagrad is particularly useful for problems where the gradient for some parameters may be much larger than for others, as it allows for a more effective learning rate to be applied to each parameter. However, it may suffer from a diminishing learning rate problem in later stages of training, where the learning rate becomes too small to make further progress. This can be mitigated by using variants of Adagrad such as Adadelta and RMSprop.

****
$$w = \frac {\alpha g_{n-1}}{\sqrt{g_n + e}}$$
****
