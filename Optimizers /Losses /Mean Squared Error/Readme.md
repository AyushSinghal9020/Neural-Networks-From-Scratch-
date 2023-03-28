# MSE (Mean Sqaured Error) 

Mean Squared Error (MSE) is a common metric used to measure the performance of regression models. It measures the average squared difference between the predicted and actual values of a given dataset.

To calculate the MSE, you need to take the difference between the predicted and actual values for each data point in the dataset, square the difference, and then take the average of all these squared differences. This provides an overall measure of how well the model is performing in terms of predicting the target variable.

MSE is a useful metric because it penalizes large errors more heavily than small errors, since the errors are squared. This means that a model with a high MSE is likely making larger errors on average than a model with a lower MSE.

However, MSE is sensitive to outliers in the data, as they can have a large impact on the overall score. In cases where outliers are a concern, other metrics such as Mean Absolute Error (MAE) may be more appropriate.

$$Error = \frac {1}{n}\sum\limits_{i = 1}^{n}(actual - predicted)^2$$
