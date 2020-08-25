def romanToNumber(str: str):
    # init all romans
    romans = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }

    # init our num
    num = 0

    # convert input to list
    theList = list(str)

    # iterate over the list
    for index, i in enumerate(theList):
        print(i)
    
    # evaluate the numerals
        num = num + romans[i]
    
    # add the value to num
    if index > 0:
        

    # check whether the len of the input is > 0

    #

    # return num
    return num

print(romanToNumber("X"))