my_list = ("Zima", "Vesna", "Leto", "Osen")
my_dict = {'1': 'zima', '2': 'vesna', '3': 'leto', '4': 'osen'}
a = int(input("Введите месяц числом: "))
if a == 1 or a == 2 or a == 12:
    print('Zima')
    print(my_list[0])
    print(my_dict['1'])
if a == 3 or a == 4 or a == 5:
    print('Vesna')
    print(my_list[1])
    print(my_dict['2'])
if a == 6 or a == 7 or a == 8:
    print('Leto')
    print(my_list[2])
    print(my_dict['3'])
if a == 9 or a == 10 or a == 11:
    print('Osen')
    print(my_list[3])
    print(my_dict['4'])