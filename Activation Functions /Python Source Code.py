import numpy as np 

class activation_function:
    
    def __init(self , input , func = None): 
        
        self.func = func
        self.input = input

    def forward(self , self.input):
    
        if self.func == None : 
            
            return input
    
        elif self.func == "relu" : 
            
            return relu(self, self.input)
    
        elif self.func == "sigmoid" : 
            
            return sigmoid(self, self.input)
    
        elif self.func == "softmax" : 
            
            return softmax(self, self.input)
    
        elif self.func == "softplus" : 
            
            return softplus(self, self.input)
    
        elif self.func == "sogtsign" : 
            
            return softsign(self, self.input)
    
        elif self.func == "tanh" : 
            
            return tanh(self, self.input)
    
        elif self.func == "selu" : 
            
            return selu(self, self.input)
    
        elif self.func == "elu" : 
            
            return elu(self, self.input)
    
        elif self.func == "exponential" : 
            
            return exponential(self, self.input)
        else : 
            
            print("Please Enter a valid activation function")
            
            return None
    
    def relu_output(value) :
        
        output = max(0 , value) 
        
        return output
    
    def sigmoid_output(value) : 
    
        output = 1 / (1 + np.exp(- value))
    
        return output
    
    def softmax_output(value , addi) :
    
        output = np.exp(i)/ addi
    
        return output
    
    def softplus_output(value) :
    
        output = np.log1p(value)
    
        return output 
    
    def softsign_output(value) :
    
        output = value / (1 + abs(value))
    
        return output 
    
    def tanh_output(value) :
    
        output = ((m.e ** value) - (m.e ** (-value))) / ((m.e ** value) + (m.e ** (-value))) 
    
        return output
    
    def selu_output(value) : 
    
        if value > 0 :
    
            output = 1.0507 * (value)
    
        else : 
    
            output = 1.0507 * (1.6732 * (value - 1))
    
        return output
    
    def elu_output(value) : 
    
        if value > 0:
            
            output = value
        
        else :
        
            output = 1.6732 * (value - 1)

        return output

    def exponential_output(value) :
        
        output = np.exp(value)

        return output  

    def relu(self , array) : 

        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.relu_output(i)])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
    
    def sigmoid(self , array) : 

        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.sigmoid_output(i)])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
    
    def softmax(self , array) :

        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.softmax_output(i , )])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
     
    def softplus(self , array) : 
        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.softplus_output(i , )])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
     
    def softsign(self , array) : 
        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.softsign_output(i , )])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
     
    def tanh(self , array) : 
        
        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.tanh_output(i , )])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
     
    def selu(self , array) : 
        
        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.selu_output(i)])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
    
    def elu(self , array) : 
        
        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.elu_output(i)])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
    
    def exponential(self , array) : 
        
        output_array = np.empty(shape = array.shape)
        
        for i in array:
        
            output_array = np.hstack([output_array , self.exponential_output(i)])
            output_array = np.delete(output_array , 0 , 0)

        return output_array
    
