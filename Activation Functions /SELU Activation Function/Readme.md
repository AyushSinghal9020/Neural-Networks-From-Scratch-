## SELU (Scaled Exponential Linear Unit)

The Scaled Exponential Linear Unit (SELU) is an activation function used in artificial neural networks that has gained popularity due to its ability to improve training stability and model performance.

SELU is a type of activation function that is self-normalizing, meaning that it can help prevent the vanishing or exploding gradients problem commonly encountered during the training of deep neural networks. This is achieved by ensuring that the output values from each layer of the network have a mean of zero and a standard deviation of one.

In addition to addressing the vanishing gradient problem, SELU has been found to outperform other popular activation functions, such as ReLU and its variants, on a wide range of tasks. This is due in part to the fact that SELU is a smooth function that is differentiable almost everywhere, allowing for more efficient gradient-based optimization during training.

Overall, the SELU activation function has become a popular choice for researchers and practitioners working with deep neural networks, particularly for those seeking to improve the stability and performance of their models.

Formula $$f(x) = \lambda \Bigg [ \frac {x}{\alpha e^x - \alpha} \frac {if}{if} \frac {x>0}{x<=0}$$
