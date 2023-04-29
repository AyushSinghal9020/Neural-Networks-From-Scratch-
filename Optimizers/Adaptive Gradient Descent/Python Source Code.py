def adagrad(X , y , learning_rate = 0.01):
    
    weights = abs(np.random.randn(X.shape[1]))
    biases = abs(np.random.randn(1))

    losses = []
    grad = [0] * 2

    for _ in range(100):

        pred = np.sum((weights * X).T) + biases
        
        loss = np.sum((pred - y) ** 2)
        losses.append(loss)
        
        grad[1] = -2 * loss
        
        weights -= np.sqrt(-1 / (grad[1] + 1e-7)) * grad[0] * learning_rate 
        biases -= np.sqrt(-1 / (grad[1] + 1e-7)) * grad[0] * learning_rate

        grad[1] = grad[0]

    return weights , biases , losses
