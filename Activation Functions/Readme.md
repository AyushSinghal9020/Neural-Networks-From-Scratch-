# Activation Functions

An activation function is a function that is applied to the output of a neuron in a neural network. The activation function determines whether the neuron will fire, and how strongly it will fire.

|_____|_____|
|---|---
|$ReLU$|$max(x , 0)$
|$Sigmoid$|$\frac{1}{1+e^{-x}}$
|$Softmax$|$f(x) = \frac {e^{x}} {\sum \limits ^{n} _{i = 1} e^{x}} $
|$Softplus$|$f(x) = log(1 + e^x)$
|$Softsign$|$f(x) = \frac {x}{1 + |x|}$
|$SELU$|$f(x) = \lambda \Bigg [ \frac {x}{\alpha e^x - \alpha} \frac {if}{if} \frac {x>0}{x<=0}$
|$ELU$|$f(x) = \Bigg [ \frac {x}{\alpha (e^x - 1)} \frac {if}{if} \frac {x>0}{x<=0}$
|$Exponential$|$e^x$
|$TanH$|$f(x) = \frac {e^x - e^{-x}}{e^x + e^{-x}}$
