# 구구단 출력하기

def gugudan():
    dan = int(input("몇단을 입력할까요? "))

    print(dan, "단")
    for i in range(1, 10):
        print(dan, "x", i, "=", dan * i)


gugudan()
