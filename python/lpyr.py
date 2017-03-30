yr = int(input("type the year you want to know: "))

def lpyr(yr, a = False):
    if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
        a = True
    return a

a = lpyr(yr)

def lpyr_rst():
    if a == True:
        print("leap year")
    else:
        print("common year")

lpyr_rst()
