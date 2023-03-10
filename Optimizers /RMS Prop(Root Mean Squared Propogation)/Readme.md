# RMS Porp
RMSprop (Root Mean Square Propagation) is a popular optimization algorithm used in deep learning to update the parameters of a neural network. It was introduced by Geoffrey Hinton in 2012 as an improvement over the standard stochastic gradient descent (SGD) optimizer.

The main idea behind RMSprop is to adjust the learning rate for each weight based on the average of the squared gradients for that weight. The algorithm keeps track of an exponential moving average of the squared gradients, which is then used to normalize the learning rate for each weight. This normalization prevents the learning rate from becoming too small or too large, which can slow down the training process or cause it to diverge.

RMSprop is particularly effective in dealing with sparse gradients, which are common in deep neural networks. It has become a popular choice for optimizing neural networks due to its ability to converge faster and produce better results than other optimization algorithms, especially in deep architectures.

Overall, RMSprop is a powerful optimization algorithm that can help accelerate the training of deep neural networks and improve their performance.
$$calculated_-step_-size = \frac {step_-size}{1e-8 + \sqrt {s}}$$
$$s_{t+1} = ((s_t r_{ho}) + (f^1(x^2_t (1 - r_{ho})))$$
