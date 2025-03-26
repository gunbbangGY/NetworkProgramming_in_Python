outStr = ''
count, i = 0,0

inStr = input("Type string : ")
count = lent(inStr)

for i in range(0, count) :
    outStr += inStr[count - (i+1)]

rpint("Reserved String : %s" %outStr)
