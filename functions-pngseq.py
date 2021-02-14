def reduce_np_numbers(nparray, y):
    # reduces number of items in an np array to y
    # still doesn't always work for larger values of y
    # comes out w/ array 1 element too large, fix this.
    if nparray.size <= y:
        return nparray
    else:
        x = int(nparray.size / y)
        reducednp = nparray[0:-1:x]

        return reducednp


def list_to_np(list):
    # create numpy array w/ output values
    out5 = np.asarray(list)
    return out5


def add_to_array_y(nparray, x):
    # add or subtract values from np array.
    p = nparray + x
    return p


def mult_array(nparray, x):
    # multiply each array value by x
    if x == 0:
        x = 1
    p = nparray * x
    return p


def clip(nparray, min=0, max=1023):
    # set min and max values for everything in array
    x = nparray.clip(min, max)
    return x


def scale(nparray, scalevalue):
    # scales all values in array to y average. scalevalue is a percent. Output rounded to int.
    scalevaluex = scalevalue * .01
    print(scalevaluex)
    q = np.average(nparray)
    print(q)
    condlist = [nparray < q, nparray > q]
    up = 1 + scalevaluex
    down = 1 - scalevaluex
    choicelist = [nparray * up, nparray * down]
    a1 = np.select(condlist, choicelist, q)
    a2 = np.rint(a1)
    return a2