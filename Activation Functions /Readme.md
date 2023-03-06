# Activation Functions

Activation functions are mathematical functions used in neural networks to introduce non-linearity into the output of a neuron. A neuron without an activation function is essentially a linear regression model, which has limited capacity to learn complex patterns in data. Activation functions allow neural networks to model highly non-linear relationships in the input data, enabling them to learn and make predictions on more complex tasks.

There are several types of activation functions, including sigmoid, hyperbolic tangent (tanh), rectified linear unit (ReLU), and softmax, among others. Each type of activation function has its own properties and use cases, and the choice of activation function can have a significant impact on the performance of a neural network.

The sigmoid and tanh functions are commonly used in the hidden layers of a neural network, as they can output values between 0 and 1 or -1 and 1 respectively, and are useful for mapping the input data to a specific range. ReLU, on the other hand, is a popular choice for the output layer, as it can model non-linear relationships while also avoiding the vanishing gradient problem that can occur with sigmoid and tanh functions.

Overall, activation functions are an essential component of neural networks, enabling them to learn and model complex relationships in the input data, and the choice of activation function should be carefully considered based on the specific requirements of the task at hand.

There are majorly diffrent types of activation function 
* Relu(Rectified Linear Activation Function)
* Sigmoid 
* Softmax
* Softplus
* Softsign
* Selu
* Elu
* Exponential

**Modules Used**
* Numpy 
* Math
* IPython
* Seaborn
