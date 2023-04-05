# Convolutional Layer

<img src = "https://i.ytimg.com/vi/KuXjwB4LzSA/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDglX1Jo3WO2XUsh9x0ACDpEuNpCQ">

A convolutional layer is a fundamental building block of convolutional neural networks (CNNs), a type of deep learning model commonly used for image classification and computer vision tasks. The convolutional layer applies a set of filters to the input image, which helps to extract features and identify patterns at different spatial scales.

Each filter is a small matrix of weights that slides over the input image and computes a dot product at each position. The output of the convolutional layer is a set of feature maps, where each map corresponds to a specific filter and encodes the presence or absence of a particular visual pattern.

Convolutional layers are often followed by activation functions (such as ReLU) and pooling layers, which help to further reduce the dimensionality of the feature maps and capture higher-level features. By stacking multiple convolutional layers, the neural network can learn increasingly complex representations of the input image.

In addition to convolutional layers, image preprocessing is another important aspect of building effective CNNs. Common preprocessing techniques include resizing the images to a fixed size, normalizing the pixel values, and applying data augmentation techniques (such as rotation, translation, and flipping) to increase the diversity of the training data and prevent overfitting. These preprocessing steps can help to improve the accuracy and generalization of the model.

$$Y_i = B_i + \sum\limits_{i = 1}^{n}(x_{ij} * k_{ij})$$

**Note** - This notebook is hiogly inspired by this [Yoututbe Video](https://www.youtube.com/watch?v=KuXjwB4LzSA)

**KUDOS TO THE TEACHER**

[Image Credits](https://www.youtube.com/watch?v=KuXjwB4LzSA)
