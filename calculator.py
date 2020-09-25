def calc():
    #calc() uses spaces between each operator and operand
    expr = input("Enter your mathematical expression like '2 + 3': ")
    [strnum1,operator,strnum2] = expr.split(" ") # 'split()' used to split string by spaces (" ") and the result of it is stored in strnum1,strnum2,operator
    # line 3 also represent 'unpacking'
    intnum1 = int(strnum1) #'int()' is used to convert string to integer
    intnum2 = int(strnum2)
    if operator=='+':
        print('Sum is : ',intnum1+intnum2)
    elif operator=='-':
        print('Difference is : ',intnum1-intnum2)
    elif operator=='*':
        print('Product is : ',intnum1*intnum2)
    elif operator=='/':
        print('Division is : ',intnum1/intnum2)

# we can also do this same kind of thing using 'eval()'
def calceval():
    expr = input("Enter your mathematical expression like '2+3': ")
    print('The result is: ',eval(expr))

calceval()
