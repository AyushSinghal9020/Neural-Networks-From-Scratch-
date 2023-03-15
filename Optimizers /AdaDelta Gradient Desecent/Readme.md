# AdaDelta Gradient Descent 

AdaDelta is an optimization algorithm that is designed to overcome some of the limitations of traditional gradient descent methods, such as the need for manual tuning of learning rates and difficulties in optimizing in high-dimensional spaces.

In AdaDelta, the learning rate is adaptively adjusted during training based on the historical information of the gradients, which allows for more efficient convergence and better handling of sparse gradients.

The algorithm also includes two decaying averages, one for the squared gradients and one for the squared parameter updates, which help to normalize the learning rate and prevent it from becoming too large or too small.

AdaDelta has been shown to work well in a variety of settings, including deep neural networks and natural language processing tasks. It is often used as an alternative to other optimization algorithms such as Adam or RMSProp, and can be particularly effective when working with large datasets or when dealing with sparse gradients.

$$learning_-rate_{new} = \frac {learning_-rate_{old}}{\sqrt {k + e}}$$
$$k_{new} = rk_{old} + (1-r)(gradient_{old}^2)$$
