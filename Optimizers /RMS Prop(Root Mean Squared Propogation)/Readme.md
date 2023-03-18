# RMS Porp
RMSprop (Root Mean Square Propagation) is a popular optimization algorithm used in deep learning to update the parameters of a neural network. It was introduced by Geoffrey Hinton in 2012 as an improvement over the standard stochastic gradient descent (SGD) optimizer.

The main idea behind RMSprop is to adjust the learning rate for each weight based on the average of the squared gradients for that weight. The algorithm keeps track of an exponential moving average of the squared gradients, which is then used to normalize the learning rate for each weight. This normalization prevents the learning rate from becoming too small or too large, which can slow down the training process or cause it to diverge.

RMSprop is particularly effective in dealing with sparse gradients, which are common in deep neural networks. It has become a popular choice for optimizing neural networks due to its ability to converge faster and produce better results than other optimization algorithms, especially in deep architectures.

Overall, RMSprop is a powerful optimization algorithm that can help accelerate the training of deep neural networks and improve their performance.

$$g_{t} = \nabla_{\theta}J(\theta_{t})$$

$$v_{t} = \gamma v_{t-1} + (1-\gamma)g_{t}^{2}$$

$$s_{t} = \sqrt{v_{t} + \epsilon}$$

$$\theta_{t+1} = \theta_{t} - \frac{\eta}{s_{t}}g_{t}$$

$$\theta_{t+1} = \theta_{t} - \frac{\eta}{\sqrt{v_{t} + \epsilon}}g_{t}$$

$$E[g^2]_t = \beta E[g^2]_{t-1} + (1 - \beta)\frac {dC}{dw}$$
$$w_t = w_{t - 1} - \frac {lr}{\sqrt {E[g^2]_t + epsilon}} \frac {dC}{dw}$$
