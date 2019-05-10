import sys

def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    if year <= 0:
        print("Error in year")
        print("command is 'python3 year month'")
        print("year is more 0")

        return
    if month < 0 || month > 12:
        print("Error in month")
        print("month is from 1 to 12")
        print("command is 'python3 year month'")
        
        return
    print("Month of ", month, "/", year, " has ", 31, " days.", sep="")

if __name__ == '__main__':
    main()
