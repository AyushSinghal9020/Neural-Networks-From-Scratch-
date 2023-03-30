# Tanh
<img src = "https://production-media.paperswithcode.com/methods/Screen_Shot_2020-05-27_at_4.23.22_PM_dcuMBJl.png">

The hyperbolic tangent function, or tanh, is a popular activation function used in neural networks. It maps input values to a range between -1 and 1/

Compared to the sigmoid function, another common activation function, the tanh function is zero-centered, meaning its outputs are centered around zero. This makes it useful in situations where the mean of the input data is important, such as in image processing tasks where the pixel values range from 0 to 255.

Like the sigmoid function, the tanh function is also prone to the vanishing gradient problem, where gradients become very small as the input moves far away from zero, which can slow down or prevent learning in deep networks.

Despite this drawback, the tanh function is still widely used in practice, particularly in recurrent neural networks (RNNs) and convolutional neural networks (CNNs).

$$f(x) = \frac {e^x - e^{-x}}{e^x + e^{-x}}$$

```
import math as m 

x = ((m.e ** x) - (m.e ** (-x))) / ((m.e ** x) + (m.e ** (-x)))
```
