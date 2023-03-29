# MAE 

<img src = "https://jmlb.github.io/images/20180701/img_01.png">

Mean Absolute Error (MAE) is a commonly used metric in regression analysis to evaluate the accuracy of a model's predictions. It measures the average difference between the predicted and actual values of the target variable.

The MAE is measured in the same units as the target variable, which makes it easy to interpret. A lower MAE value indicates better accuracy of the model's predictions, whereas a higher MAE value indicates poorer accuracy.

MAE has some advantages over other metrics such as mean squared error (MSE) as it is less sensitive to outliers, since it does not involve squaring the differences between actual and predicted values. However, it may not penalize larger errors as strongly as MSE.

$$MAE = \frac {1}{n}\sum\limits _{i = 1}^{n}|actual - predicted|$$
