#Keontae Trotman
#Class Name
class average:
    #This method returns the average increase of data as a % as long as it's a list
    def calcAverageRise(data):
        #If list and has more than 1 element
        if isinstance(data,list) and len(data)>1:
            #Final - Initial / initial * list length * 100 and rounded to the 2nd dec pt
            average = round(float(((data[-1]-data[0])/data[0])*(1/len(data))*100),2)
            #Returns the average
            return average
        #Returns False if conditions not met
        else: return False
    #This method uses the average rise for every 2 elements in list
    def getAnnualAverage(data):
        #Checks if list and has more than one element
        if isinstance(data,list) and len(data)>1:
            #Gets average rise for every 2 elements in list and makes them into a rounded %.
            rise = [str(average.calcAverageRise(data[i:i+2]))+"%" for i in range(0, len(data),2)]
            #returns rise
            return rise
        #Returns False if conditions not met
        else: return False
        #TODO:Two year averages Probably the same thing just with a 3 instead of 2
    def getBiennalAverage(data):
        #Checks if list and has more than one element
        if isinstance(data,list) and len(data)>1:
            #Gets average rise for every other 2 elements in list and makes them into a rounded %.
            rise = [str(average.calcAverageRise(data[i:i+3]))+"%" for i in range(0, len(data),4)]
            #returns rise
            return rise
        #Returns False if conditions not met
        else: return False