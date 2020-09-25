def hellouser():
    name = input("what is your name? ") # 'input()' is used to take input from user
    print('Hello %s, nice to meet you!'%(name)) #inside 'print()' we use string formatting

# Below we write main function in python and how to call another function i.e. hellouser() inside main()
if __name__=='__main__':
    hellouser()
