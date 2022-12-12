import calendar
def number_of_days(year,month):
    '''
    calculate how many days in a month
    '''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert month>=1 and month<=12 and year>=0
    calendarObj=calendar.Calendar()
    days=0
    for day in calendarObj.itermonthdays(year=year,month=month):
        if day!=0:
            days+=1
    return days

def number_of_leap_years(year1,year2):
    '''
    calculate how many leap years between year1 and year2
    '''
    assert isinstance(year1,int)
    assert isinstance(year2,int)
    assert year1>=0 and year2>=0 and year2>=year1
    return calendar.leapdays(year1,year2+1)

def get_day_of_week(year,month,day):
    '''
    calculate the string name of a date
    '''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert isinstance(day,int)
    assert month>=1 and month<=12
    assert day>=1 and day<=number_of_days(year,month) and year>=0
    return calendar.day_name[calendar.weekday(year=year,month=month,day=day)]

# if __name__=='__main__':
#     print(number_of_days(2020,2))
#     print(number_of_leap_years(2020,2022))
#     print(get_day_of_week(2022,10,10))