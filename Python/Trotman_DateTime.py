#Keontae Trotman
#This program adds month day and year in addition to the clock from timetype
from Trotman_Clock import TimeType
class Clock(TimeType):
    #Initalizes date at 1/1/1980
    def __init__(self,month=1,day=1,year=1980):
        #Calls the parent class
        super().__init__()
        #Sets the months
        self.__month=month
        self.__day=day
        self.__year=year
        #The last day of each month. Starts at -1 for indexing purposes
        self.__days=[-1,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #Makes feburary 29 if it's a leapyear. Otherwise does nothing.
    def leapyear(self,year):
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    self.__year=year
                    self.__days[2]=29
                    return True
                else:
                    self.__year=year
                    return False
            else:
                self.__days[2]=29
                self.__year=year
                return True
        else:
            self.__year=year
            return False
    #Sets the date and time and returns true if all conditions are met. Otherwise nothing and false.
    def setClock(self,hours,minutes,seconds,month,day,year):
        #Check if these return true
        #if leapyear febs last day is 29
        if month >=1 and month <=12 and day <= self.__days[month] and day>=1 and year>0 and super().set_time(hours,minutes,seconds) is True:
            self.leapyear(year)
            self.__year=year
            self.__day=day
            self.__month=month
            return True,year
        else:return False
    #Increases the day by 1
    def increaseDay(self):
        #Checks for leapyear
        self.leapyear(self.__year)
        self.__day+=1
        #If day is greater than day in month increase month. set day to 1
        if self.__day>self.__days[self.__month]:
            self.__day=1
            self.__month+=1
        #If month is greater than 12. Inc yr by 1 and set month to jan
        if self.__month>12:
            self.__month=1
            self.__year+=1
        self.leapyear(self.__year)
    #Decrease day by 1
    def decreaseDay(self):
        self.leapyear(self.__year)
        self.__day-=1
        #If day is negative go back 1 month and set day to last day of that month
        if self.__day<=0:
            self.__month-=1
        #If month is negative set to dec and dec year by 1
        if self.__month<1:
            self.__month=12
            self.__year-=1
        #Sets day to last day of the month if day is 0 or a negative
        if self.__day<=0:
            self.__day=self.__days[self.__month]
    #Increase second by one
    def increaseSecond(self):
        self.leapyear(self.__year)
        #Calls super method
        super().increase_second()
        #If time is all 0 after increase, increase the day
        if super().get_hours()==0 and super().get_minutes()==0 and super().get_seconds()==0:
            self.increaseDay()
    #Decrease second by 1
    def decreaseSecond(self):
        self.leapyear(self.__year)
        #Calls super method
        super().decrease_second()
        #If time goes below midnight decrease day by 1
        if super().get_hours()==23 and super().get_minutes()==59 and super().get_seconds()==59:
            self.decreaseDay()
    def __str__(self):
        #Return parent and child formats for date and time. 
        return "{mon:02}/{day:02}/{yr:04} ".format(mon=self.__month, day=self.__day, yr=self.__year) + super().__str__()
