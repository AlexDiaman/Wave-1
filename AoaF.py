length = int(input("Please input length of field in feet: "))
width = int(input("Please input width of field in feet: "))

area = length * width
areaacre = area // 43560

print(areaacre)