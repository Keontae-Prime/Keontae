#Keontae Trotman
#This program mimics a clock.
class TimeType:
    #Initializes hours minutes and seconds as private int attributes of 0
    def __init__(self):
        hours=0
        minutes=0
        seconds=0
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    #This method returns the number of hours in 12 hour format.
    def get_hours(self):
        return self.__hours
    #This method returns the number of minutes
    def get_minutes(self):
        return self.__minutes
    #This method returns the number of seconds
    def get_seconds(self):
        return self.__seconds
        
    #This method returns true if hours is btwn 23 and 0 or is 23 or 0
    def set_hours(self,hours):
        if hours <=23 and hours >=0:
            self.__hours=hours
            return True
        #Returns false otherwise
        else:return False
    #This method returns true if minutes is btwn 59 and 0 or is 59 or 0
    def set_minutes(self,minutes):
        if minutes <=59 and minutes >=0:
            self.__minutes=minutes
            return True
        #Returns false otherwise
        else:return False
    #This method returns true if seconds is btwn 59 and 0 or is 59 or 0
    def set_seconds(self,seconds):
        if seconds <=59 and seconds >=0:
            self.__seconds=seconds
            return True
        #Returns false otherwise
        else:return False
    #This method sets the hours minutes and seconds at the same time if all conditions are met and returns true.
    def set_time(self,hours,minutes,seconds):
        #conditions
        if hours <=23 and hours >=0 and minutes <=59 and minutes >=0 and seconds <=59 and seconds >=0:
            #Changes the private attributes
            self.__hours=hours
            self.__minutes=minutes
            self.__seconds=seconds
            return True
        #Otherwise returns false
        else:return False
    #This method increases the second by 1 and adjusts the time as it should.
    def increase_second(self):
        #Increase seconds by 1
        self.__seconds+=1
        #If it's @ 59 reset the secs and add 1 to mins
        if self.__seconds > 59:
            self.__minutes=self.__minutes+1
            self.__seconds=0
        #Otherwise add 1 to secs
        #If minutes is greater than 59 adjust the hour by 1 and reset minutes to 0
        if self.__minutes > 59:
            self.__minutes=0
            self.__hours=self.__hours+1
        #If hours is greater than 23 reset to 0.
        if self.__hours>23:
            self.__hours=0
    #This method decreases the second by 1 and adjusts the time as it should.
    def decrease_second(self):
        self.__seconds-=1
        #If seconds is 0 make it 59 and decrease minute by 1
        if self.__seconds<0:
            self.__seconds=59
            self.__minutes-=1
        #If minute is 0 make it 59 and decrease hour by 1
        if self.__minutes<0:
            self.__minutes=59
            self.__hours-=1
        #If hours is less than 0 reset to 23
        if self.__hours<0:
            self.__hours=23

        #In case hours becomes a negative add 12.
        
    #This method returns the hours minutes and seconds in 12 hour format
    #Substitute x is used so the private attributes aren't affected in case they are used again.
    def __str__(self):
        if self.__hours>12:
            x=self.__hours-12
            ap='PM'
            return "{hr:>2}:{min:02}:{sec:02} {ap}".format(hr=x, min=self.__minutes, sec=self.__seconds, ap=ap)
        elif self.__hours<12 and self.__hours != 0:
            x=self.__hours
            ap='AM'
            return "{hr:>2}:{min:02}:{sec:02} {ap}".format(hr=x, min=self.__minutes, sec=self.__seconds, ap=ap)
        elif self.__hours==12:
            x=self.__hours
            ap='PM'
            return "{hr:>2}:{min:02}:{sec:02} {ap}".format(hr=x, min=self.__minutes, sec=self.__seconds, ap=ap)
        else:
             x=self.__hours+12
             ap='AM'
             return "{hr:>2}:{min:02}:{sec:02} {ap}".format(hr=x, min=self.__minutes, sec=self.__seconds, ap=ap)
        #Shoe comb Phone#