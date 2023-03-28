def MSE(predicted , actual):
    
    error = ((predicted - actual) ** 2).mean()

    return error
