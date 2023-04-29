def adagrad(X , y):
    
    weights = abs(np.random.randn(X.shape[1]))
    biases = abs(np.random.randn(1))

    losses = []

    for _ in range(100):

        pred = np.sum((weights * X).T) + biases
        
        loss = np.sum((pred - y) ** 2)
        losses.append(loss)
        
        weights -= -2 * loss * 0.01
        biases -= -2 * loss * 0.01

    return weights , biases , losses
