file = open("input.txt", "r")
list = None

for line in  file.readlines():
        list = line.rstrip().split(',')

sum = 0
for str in list:
        value = 0
        for char in str:
                value = (value + ord(char)) * 17 % 256
        sum +=value
print(sum)





###PART 2###


