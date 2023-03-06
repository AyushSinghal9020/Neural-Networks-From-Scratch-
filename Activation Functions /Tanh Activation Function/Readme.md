## Exponential Activation Function 

The exponential activation function is a mathematical function commonly used in artificial neural networks as an activation function for the output layer of a network.

Compared to other activation functions such as sigmoid or ReLU, the exponential function has the property of being always positive, and its output increases exponentially as its input increases. This can be useful in certain applications such as modeling growth rates or probabilities.

However, the exponential function also has some drawbacks, such as its unbounded nature which can lead to numerical instability, and its vanishing gradient problem, which can make it difficult to train deep neural networks.

Overall, the exponential activation function can be a useful tool in certain neural network applications, but it should be used with caution and in combination with other activation functions as part of a well-designed network architecture.

Formula $$f(x) = e^x$$

```
import numpy as np

x = np.exp(x)
```
