# from turtle import *
# import colorsys

# speed(0)
# bgcolor("black")
# h = 0

# for i in range(16):
#     for j in range(18):
#         c = colorsys.hsv_to_rgb(h, 1, 1)
#         color(c)
#         h += 0.001
#         rt(90)
#         circle(150 - j * 6, 90)
#         lt(90)
#         circle(150 - j * 6, 90)
#         rt(180)
#     circle(40, 24)
# done()

'''import math
from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(0)
bgcolor("black")
for i in range(10000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()'''




# DSA QUESTIONS PRACTICE.
'''list = [11, 7, 12, 8, 3, 2, 1, 5, 4, 6, 9, 10]

      # list.sort()
      # print(f"Sorted in ascending order: {list}")
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)

      # list.sort(reverse=True)
      # print(f"Sorted in decending order: {list}")
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)'''

