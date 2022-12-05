from PIL import Image
import matplotlib.pyplot as plt
import numpy as np



def BringInImages(Image_path, Key_path, shrink = 1, show = True):
    '''This function will bring in the images, resize them, and optionaly display them
    Input: 
        Image_path: path to image
        Key_path: path to black and white key image
        shrink: 0-1 ratio of pixels to use
        show: boolean to change if the brought in images are displayed
    '''
    #bring in images
    im = Image.open(Image_path)
    key = Image.open(Key_path)

    
    #resize them
    size_arr_org = np.array(im)
    a1 = len(size_arr_org)*len(size_arr_org[1])
    size = (int(len(size_arr_org[0])*shrink), int(len(size_arr_org)*shrink))
    im = im.resize(size)
    key = key.resize(size)
    
    size_arr = np.array(im)
    a2 = len(size_arr)*len(size_arr[1])
    
    if show:
        print("New Pixels: {} ({} i x {} j)".format(a2, len(size_arr), len(size_arr[1])))
        print("Original Pixels: {} ({} i x {} j)".format(a1, len(size_arr_org), len(size_arr_org[1])))
        print("Percent of pixels used {:.3f} %".format(100*a2/a1))
        
        
        #Display them
        f = plt.figure()
        f.set_figwidth(20)
        f.set_figheight(20)
        
        plt.subplot(1,2,1)
        plt.title("Input Image")
        plt.imshow(im)

        plt.subplot(1,2,2)
        plt.title("Image Key")
        plt.imshow(key)
    
    return im, key


def Collect_key_matrix(image, show = False):
    '''Takes in a black and white key image and changes it to be 0's and  1's
    Input:
        image: Black and white image object
    Results:
        1D array of 1's and 0's based on the image
        a matrix of 1's and 0's the same shape as the key
        2D array containing the indices in tuples for each marker pixel
    '''
    key1_arr = np.array(image)
    key = np.zeros((len(key1_arr), len(key1_arr[0])))
    key_labeled_arr = []
    key_indecies = []

    #convert to 1's and zeros
    for i in range(0,len(key1_arr)):
        for j in range(0,len(key1_arr[0])):
            pixel = np.sum(key1_arr[i, j])
            if pixel > 650:
                key[i,j] = 0
                key_labeled_arr.append(0)
            else: 
                key[i,j] = 1
                key_labeled_arr.append(1)
                pixel_index = (j, i)
                key_indecies.append(pixel_index)

    if show:
        f = plt.figure()
        f.set_figwidth(20)
        f.set_figheight(20)

        plt.subplot(1,2,1)
        plt.title("RGB Key")
        plt.imshow(image)
        plt.subplot(1,2,2)
        plt.title("1 & 0 Key")
        plt.imshow(key)
                
    return key_labeled_arr, key , key_indecies



def Reconstruct(labeled_array, row_orig, column_org):
    '''Takes in a 1D array and reconstructs it to be an image
    Inputs:
        1D array to convert to the image
        number of rows in the orignal photo
        number of columns in the original photo
    '''
    image = []
    
    for i in range(0, row_orig):
        #create new row
        row = []
        for j in range(i*column_org, i*column_org+column_org):
            row.append(labeled_array[j])
        image.append(row)

    return image
