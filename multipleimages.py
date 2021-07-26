import matplotlib.pyplot as plt

def multiple_images(imcon ,nrow, ncol, figsize=(12, 8), dpi=100):
    fig, axes = plt.subplots(nrows=nrow, ncols=ncol, figsize=figsize, dpi=dpi)
    fig.subplots_adjust(hspace=0, wspace=0)

    canvas = axes.ravel()
    for i in range(len(canvas)):
        canvas[i].xaxis.set_major_locator(plt.NullLocator())
        canvas[i].yaxis.set_major_locator(plt.NullLocator())
        canvas[i].imshow(imcon[i].reshape((28, 28)), cmap="binary")