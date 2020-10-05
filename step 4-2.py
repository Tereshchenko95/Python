my_list = input("введите строку: ")
my_word = []
num = 1
for el in range(my_list.count(' ') + 1):
    my_word = my_list.split()
    print(len(str(my_word[el])))
    if len(str(my_word[el])) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1