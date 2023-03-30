## Softsign Activation Function
<img src  = "https://www.researchgate.net/publication/332295580/figure/fig6/AS:745763252498436@1554815223676/Curve-of-the-SoftSign-function.jpg">

The Softsign activation function is a continuous and differentiable activation function used in neural networks. It is similar to the sigmoid activation function, but it has a number of advantages over it. 

The Softsign activation function has several advantages over other activation functions such as the sigmoid function. One of the primary advantages is that it does not suffer from the vanishing gradient problem that can occur with the sigmoid function. This means that the Softsign function can be more effective in training deep neural networks.

Another advantage of the Softsign function is that it has a more natural behavior near the extremes of the input range. As the input approaches infinity or negative infinity, the output approaches +1 or -1 respectively. This means that the Softsign function can be more effective in handling large input values.

Overall, the Softsign activation function is a useful activation function to consider when designing neural networks, especially when dealing with large input values and deep networks.

$$f(x) = \frac {x}{1 + |x|}$$

```
x = x / (1 + abs(x)) 
```
