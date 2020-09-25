def charcount():
    str = input("what is the input string? ")
    #we ask user to provide input, if user not provide anything
    while len(str)==0: #'len()' is used to find length of string
        str = input("please provide some input! ")
    print('%s has %s characters.'%(str,len(str)))

# it is not mandatory to write main function always. we directly call 'charcount()' without main
charcount()
