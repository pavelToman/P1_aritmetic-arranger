def arithmetic_arranger(problems, x=False):
    row_1 = ""
    row_2 = ""
    row_3 = ""
    row_4 = ""
    count = len(problems) -1
    if len(problems)>5:
        print("Error: Too many problems.")
        return("Error: Too many problems.")
    else:
        for i in problems:
            a = i.split()
            if len(a[0]) > len(a[2]):
                leng = len(a[0])
            else:
                leng = len(a[2])
            if leng > 4:
                print("Error: Numbers cannot be more than four digits.")
                return("Error: Numbers cannot be more than four digits.")
                break
            if (a[1] != "+") and (a[1] != "-"):
                print("Error: Operator must be \'+\' or \'-\'.")
                return("Error: Operator must be \'+\' or \'-\'.")
                break
            try:
                a1 = int(a[0])
                a2 = int(a[2])
            except:
                print("Error: Numbers must only contain digits.")
                break
            
            m1 = leng - len(a[0]) +2
            row_1 += " "*m1
            row_1 += a[0]
            if count != 0:
                row_1 += " "*4

            row_2 += a[1]+" "
            m2 = leng - len(a[2])
            row_2 += " "*m2
            row_2 += a[2]
            if count != 0:
                row_2 += " "*4

            row_3 += "-"*(leng+2)
            if count != 0:
                row_3 += " "*4
            
            if a[1] == "+":
                r = str(a1 + a2)
            elif a[1] == "-":
                r = str(a1 - a2)
            rl = len(r)
            
            row_4 += " "*((leng+2)-rl)
            row_4 += r
            if count != 0:
                row_4 += " "*4
                       
            count -= 1
        if x == True:    
            arranged_problems = row_1+"\n"+row_2+"\n"+row_3+"\n"+row_4
        else:
            arranged_problems = row_1+"\n"+row_2+"\n"+row_3
        print(arranged_problems)
        return arranged_problems

  
arithmetic_arranger(["10 + 234", "5467 - 67"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
arithmetic_arranger(["3801 - 2", "123 + 49"])

#error too many
#arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87'])
#error + a -
#arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])
#error moc čísel
#arithmetic_arranger(["10 + 2345678"])
#error digits
#arithmetic_arranger(["10e + k78"])