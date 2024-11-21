current_name = input('what is your name :')

my_file = open('names.txt', 'a')
my_file.write(current_name + '\n')
my_file.close()

my_file = open("names.txt", 'r')
for name in my_file.readlines():
    print(f"hello {name}")
