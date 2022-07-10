def task(array):
    for i in range(len(array)):
        if array[i] == '0':
            return i
    return -1


print(task('1111111111100000000000'))

