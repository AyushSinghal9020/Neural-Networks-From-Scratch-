# Gradient Descent 

Gradient Descent is an iterative optimization algorithm used to find the minimum of a function. It is widely used in machine learning and artificial intelligence to update the parameters of a model to minimize the loss function.

The idea behind gradient descent is to take steps in the direction of the negative gradient of the function, which indicates the direction of steepest descent. The size of each step is determined by the learning rate, which controls the rate at which the algorithm converges.

There are three variants of gradient descent: batch gradient descent, stochastic gradient descent, and mini-batch gradient descent. Batch gradient descent computes the gradient of the entire dataset, while stochastic gradient descent computes the gradient of a single example at a time. Mini-batch gradient descent computes the gradient of a small batch of examples.

Gradient descent can be susceptible to getting stuck in local minima, so advanced techniques like momentum, AdaGrad, RMSProp, and Adam are often used to improve convergence and prevent overshooting.

Overall, gradient descent is a powerful optimization algorithm that is essential for training machine learning models.

**Modules Used**
* Numpy 
* Pandas 
* Sklearn

**Note**
* Pandas was only used to import the dataset
* Sklearn was only used to validate the build 
* This is the [dataset](https://github.com/VikParuchuri/zero_to_gpt/blob/master/data/clean_weather.csv) used 
