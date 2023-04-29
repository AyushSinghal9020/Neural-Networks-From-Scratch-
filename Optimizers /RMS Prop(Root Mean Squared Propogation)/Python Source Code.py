# METHOD 1

class rms_prop:
    def __init__(X , y , 
                 learning_rate = 0.01 , rho = 0.9 , 
                 momentum = 0 , epsilon = 1e-7 , 
                 clip_norm = None , clip_value = None , 
                 ema = False , ema_momentum = 0):
        
        self.X = X
        self.y = y
        self.learning_rate = learning_rate
        self.rho = rho
        self.momentum = momentum
        self.epsilon = epsilon
        self.clip_norm = clip-norm
        self.ema = ema
        self.ema_momentum = ema_momentum

    def build(self , weights = None , biases = None):
        
        if weights == None:
            
            self.weights = abs(np.random.randn(self.X.shape[1]))
        
        else :
            
            if weights.shape[1] == self.X.shape[1]:
                
                self.weights = weights
            
            else :
                
                raise UserWarning("Shapes do not match. Using random variables")
                self.weights = abs(np.random.randn(self.X.shape[1]))

        if biases == None:
            
            self.biases = abs(np.random.randn(1))
        
        else :
            
            if baises.shape[1] == 1:
                
                self.weights = weights
            
            else :
                
                raise UserWarning("Shapes do not match. Using random variables")
                self.weights = abs(np.random.randn(self.X.shape[1]))

        self.m_weights = 0
        self.m_biases = 0

        self.u_weights = 0
        self.u_biases = 0

        self.predic = []

    # for epochs in range(100):

    #     pred = np.sum((weights * X).T) + biases
        
    #     loss = np.sum(pred - y)
    #     losses.append(loss)

    #     u_weights = rho * l_weights + (1 - rho) * (-2 * loss)
    #     u_biases = rho * l_biases + (1 - rho) * (-2 * loss)

    #     m_weights = momentum * m_weights + (1 - momentum) * loss
    #     m_biases = momentum * m_biases + (1 - momentum) * loss
        
    #     if ema:
            
    #         m_weights = ema_momentum * m_weights + (1 - ema_momentum) * -2 * loss
    #         m_biases = ema_momentum * m_biases + (1 - ema_momentum) * -2 * loss

    #     if clip_norm != None:

    #         weights = np.clip(weights , weights , clip_norm)
    #         biases = np.clip(biases , biases , clip_norm)

    #     if clip_value != None:
            
    #         weights = np.clip(m_weigts , m_weights , clip_value)
    #         biases = np.clip(m_biases , m_biases , clip_value)
            
    #     weights -= (1/np.sqrt(u_weights + epsilon) * 1 / np.sqrt(m_weights + epsilon)) * learning_rate
    #     biases -= (1/np.sqrt(u_biases + epsilon) * 1 / np.sqrt(m_boases + epsilon)) * learning_rate

    # return weights , biases , losses


# METHOD 2

import numpy as np
from numpy import random

class simple_gradient_descent:

    def __init__(self , 
                 features , target , 
                 learning_rate = 0.01 , epochs = 100 , 
                 beta = 0.9 , epsilon = 1e-7):

        self.X = features
        self.Y = target
        self.lr = learning_rate
        self.epochs = epochs
        self.beta = beta

    def initialize(self , X):
    
        biases = random.random()
        weights = random.rand(self.X.shape[0])
        weights_sum = 0
        biases_sum = 0
    
        return biases , weights , weights_sum , biases_sum

    def predict(self , biases , weights , X):
        
        predicted_values = biases + np.dot(self.X.T , weights)

        return predicted_values
    
    def cost(self , predicted_values , Y):
        
        costing = self.Y - predicted_values

        return costing
    
    def update(self , predicted_values , biases , weights , epoch_number , weights_sum , biases_sum):

          weights_rec = []
          biases_rec = []

          if epoch_number == 0:

            params_weights = self.beta * weights + (1 - self.beta) * (weights**2)
            params_biases = self.beta * biases + (1 - self.beta) * (biases ** 2)

            weights = -(self.lr / np.sqrt(params_weights + self.epsilon)) * weights
            biases = -(self.lr / np.sqrt(params_biases + self.epsilon)) * biases

            weights_rec.append(weights)
            biases_rec.append(biases)

          else : 

            params_weights = self.beta * weights_rec[epoch_number - 1] + (1 - self.beta) * (weights_rec[epoch_number - 1]**2)
            params_biases = self.beta * biases_rec[epoch_number - 1] + (1 - self.beta) * (biases_rec[epoch_number - 1] ** 2)

            weights = -(self.lr / np.sqrt(params_weights + self.epsilon)) * weights_sum
            biases = -(self.lr / np.sqrt(params_biases + self.epsilon)) * biases_sum

            weight_sum += weights
            biases_sum += biases

            weights_rec.append(weights)
            biases_rec.append(biases)

    def forward(self):
        for epoch_number in range(self.epochs):
            self.predict(biases , weights , self.X)
            self.cost(predicted_values , self.y)
            self.update(predicted_values , biases , weights)

        return self.new_biases , self.new_weights

# METHOD 3
def MSE(predicted , actual):
    
    error = ((predicted - actual) ** 2).mean()

    return error
def MAE(predicted , actual):
    
    error = (abs(predicted - actual)).mean()

    return error
def CCE(predicted , actual):
    
    for _ in classes :
        
        for _ in list_of_values:
        
            error = 0
            error += predicted * np.log1p(predicted)

    return error

def RMSProp(X_train , Y_train , 
                     loss_func = "MSE" , epochs = 100 , 
                     lr = 0.01 , epsilon = 1e-7):
    
    def initialize(number_of_features):
    
        weights = np.random.randn(number_of_features) * 0.1
        biases = np.random.randn(1) * 0.1

        params = np.array([weights , biases])

    def predict(weights , biases , X_test):
        
        predicted_values = (weights * X_test) + biases

        return predicted_values

    def backward(Y_train , predicted , loss_func):
    
        if loss_func == "MSE" : 
            
            MAE(Y_train , predicted)
        
        elif loss_func == "MAE" : 
            
            MAE(Y_train , predicted)
        
        elif loss_func == "CCE" : 
            
            CCE(Y_train , predicted)


        return loss
    
    def forward(X_train , Y_train , epochs , lr):
    
        initialize(len(X_train.columns))
    
        for _ in range(epochs):
    
            predict(weights , biases , X_train)
            backward(Y_train , predicted_values)
    
            weights = weights - ((lr/(weights + epsilon)) * loss)
            biases = biases - ((lr/(biases + epsilon)) * loss)

    forward(X_train , Y_train , epochs , lr)

    new_params = np.array([weights , biases])

    return new_params
