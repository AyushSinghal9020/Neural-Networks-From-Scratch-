# Pooling 

A pooling layer in a convolutional neural network (CNN) is a type of layer that reduces the spatial dimensions (width and height) of the feature maps obtained after the convolutional layers. This reduction in dimensions helps to decrease the computational complexity and memory requirements of the network and also helps to control overfitting.

The pooling layer works by applying a pooling function, such as max pooling or average pooling, over a window (also known as the pooling kernel) on the feature map. The window moves over the input feature map, and at each position, the pooling function calculates a single output value by applying a mathematical operation to the values in the window.

Max pooling takes the maximum value in each window, while average pooling takes the average value. The output of the pooling layer is a downsampled version of the input feature map, where each output value represents a summary of the information in the corresponding window of the input feature map.

Overall, the pooling layer helps to reduce the size of the feature maps, which can lead to faster training and better generalization performance of the model.

**Note**
* This notebook is higly inspired by this [stackoverflow answer](https://stackoverflow.com/questions/54962004/implement-max-mean-poolingwith-stride-with-numpy)

**KUDOS TO THE TEACHER**
