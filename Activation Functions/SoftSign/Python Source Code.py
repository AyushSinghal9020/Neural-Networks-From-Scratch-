def softsign(array):
    
    output_array = np.empty(shape = array.shape)
    
    for i in array:
    
        output_array = np.hstack([output_array , i / 1 + abs(i)])
        output_array = np.delete(output_array , 0 , 0)

    return output_array
