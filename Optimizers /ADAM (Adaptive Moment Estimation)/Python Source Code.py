def adam(columns , lr = 0.001 , beta = 0.9 , epochs = 100 , epsilon = 1e-7): 
    
    updated_gradient = np.empty(shape = (2,2))
    gradient_rec = []
    gradient_sum = np.zeros(shape = (len(columns) , 2))
    
    for epochs in range(epochs):
    
        if epochs == 0 or epochs == 1:
    
            gradient = gradient
    
        else :
    
            if np.all(np.array(gradient_rec[epochs-2]) > np.array(gradient_rec[epochs-1])):
    
                gradient = gradient_rec[epochs-2]
    
            else :
    
                gradient = gradient_rec[epochs-1]
    
        for parameters in range(2):
    
            upda_gradient = np.empty(shape = (len(columns),))
    
            for values in range(2):
    
                up_gradient = beta * gradient[parameters][values] ** 2 + (1 - beta) * gradient[parameters][values]
    
                upda_gradient = np.hstack([upda_gradient , up_gradient])
                upda_gradient = np.delete(upda_gradient , 0  , 0)
    
            updated_gradient = np.vstack([updated_gradient , upda_gradient])
            updated_gradient = np.delete(updated_gradient , 0 , 0)
    
        gradient_rec.append(updated_gradient)
    
        if epochs == 0 :
    
            params = params - np.dot((lr/ np.sqrt(gradient) + epsilon) ,np.array(gradient))
    
        else:
    
            params = params - np.dot((lr/ np.sqrt(gradient + epsilon)) ,np.array(gradient_rec[epochs - 1]))

    return params 