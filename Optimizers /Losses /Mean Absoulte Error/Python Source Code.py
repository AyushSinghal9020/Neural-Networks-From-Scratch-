def MAE(predicted , actual):
    
    error = (abs(predicted - actual)).mean()

    return error
