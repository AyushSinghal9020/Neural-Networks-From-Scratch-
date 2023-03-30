def selu(array):

    def selu_output(value):
        a = 1.0507
        b = 1.6732

        if value > 0 : 
            return a * value
        else : 
            return (a * (b * (value - 1)))

    output_array = np.empty(shape = array.shape)
    
    for i in array:
        output_array = np.hstack([new_array , selu_output(i)])
        output_array = np.delete(output_array , 0 , 0)

    return output_array
