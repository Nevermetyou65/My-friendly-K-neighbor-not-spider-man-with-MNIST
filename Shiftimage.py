from scipy.ndimage.interpolation import shift
import numpy as np

def shift_images(Xtrain, ytrain):

    bigger_X_train = [Xtrain]
    bigger_y_train = [ytrain]

    for i in range(len(Xtrain)):
        for adjustment in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            adjusted = shift(Xtrain[i].reshape((28, 28)), shift=adjustment)
            bigger_X_train.append(adjusted.reshape((1, 784)))
            bigger_y_train.append([ytrain[i]])
    
    new_X_train = np.concatenate(bigger_X_train)
    new_y_train = np.concatenate(bigger_y_train)

    return new_X_train, new_y_train
