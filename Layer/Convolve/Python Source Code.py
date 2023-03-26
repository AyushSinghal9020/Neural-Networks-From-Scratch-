class ConvolutionLayer:
    
    def __init__(self, kernel_num, kernel_size):
    
        self.kernel_num = kernel_num
        self.kernel_size = kernel_size        
        self.kernels = np.random.randn(kernel_num, kernel_size, kernel_size) / (kernel_size**2)

    def patches_generator(self, image):
    
        image_h, image_w = image.shape
    
        self.image = image
    
        for h in range(image_h-self.kernel_size+1):
    
            for w in range(image_w-self.kernel_size+1):
    
                patch = image[h:(h+self.kernel_size), w:(w+self.kernel_size)]
    
                yield patch, h, w
