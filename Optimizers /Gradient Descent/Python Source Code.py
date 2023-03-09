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
