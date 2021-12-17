#Keontae Trotman
#Class name
class prediction:
    #This method returns the first year
    #This method returns the average increase of data as a % as long as it's a list
    def getAverageRise(data):
        if isinstance(data,list) and len(data)>1:
            #Final - Initial / initial * list length * 100 and rounded to the 2nd dec pt
            average = round(float(((data[-1]-data[0])/data[0])*(1/len(data))*100),2)
            # Returns value as a string with a percentage attached
            return str(average)+"%"
        else: return False

    #This method calculates the annual rise of 2 elements in a list
    def calcAnnualRise(data):
        if isinstance(data,list) and len(data)>1:
            #v2/v1-1
            annualRise = round(float((data[-1]/data[0]))-1,2)
            #Returns yearly rise list
            return annualRise
        else: return False
    #This method gets the annual rise for every 2 elements in a list
    def getAnnualRise(data):
        if isinstance(data,list) and len(data)>1:
            # Calcs annual rise for every 2 elements in list and makes them into a rounded %.
            res = [str(prediction.calcAnnualRise(data[i:i+2]))+"%" for i in range(0, len(data))]
            # Removes last value which is none
            res.pop(-1)
            #returns rise
            return res
        else: return False

    #This method returns the predicted tuition rise for 1 year
    def predAnnualRise(data):
        #If it's a list add get the difference of the last 2 years
        if isinstance(data,list):
            #Takes the rise between the last 2 years and adds it to the final year.
            #This needs to be changed. We need a percentage for its inc/dec
            res = [prediction.calcAnnualRise(data[i:i+2]) for i in range(0,len(data))]
            #Removes the last value, which is none
            res.pop(-1)
            # returns prediction as percentage
            return str(round(sum(res)/len(data),2))+"%"

    def predBiennialRise(data):
        #Checks if it's a list
        if isinstance(data,list):
            #Gets the rise for the pairs of years
            res=[prediction.calcAnnualRise(data[i:i+2]) for i in range(0,len(data))]
            #Removes the last value b/c it returns None
            res.pop(-1)
            #Returns the predicted value as a rounded percentage
            return str(round(sum(res)/len(res),2))+"%"
