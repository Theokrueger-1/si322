#Theo Krueger

#Create an empty list to store numnbers

numbers = []

#Read numbers from text file and append to the list
with open("number.txt", "r") as my_file:
    for line in my_file:
        clean_line = line.strip()
        number = int(clean_line)
        numbers.append(number)


#Sort numbers
numbers.sort()


#Print to STDOUT on different lines. 
for number in scores:
    print(numbers)