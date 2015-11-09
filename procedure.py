def hs(n):
    counter = 0
    while (n != 1):
        print (n)
        counter = counter + 1
        if (n % 2 == 0):
            n = n//2
        else:
            n = 3*n + 1
    if (n == 1):
        counter= counter + 1
        print ("1")
        print (counter)
        print ("None")
   
