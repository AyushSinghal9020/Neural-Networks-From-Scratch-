def adagrad(X , y , learning_rate = 0.01 , epsilon = 1e-7 , clip_norm = None , clip_value = None):
    
    weights = abs(np.random.randn(X.shape[1]))
    biases = abs(np.random.randn(1))

    losses = []
    grad = np.zeros(2)

    for _ in range(100):

        pred = np.sum((weights * X).T) + biases
        
        loss = np.sum((pred - y) ** 2)
        losses.append(loss)
        
        grad[1] = -2 * loss

        if clip_norm != None:
            
            weights = np.clip(weights , weights , clip_norm)
            biases = np.clip(biases , biases , clip_norm)

        if clip_value != None:

            grad = np.clip(grad , grad , clip_value)
        
        weights -= np.sqrt(-1 / (grad[1] + epsilon)) * grad[0] * learning_rate 
        biases -= np.sqrt(-1 / (grad[1] + epsilon)) * grad[0] * learning_rate

        grad[1] = grad[0]

    return weights , biases , losses
