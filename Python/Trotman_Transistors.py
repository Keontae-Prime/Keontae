#Keontae Trotman
import csv
from Trotman_Transistor_Module import average as av
def main():
    # Opens the cpu file
    cpuData=open('cpu.csv')
    # Reads the cpu file
    cpuReader=csv.reader(cpuData)
    # opens gpu file
    gpuData=open('gpu.csv')
    # Reads gpu file
    gpuReader=csv.reader(gpuData)
    # Opens ram file
    ramData=open('ram.csv')
    # Reads ram file
    ramReader=csv.reader(ramData)
    next(cpuReader,None)
    # Dict holding transistor count for cpu
    cpu={}
    #List holding years for cpu
    cpuYears=[]
    # List hold transistor count for cpu
    cpuTransistors=[]
    # List holding chip type for cpu
    cpuType=[]
    #List holding manufacturors for cpu
    cpuManufacturors=[]
    #reads through each row in cpu file
    for row in cpuReader:
        #ignore non-existent transistor counts
        if row[1] != "NA":
            #year holds the year in the current session
            year=(row[2])
            #Count hold transistor count
            count=int(row[1])
            #Chip holds chip name
            chip=row[0]
            #cpumanu holds manufacuror
            cpuManufacturor=row[3]
            #cpu dict holds year as key and chip,transistors,and manu as values
            cpu[year]=chip,count,cpuManufacturor
    # This var sorts the dict by key so the years are in correct order
    sortedByKey = {key:value for key,value in sorted(cpu.items())}
    #Uses sorted dict items
    for k,v in list(sortedByKey.items()):
        # TODO: Create list of years grouped for 1 and 2. TODO: Do predictions and put it next to grouped years
        #appends values to corresponding list
        cpuYears.append(k)
        cpuTransistors.append(v[1])
        cpuType.append(v[0])
        cpuManufacturors.append(v[2])
    #Combines to years
    years=([cpuYears[i:i+2] for i in range(0, len(cpuYears),2)])
    twoYears=cpuYears[0::2]
    twoYears=([twoYears[i:i+2] for i in range(0, len(twoYears),2)])
    #Removes non-existent year
    print("CPU annual average increase:")
    #Combines all vars into a single for loop
    for x,y,z,a in zip(years,av.getAnnualAverage(cpuTransistors),cpuType[1::2],cpuManufacturors[1::2]):
            #Prints output
            print(str(x).replace(","," -")+":",y,"with the",z,"by",a)
    print("CPU biennial average increase:")
    for x,y,z,a in zip(twoYears,av.getBiennalAverage(cpuTransistors),cpuType[2::4],cpuManufacturors[2::4]):
            #Prints output
            print(str(x).replace(","," -")+":",y,"with the",z,"by",a)
    #Skips header
    next(gpuReader,None)
    # gpu dict holds transistor count
    gpu={}
    #Holds years for gpu
    gpuYears=[]
    #Hold transistor count for gpu
    gpuTransistors=[]
    #Holds gpu Type for gpu
    gpuType=[]
    #Holds manus for gpu
    gpuManufacturors=[]
    for row in gpuReader:
        #Captures current session year
        year=(row[2])
        #Captures current session transistors
        count=int(row[1])
        #Captures chip name
        chip=row[0]
        #Captures manu
        gpuManufacturor=row[3]
        #Adds year as key and everything else as values
        gpu[year]=chip,count,gpuManufacturor
    # This var sorts the dict by key so the years are in correct order
    sortedByKey = {key:value for key,value in sorted(gpu.items())}
    #Reads through sorted dict
    for k,v in list(sortedByKey.items()):
        #appends values to associated lists
        gpuYears.append(k)
        gpuTransistors.append(v[1])
        gpuType.append(v[0])
        gpuManufacturors.append(v[2])
    #Links every year
    years=([gpuYears[i:i+2] for i in range(0, len(gpuYears),2)])
    #Links every other year
    twoYears=gpuYears[0::2]
    twoYears=([twoYears[i:i+2] for i in range(0, len(twoYears),2)])
    #Removes non existent year
    twoYears.pop(-1)
    # Gets the average increase and formats it
    print("GPU annual average increase:")
    for x,y,z,a in zip(years,av.getAnnualAverage(gpuTransistors),gpuType[1::2],gpuManufacturors[1::2]):
            print(str(x).replace(","," -")+":",y,"with the",z,"by",a)
    #Gets the Biennal increase and formats it
    for x,y,z,a in zip(twoYears,av.getBiennalAverage(gpuTransistors),gpuType[2::4],gpuManufacturors[2::4]):
            #Prints output
            print(str(x).replace(","," -")+":",y,"with the",z,"by",a)
    next(ramReader,None)
    #The same thing is done for ram
    ram={}
    ramYears=[]
    ramTransistors=[]
    ramType=[]
    ramManufacturors=[]
    twoYears=[]
    for row in ramReader:
        if row[4]!="NA":
            year=(row[5])
            count=int(row[4])
            chip=row[0]
            ramManufacturor=row[6]
            ram[year]=chip,count,ramManufacturor
    # This var sorts the dict by key so the years are in correct order
    sortedByKey = {key:value for key,value in sorted(ram.items())}
    for k,v in list(sortedByKey.items()):
        ramYears.append(k)
        ramTransistors.append(v[1])
        ramType.append(v[0])
        ramManufacturors.append(v[2])
    years=([ramYears[i:i+2] for i in range(0, len(ramYears),2)])
    twoYears=ramYears[0::2]
    twoYears=([twoYears[i:i+2] for i in range(0, len(twoYears),2)])
    print("RAM annual average increase:")
    for x,y,z in zip(years,av.getAnnualAverage(ramTransistors),ramManufacturors[1::2]):
            print(str(x).replace(","," -")+":",y,"by",z)
    print("RAM biennial average increase:")
    for x,y,z in zip(twoYears,av.getBiennalAverage(ramTransistors),ramManufacturors[2::4]):
        #Prints output
        print(str(x).replace(","," -")+":",y,"by",z)
#Calls the main function
main()