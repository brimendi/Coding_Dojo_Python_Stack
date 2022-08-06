#1 Print all integers from 0 - 150
for i in range(0, 151):
    print(i)

#2 print all the multiples of 5 from 5 to 1000
for i in range(5, 1005, 5):
    print(i)

#3 Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 10 == 0: 
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4 Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(0, 500001):
    if i % 2 == 1:
        sum += i
print(sum)        

#5 Print positive numbers starting at 2018, counting down by fours
for i in range(2018, 0, -4):
    if i % 2 == 0:
        print(i)

#6 Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
lowNum = 1
highNum = 30 
mult = 6
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
        