# ADAM
ADAM (Adaptive Moment Estimation) is an optimization algorithm used to update the parameters of a neural network during the training process. It was introduced by Diederik P. Kingma and Jimmy Lei Ba in their 2014 paper "Adam: A Method for Stochastic Optimization".

ADAM combines the benefits of two other optimization algorithms, stochastic gradient descent (SGD) and Root Mean Square Propagation (RMSProp). It keeps track of the first and second moments of the gradients to adaptively adjust the learning rate for each parameter.

The algorithm uses a moving average of the gradient and its squared value, and then calculates the gradient update by dividing the moving average of the gradient by the square root of the moving average of the squared gradient. ADAM also introduces bias correction to the moving averages to help improve convergence.

ADAM has been shown to work well on a wide range of deep learning tasks and is widely used in the field of machine learning. Its benefits include fast convergence, low memory requirements, and robustness to noisy gradients.
$$E[g^2]_t = \beta E[g^2]_{t-1} + (1 - \beta)\frac {dC}{dw}$$
$$w_t = w_{t - 1} - \frac {lr}{\sqrt {E[g^2]_t + epsilon}} \frac {dC}{dw}$$
