class adagrad:
    def __init__(X , y , 
                 learning_rate = 0.01 , epsilon = 1e-7 , 
                 clip_norm = None , clip_value = None , 
                 ema = False , ema_momentum = 0):
    
        self.X = X
        self.y = y 
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.clip_norm = clip_norm
        self.clip_value = clip_value
        self.ema = ema
        self.ema_momentum = ema_momentum
    
    def build(self , weights = None , biases = None):
    
        if weights == None:
            
            self.weights = abs(np.random.randn(self.X.shape[1]))
        
        else :
            
            if weights.shape[0] == self.X.shape[1]:
                
                self.weights = weights
            
            else :
                
                raise UserWarning("Shapes do not match , initalizing random weights")
                    
                self.weights = abs(np.random.randn(self.X.shape[1]))
        
        if biases == None:
            
            self.biases = abs(np.random.randn(1))
        
        else :
            
            if biases.shape[0] == 1:
                
                self.biases = biases
            
            else :
                
                raise UserWarning("Shapes do not match , initalizing random biases")
                    
                self.biases = abs(np.random.randn(1))

        self.losses = []
        self.grad = np.zeros(2)

    def compute_gradient(self , weights , biases):

        pred = np.sum((weights * X).T) + biases
        
        loss = np.sum((pred - y) ** 2)
        
        losses.append(loss)
        
        grad[1] = -2 * loss

        yield grad

#     if ema: 

#         grad = ema_momentum * grad + (1 - ema_momentum) * grad

#     if clip_norm != None:
        
#         weights = np.clip(weights , weights , clip_norm)
#         biases = np.clip(biases , biases , clip_norm)

#     if clip_value != None:

#         grad = np.clip(grad , grad , clip_value)
    
#     weights -= np.sqrt(-1 / (grad[1] + epsilon)) * grad[0] * learning_rate 
#     biases -= np.sqrt(-1 / (grad[1] + epsilon)) * grad[0] * learning_rate

#     grad[1] = grad[0]

# return weights , biases , losses
