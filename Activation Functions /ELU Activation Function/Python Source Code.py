def elu(array):

    def elu_output(value):

        b = 1.6732

        if value > 0 : 
            return value
        else : 
            return (b * (value - 1))

    output_array = np.empty(shape = array.shape)
    
    for i in array:
        output_array = np.hstack([new_array , elu_output(i)])
        output_array = np.delete(output_array , 0 , 0)

    return output_array
