# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    condition1 = year % 400
    condition2 = year % 4
    condition3 = year % 100
    if condition2 !=0:
        return False
    else:
        if condition3 != 0:
            return True
        else:
            if condition1 != 0:
                return False
            return True
        return False
    return True
            

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
##count days of year before birthday.
    if isLeapYear(y1) is True:
        daysOfMonths[1] = 29
        month = 0
        pre_days = 0
        while month < m1:
            days = daysOfMonths[month]
            pre_days = pre_days + days
            month = month + 1
        pre_days = pre_days + d1
    else:
        daysOfMonths[1] = 28
        month = 0
        pre_days = 0
        while month < m1:
            days = daysOfMonths[month]
            pre_days = pre_days + days
            month = month + 1
        pre_days = pre_days + d1
        
#count days from 1/1 to day of current year
    if isLeapYear(y2) is True:
        daysOfMonths[1] = 29
        month = 0
        current_days = 0
        while month < m2:
            days = daysOfMonths[month]
            current_days = current_days + days
            month = month + 1
        current_days = current_days + d2
    else:
        daysOfMonths[1] = 28
        month = 0
        current_days = 0
        while month < m2:
            days = daysOfMonths[month]
            current_days = current_days + days
            month = month + 1
        current_days = current_days + d2

##count days of whole years        
    total_days = 0
    LeapY_total_days = 0
    commonY_total_days = 0
    while y2-y1 >=1:
        if isLeapYear(y1) is True:
            daysOfMonths[1] = 29
            for day in daysOfMonths:
                LeapY_total_days = LeapY_total_days + day
            total_days = total_days + LeapY_total_days
            LeapY_total_days = 0
            y1 = y1 + 1
        else:
            daysOfMonths[1] = 28
            for day in daysOfMonths:
                commonY_total_days = commonY_total_days + day
            total_days = total_days + commonY_total_days
            commonY_total_days = 0
            y1 = y1 + 1

### return result
    days = total_days - pre_days + current_days
    return days

#print isLeapYear(2000)
print daysBetweenDates(2012, 6, 29, 2013, 6, 31)
