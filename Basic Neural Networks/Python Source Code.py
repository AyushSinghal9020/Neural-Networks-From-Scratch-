class Dense:

    def __init__(self , inputs , neurons):
        
        self.weights = 0.01 * np.random.randn(inputs , neurons)
        self.biases = np.zeros((1 , neurons))
    
    def forward(self , inputs):
    
        self.output = np.dot(inputs , self.weights) + self.biases
