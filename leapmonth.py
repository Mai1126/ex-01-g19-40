import sys

def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    if year <= 0:
        print("Error in year")
        print("command is 'python3 year month'")
        print("year is more 0")

        return
    if month < 0 or month > 12:
        print("Error in month")
        print("month is from 1 to 12")
        print("command is 'python3 year month'")
        
        return

    d = {}
    for m in [1, 3, 5, 7, 8, 10, 12]:
        d[m] = 31
    for m in [4, 5, 6, 9, 11]:
        d[m] = 30

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            d[2] = 28
        else:
            d[2] = 29
    else:
        d[2] = 28

    print("Month of ", month, "/", year, " has ", d[month], " days.", sep="")

if __name__ == '__main__':
    main()
