print("Enter number:")
number = int(input())
months = [(31, "January"), (28, "February"), (31, "March"), (30, "April"), (31, "May"), (30, "June"),
(31, "July"), (31, "August"), (30, "September"), (31, "October"), (30, "November"), (31, "December")]
while(number > 12 or number < 1):
    print("Enter number:")
    number = int(input())
for index, month in enumerate(months):
    if(index == number - 1):
        print(month)
''' Enter number:
1
(31, 'January')'''
