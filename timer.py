import time


print("\nTimer v 1.20\nCopyright(c) 2018 Program Valley\n"
          "Type :start: for start count\n")



class t():
    days = 0
    hour = 0
    min = 0
    sec = -1
    add = 1
    holder = 0
    mholder = 0
    hholder = 0
    dholder = 0



def sekundy():
    time.sleep(1)
    t.sec = t.sec + 1
    t.holder = t.holder + 1
    print(str(t.days) +"d : " + str(t.hour) + "h : " + str(t.min) + "m : " + str(t.sec) + "s ")


def minuty():
    if t.holder == 60:
        t.min = t.min+1
        t.holder = 0
        t.sec = -1
        t.mholder = t.mholder + 1

def hodiny ():
    if t.mholder == 60:
        t.hour = t.hour + 1
        t.mholder = 0
        t.min = 0
        t.hholder =  t.hholder + 1


def dny ():
    if t.hholder == 24:
        t.days = t.days + 1
        t.hholder = 0
        t.hour = 0
        t.dholder = t.dholder + 1

statr = input(">>>")

while statr.lower() != "start":
    statr = input(">>>")

if statr.lower() == "start":
    while True:
        sekundy()
        minuty()
        hodiny()
        dny()

