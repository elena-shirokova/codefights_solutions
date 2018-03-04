def rotateImage(a):

    rotate_img = [[a[i][j] for i in reversed(range(len(a)))] for j in range(len(a))]
    return rotate_img