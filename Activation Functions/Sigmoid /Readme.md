# Sigmoid Activation Function 
<img src = "https://miro.medium.com/v2/resize:fit:970/1*Xu7B5y9gp0iL5ooBj7LtWw.png">

The sigmoid activation function is a commonly used non-linear function in artificial neural networks. It maps any input value to a value between 0 and 1, making it useful for problems where the output is a probability, such as binary classification problems.

The sigmoid function is differentiable, which makes it useful for backpropagation during neural network training. However, it has a few limitations, such as the vanishing gradient problem, which can occur when the input to the function is very large or very small.

Overall, the sigmoid activation function is a popular choice in artificial neural networks, particularly for binary classification problems. However, it is important to consider its limitations and potential drawbacks when using it in a neural network architecture.

Formula $$f(x) = \frac {1}{1 + e^{-x}}$$

```
import math as m

x = 1 / (1 + m.e ** (-x))
```
