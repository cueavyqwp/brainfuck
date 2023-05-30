while 1 :
    try :
        word = input(">")
        for i in word :
            I = ord(i)
            num1 = I // 10
            num2 = I % 10
            if num2 >= 5 :
                num1 += 1
                num3 = 10 - num2
                str3 = "-"
            else :
                num3 = num2
                str3 = "+"
            str1 = num1 * "+"
            str2 = num3 * str3
            ret = f">{str1}[<++++++++++>-]<{str2}.>"
            print(ret)
    except :
        print()