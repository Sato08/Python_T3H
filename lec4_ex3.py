def day_Month(number):
    months = [(31, "January"), (28, "February"), (31, "March"), 
              (30, "April"), (31, "May"), (30, "June"),
              (31, "July"), (31, "August"), (30, "September"), 
              (31, "October"), (30, "November"), (31, "December")]
    for index, month in enumerate(months):
        if(index == number - 1):
            return month
day_Month(1)