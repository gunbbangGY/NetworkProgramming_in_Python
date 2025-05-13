import random

for i in range(20) :
    f = open("ex-" + str(i+1) + ".txt", "w")
    f.write("다음의 문제를 풀어서 제출하세요\n")
    f.write("이름 :      점수 :           \n\n")

    for k in range(10) :
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        op = random.choice("+-*/")
        f.write("{0} {1} {2} = \n".format(x, op, y))

    f.close()
            
