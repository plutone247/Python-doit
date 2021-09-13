coffee = 10
while True:
    money = int(input("give me the money"))
    if money == 300:
        print("ok i give you coffee")
        coffee = coffee -1
    elif money > 300:
        print("give %d in change, take coffee" % (money - 300))
        coffee = coffee -1
    else:
        print("not enough and i'm not give coffee")
        print("now coffee situation %d" % coffee)
    if coffee == 0:
        print ("more no coffee stop sell coffee")
        break
