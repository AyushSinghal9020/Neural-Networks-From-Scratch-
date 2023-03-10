def rms_prop(columns , rho = 0.999 , lr = 0.01 , epochs = 100):
    
    params = np.random.ran(len(columns)) * 0.1
    
    gradient = [params[:len(columnes) - 2] * 2 , params[-1] * 2]
    
    step_size = np.random.rand(len(columnes)) * 0.1
    
    for i in range(len(gradient)):
    
        gradient[i] = (gradient[i] * rho) + ((gradeint[i] ** 2) * lr)
    
        for i in range(epochs) : 
    
            step_size = step_size / (1e-8 + np.array(gradient[i]))

    return step_size
