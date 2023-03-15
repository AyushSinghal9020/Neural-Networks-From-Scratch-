def rms_prop(columns , rho = 0.999 , lr = 0.01 , epochs = 100 , epsilon = 1e-7):
    
    params = np.random.ran(len(columns)) * 0.1
    
    gradient = [params[:len(columns) - 2] * 2 , params[-1] * 2]
    
    step_size = np.random.rand(len(columns)) * 0.1

    gradient_record = []
    k_record = []

    for i in range(len(gradient)):
        
        gradient[i] = (gradient[i]) + ((gradient[i] ** 2) * lr) 
        
        k = r*k + (1- r)*(gradient[i]**2)

        lr = lr/np.sqrt(k + epsilon)

        for i in range(epochs) : 
    
            step_size = step_size * lr

    return step_size
