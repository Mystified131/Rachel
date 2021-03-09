
#This function retrieves a product to use as a multiplier with with original number

def return_product(num1):

    num = str(num1)

    import datetime
    import time

    x = 9

    if len(num) > 9:
        x = len(num)

    dv = "."

    for x1 in range(x - 1):
        dv += "0"

    dv += "1"

    div = float(dv)

    outnum = ""

    for ctr in range(x):

        right_now = datetime.datetime.now().isoformat()    

        substr = ""

        for i in right_now:
            if i.isnumeric():
                substr += str(i)

        dg = substr[-1:]

        outnum += dg

        time.sleep(.0000001)

    out = float(outnum)  

    aval = out * div

    bval = round(aval, x)

    return(bval)

#This function uses the second argument to transform the first via multiplication

def transpose(num, ranm):

    prod = int(round(num * ranm))

    return(prod)

#This function sets up and calls the other two, from a simple original value. It returns a "randomized" integer.

def random_number2(val, val2):

    val3 = float(val2 - 1) - float(val)

    val4 = str(val3)

    res1 = return_product(val4)

    res2 = transpose(val3, res1)

    res2b = int(float(val) + res2)

    return res2b

#res = random_number2(50, 100)

#print(res)

##THE GHOST OF THE SHADOW##




