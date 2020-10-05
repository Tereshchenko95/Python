my_list = [9, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
dig = int(input("Введите значение (123 - выход): "))
while dig != 123:

    for el in range(len(my_list)):
        if my_list[el] == dig:
            my_list.insert(el + 1, dig)
            break
        elif my_list[0] < dig:
            my_list.insert(0, dig)
            break
        elif my_list[-1] > dig:
            my_list.append(dig)
            break
        elif my_list[el] > dig and my_list[el + 1] < dig:
            my_list.insert(el + 1, dig)
            break
    print(f"текущий список - {my_list}")
    dig = int(input("Введите число: "))