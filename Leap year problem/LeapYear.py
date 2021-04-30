def is_leap(year):
    leap = False
    if (year % 400 == 0):
        return True
        if (year % 100 == 0):
            return True
            if (year % 400 == 0):
                return False
    # Write your logic here

    return leap


year = int(input())