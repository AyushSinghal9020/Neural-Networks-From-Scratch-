# RELU(Rectified Linear Activation Function)
<img src = "https://www.researchgate.net/publication/319235847/figure/fig3/AS:537056121634820@1505055565670/ReLU-activation-function.png">

The Rectified Linear Unit (ReLU) is a widely used activation function in deep learning models. It is a simple function that returns the maximum of zero and the input value. In mathematical terms, it can be expressed as `f(x) = max(0, x)`.

ReLU activation function is preferred over other activation functions like sigmoid and tanh because it is computationally efficient and avoids the vanishing gradient problem. The vanishing gradient problem is a common issue faced in deep neural networks, where the gradients become very small during backpropagation, making it difficult to train the model.

ReLU activation function is also beneficial because it introduces sparsity in the model, which means that a small number of neurons are activated for a given input, leading to faster and efficient computations. However, ReLU has its limitations as it may lead to the problem of dead neurons, where a neuron becomes permanently inactive and stops learning.

In summary, ReLU activation function is a simple yet powerful tool that helps deep learning models to learn efficiently and avoid the vanishing gradient problem.



Formula $$f(x) = \Bigg [ \frac {x}{0} \frac {if}{if} \frac {x > 0}{x < 0}$$
```
x = max(0 , x)
```
