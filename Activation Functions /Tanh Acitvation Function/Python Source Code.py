def tanh(array):
    output_array = np.empty(shape = array.shape)
    
    for i in array:
        output_array = np.hstack([new_array , ((m.e ** i) - (m.e ** (-i))) / ((m.e ** i) + (m.e ** (-i)))])
        output_array = np.delete(output_array , 0 , 0)

    return output_array
