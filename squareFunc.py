def square(s) :
    area = s * s
    circumference = 4 * s
    return (area, circumference)

s = float(input('input : '))
a, c = square(s)
print('area : ', a, 'circumference : ', c)
