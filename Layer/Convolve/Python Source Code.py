import scipy
import numpy as np 

def convolve(image , kernel):
    
    if image.shape[2] == 3:
    
        test_image = np.reshape(image , newshape = (3 , image.shape[0] , image.shape[1]))
    
    else :
    
        test_image = image
    
    sample = np.empty(shape = test_image.shape)
    
    for channels in range(test_image.shape[0]):
    
        sample = np.vstack([sampel , 
                            scipy.signal.convolve2d(test_image[channels] , kernel , "same")
    
        sample = np.delete(sample , 0 , 0)
    
    sample = np.reshape(sample , newshape = (sample.shape[1] , sample.shape[2] , sample.shape[0]))

    return sample
