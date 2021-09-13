marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("num %d pass" % number)
    else:
        print("num %d nopass" % number)
