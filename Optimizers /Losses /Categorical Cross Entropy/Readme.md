# Categorical Cross Entorpy

<img src = "https://androidkt.com/wp-content/uploads/2021/05/Selection_098.png">

Categorical cross-entropy is a loss function commonly used in machine learning for multi-class classification problems. It measures the dissimilarity between the predicted probability distribution and the true probability distribution of the target variable.

In other words, it calculates the difference between the predicted probabilities of each class and the true probabilities. The predicted probabilities are obtained using a softmax function, which converts the output of a neural network into a probability distribution. The true probabilities are represented as one-hot encoded vectors.

The categorical cross-entropy loss is defined as the negative log-likelihood of the true class, given the predicted probability distribution. The goal of the learning algorithm is to minimize the categorical cross-entropy loss, which means that it tries to make the predicted probabilities as close as possible to the true probabilities.

Categorical cross-entropy is a popular loss function because it is differentiable and relatively easy to optimize. It is widely used in deep learning models for image classification, natural language processing, and other applications that involve multi-class classification problems.

$$CCE = \sum\sum y(log(y))$$
