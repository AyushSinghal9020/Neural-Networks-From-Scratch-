## Softmax Activation Function

Softmax activation function is a widely used activation function in machine learning for multi-class classification tasks. It is a type of exponential function that transforms the output of a neural network into a probability distribution over multiple classes.

The softmax function takes a vector of arbitrary real-valued numbers and converts them into a probability distribution by normalizing the exponentiated values of each element in the vector. In other words, the softmax function squashes the output of a neural network into a set of probabilities that add up to 1, where each probability represents the likelihood of an input belonging to a particular class.

The main advantage of the softmax function is that it provides a probabilistic interpretation of the output of a neural network, which is useful for classification tasks where we want to know the most likely class for a given input. It is also differentiable, which allows for gradient-based optimization methods such as stochastic gradient descent to be used to train the network.

Overall, the softmax activation function is a powerful tool for multi-class classification tasks and is commonly used in neural network architectures such as feedforward neural networks, convolutional neural networks, and recurrent neural networks.

Formula $$f(x) = \frac {e^{x}} {\sum \limits ^{n} _{i = 1} e^{x}} $$

```
import numpy as np 

x = np.exp(x) / np.sum(np.exp(x))
```
