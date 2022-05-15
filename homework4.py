i=0
i=i+1

for i in range(0,4):
    name  = input()
    score = int(input())

    if score in range(90, 101):
        grade = "A"
    elif score in range(80, 90):
        grade = "B"
    elif score in range(70, 80):
        grade = "C"
    elif score in range(60, 70):
        grade = "D"
    else:
        grade = "F"

    print("{}의 학점 : {}".format(name, grade))
