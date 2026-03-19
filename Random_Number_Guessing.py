import random as r
number=int(input("Enter Number:"))
def random_no_game(num):
    points=0
    random_num=r.randint(1,100)
    print("Random NO:",random_num)
    while True:
        points += 5
        print("WON!!")
        if num!=random_num:
         break

    return points
bouns=random_no_game(number)
print(bouns)
