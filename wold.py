while 1 :
    num = int( input("Enter num\n>") )
    word = input("Enter text\n>")
    for i in word :
        I = ord(i)
        num1 = I // num
        num2 = I % num
        if num2 >= num//2 :
            num1 += 1
            num3 = num - num2
            str3 = "-"
        else :
            num3 = num2
            str3 = "+"
        str1 = num1 * "+"
        str2 = num3 * str3
        ret = f">{str1}[<{'+'*num}>-]<{str2}.>"
        print(ret)
