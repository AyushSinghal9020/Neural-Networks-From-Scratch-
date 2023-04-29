def adagrad(X , y):
    
    weights = abs(np.random.randn(X.shape[1]))
    biases = abs(np.random.randn(1))

    losses = []
    grad = [0] * 2 # Intialize of only 2 elements

    for _ in range(100):

        pred = np.sum((weights * X).T) + biases
        
        loss = np.sum((pred - y) ** 2)
        losses.append(loss)
        
        grad[1] = -2 * loss # calculate the gradient for 1 epoch
        
        weights -= np.sqrt(-1 / (grad[1] + 1e-7)) * grad[0] * 0.01#|Update the weights using gradient 
        biases -= np.sqrt(-1 / (grad[1] + 1e-7)) * grad[0] * 0.01#-|

        grad[1] = grad[0] # Replace the 1 gradient with 0 and move on 

    return weights , biases , losses
