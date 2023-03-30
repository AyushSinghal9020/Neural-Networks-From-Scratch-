def softplus(array):
    
    output_array = np.empty(shape = array.shape)
    
    for i in array:
    
        output_array = np.hstack([output_array , np.log1p(np.exp(i))])
        output_array = np.delete(output_array , 0 , 0)

    return output_array
