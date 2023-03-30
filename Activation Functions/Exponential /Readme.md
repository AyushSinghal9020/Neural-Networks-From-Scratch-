# Exponential 

<img src = "https://i.stack.imgur.com/7aiVh.png">

The exponential activation function is a type of activation function used in artificial neural networks that applies the exponential function to the input. This activation function is also known as the "exponential linear unit" or ELU.

The exponential activation function has some advantages over other activation functions such as the sigmoid or ReLU functions. It provides smooth and continuous outputs, which can make it easier to optimize neural networks during the training process. Additionally, unlike the ReLU function, the exponential activation function does not suffer from the "dying ReLU" problem, where neurons can become permanently inactive during training.

Overall, the exponential activation function is a useful tool for building neural networks, and it has been shown to perform well in certain types of applications. However, like any activation function, it may not be the best choice for every situation, and researchers and practitioners should carefully consider the strengths and limitations of different activation functions when designing neural networks.

$$f(x) = \frac {\alpha e^{x-1}}{x} \frac {for}{for} \frac {x<0}{x>=0}$$

