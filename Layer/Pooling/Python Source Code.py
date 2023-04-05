def pool2d(image, kernel_size, stride, padding=0, pool_mode='max'):

    image = np.pad(image, padding, mode='constant')

    output_shape = ((image.shape[0] - kernel_size) // stride + 1,
                    (image.shape[1] - kernel_size) // stride + 1)
    
    shape_w = (output_shape[0], output_shape[1], kernel_size, kernel_size)
    strides_w = (stride*image.strides[0], stride*image.strides[1], image.strides[0], image.strides[1])
    
    A_w = as_strided(image, shape_w, strides_w)

    if pool_mode == 'max':

        return A_w.max(axis=(2, 3))

    elif pool_mode == 'avg':

        return A_w.mean(axis=(2, 3))
