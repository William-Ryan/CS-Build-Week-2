def reduceToZero(num):
    # copy num
    copyNum = num
    iterNum = 0
    # loop while num > 0
    while copyNum > 0:
        # make variable for checking is even
        isEven = copyNum % 2 == 0
        # if isEven is true, divide by 2
        if (isEven):
            copyNum = copyNum / 2
        # else subtract by 1
        else:
            copyNum -= 1
        # increment the iterations for tracking
        iterNum += 1
    # return the amount of times it passed through while loop
    return iterNum

print(reduceToZero(14))
