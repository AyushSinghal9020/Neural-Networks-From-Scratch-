## Softplus Activation Function 
<img src = "https://pytorch.org/docs/stable/_images/Softplus.png" width = 400>

The Softplus activation function is a type of non-linear activation function used in neural networks. The softplus function has a similar shape to the ReLU activation function but with a smoothed out slope. It maps any input value to a positive output value, which makes it suitable for activations in the output layer for regression problems where the output should be a positive value.

The Softplus function is also used in some neural network architectures to replace the sigmoid or tanh activation functions, as it can help prevent the vanishing gradient problem that can occur with these functions.

Overall, the Softplus activation function has become increasingly popular in neural networks due to its smoothness and positive outputs, which make it particularly useful in some specific types of problems.

$$f(x) = log(1 + e^x)$$
```
import numpy as np 

x = np.log(1 + np.exp(x))
```
