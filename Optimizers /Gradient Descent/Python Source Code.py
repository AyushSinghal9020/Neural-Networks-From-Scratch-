# METHOD 1

class SGD:
    
    def __init__(self , 
                 X , y , 
                 learning_rate = 0.01 , momentum = 0 , 
                 nestrov = False , weight_decay = 0 , 
                 clip_norm = None , clip_value = None , 
                 use_ema = False , ema_momentum = 0):
        
        self.X = X
        self.y = y
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.nestrov = nestrov
        self.weight_decay = weight_decay
        self.clip_norm = clip_norm
        self.clip_value = clip_value
        self.use_ema = use_ema
        self.ema_momentum = ema_momentum
    
    def build(self , weights = None , biases = None):
        
        if weights == None:
            
            self.weights = abs(np.random.randn(self.X.shape[0]))
        
        else :
            
            if weights.shape[0] == self.X.shape[1]:
                
                self.weights = weights
            
            else :
                
                self.weights = abs(np.random.randn(self.X.shape[1]))
                
                raise UserWarning("Values do not match with the `X` , intializing random Values")
                
        
        if biases == None:
            
            self.biases = abs(np.random.randn(1))
        
        else :
            
            if biases.shape[0] == 1:
                
                self.biases = biases
            
            else :
                
                self.biases = abs(np.random.randn(1))
                
                raise UserWarning("Values do not match with the `X` , intializing random Values")
    
        self.m_weights = [0]
        self.m_biases = [0]
    
        self.predic = []
        self.losses = []
    
        for epochs in range(100):
        
            pred = np.sum((weights * self.X).T) + biases
            
            loss = np.sum((pred - self.y) ** 2)
            self.losses.append(loss)
            
            if self.nestrov :

                self.m_weights[epochs + 1] = ((self.momentum * self.m_weights[epochs]) + ((1 - self.momentum) * (weights - self.momentum * self.m_weights[epochs])) * (-2 * loss)) 
                self.m_biases[epochs + 1] = ((self.momentum * self.m_biases[epochs]) + ((1 - self.momentum) * (weights - self.momentum * self.m_biases[epochs])) * (-2 * loss))

            else :

                self.m_weights[epochs + 1] = (self.momentum * self.m_weights[epochs] + (1 - self.momentum) * (-2 * loss))
                self.m_biases[epochs + 1] = (self.momentum * self.m_biases[epochs] + (1 - self.momentum) * (-2 * loss))
            
            if self.use_ema:
                
                self.m_weights[epochs + 1] = self.ema_momentum * self.momentum[epochs] + (1 - self.ema_momentum) * (self.m_weights[epochs + 1])
                self.m_biases[epochs + 1] = self.ema_momentum * self.momentum[epochs] + (1 - self.ema_momentum) * (self.m_biases[epochs + 1])
                
            if self.clip_norm != None:
                
                weights = np.clip(weights , weights , self.clip_norm)
                biases = np.clip(biases , biases , self.clip_norm)
            
            if self.clip_value != None:
                
                self.m_weights[epochs + 1] = np.clip(self.m_weights[epochs + 1] , self.m_weights[epochs + 1] , self.clip_value)
                self.m_biases[epochs + 1] = np.clip(self.m_biases[epochs + 1] , self.m_biases[epochs + 1] , self.clip_value)
            
            weights -= (self.m_weights[epochs + 1] + self.weight_decay * self.m_weights[epochs + 1]) * self.learning_rate
            biases -= (self.m_biases[epochs + 1] + self.weight_decay * self.m_biases[epochs + 1]) * self.learning_rate

        return weights , biases , losses

# METHOD 2

class gradient_descent:
    
    def __init__(self , X , y , lr = 1e-4 , epochs = 100) : 
    
        self.X = X
        self.y = y
        self.lr = lr
        self.epochs = epochs

    def init_params(self , X , y) : 
        
        np.random.seed(0)
        k = math.sqrt
    
        weights = np.random.rand(self.X.shape[0] , 
                                 self.y.shape[0]) * 2 * k - k
    
        biases = np.ones((1 , 
                          self.y.shape[0])) * 2 * k - k
    
        return [weights , biases]
        
    def forward(self , params) : 
        
        weights , biases = params
        prediction = self.X * weights , biases
    
        return prediction

    def backward(self , params , X , lr , grad) : 
    
        weight_grad = (self.X.T / self.X.shape[0]) * grad
        bias_grad = np.mean(grad , axis = 0)

        params[0] -= weight_grad * lr
        params[1] -= bias_grad * lr

        return params 
    
    mse = lambda actual , predictions : np.mean((predictions - actual) ** 2)
    
    mse_grad = lambda actual , predictions : (actual - predictions)
    
    def fit(self , epochs):
    
        params = self.init_params(self.X.shape[1] , y.shape[1])

        for i in range(self.epochs) : 
    
            predictions = self.forward(params , self.X)
            grad = self.mse_grad(self.y , predictions)

            params = self.backward(params , self.X , self.lr , grad)

# METHOD 3

class simple_gradient_descent:

    def __init__(self , 
                 features , targets , 
                 learning_rate = 0.01 , epochs = 100):

        self.X = features
        self.Y = target
        self.lr = learning_rate
        self.epochs = epochs

    def initialize(self , X):
    
        biases = random.random()
        weights = random.rand(self.X.shape[0])
    

    def predict(self , biases , weights , X):
        
        predicted_values = biases + np.dot(self.X.T , weights)

        return predicted_values
    
    def cost(self , predicted_values , Y):
        
        costing = self.Y - predicted_values

        return costing
    
    def update(self , predicted_values , biases , weights):

        db = (np.sum(predicted_values - self.Y) * 2) / self.X.shape[0]
        dw = (np.dot((predicted_values - self.Y) * 2, self.X)) / self.X.shape[0]
    
        biases = biases - self.lr * db

        weights = weights - self.lr * dw

        return biases , weights


    def forward(self):
        for _ in range(self.epochs):
            self.predict(biases , weights , self.X)
            self.cost(predicted_values , self.y)
            self.update(predicted_values , biases , weights)

        return self.new_biases , self.new_weights
    
# METHOD 4
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

def Gradient_Descent(X_train , Y_train , loss_func = "MSE" , epochs = 100 , lr = 0.01):
    
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
    
            weights = weights - (lr * loss)
            biases = biases - (lr * loss)

    forward(X_train , Y_train , epochs , lr)

    new_params = np.array([weights , biases])

    return new_params
     
