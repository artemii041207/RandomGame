import random

rnd = random.randint(1, 3)
usr = int(input("Угадай число (от 1 до 3): ")) 

if usr == rnd:
    print("Ты выиграл!")
elif usr < 1 or usr > 3:
    print("Что-то пошло не так...")
    again = str(input("Попытаться снова? (да/нет): "))
    if again == "да":
        import random
        rnd = random.randint(1, 3)
        usr = int(input("Угадай число (от 1 до 3): ")) 

        if usr == rnd:
            print("Ты выиграл!")
        elif usr < 1 or usr > 3:
            print("Что-то пошло не так...")
        else:
            print("Ты проиграл!")
        input()
    elif again == "нет":
        print("Гандон")

else:
    print("Ты проиграл!")
    
input()