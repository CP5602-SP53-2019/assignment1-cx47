import time
import random
lowerLimit = -46600
upperLimit = 84400
numOfValues = 100000
noDuplicates = False

def saveToFile(lst):
    file = open("C:/Users/chenxi/Desktop/New folder/Test.txt",'w')
    file.write(str(lst))
    file.close()

def rNGenerator(noDuplicates,lowerLimit,upperLimit,numOfValues):
    if noDuplicates == True:
        generateNumList = []
        while len(generateNumList) < numOfValues:
            x = random.randint(lowerLimit,upperLimit)
            if x not in generateNumList:
                generateNumList.append(x)
        lst = "lowerLimit=" + str(lowerLimit) +'\n'+ "upperLimit=" + str(upperLimit) + '\n'+"numOfValues=" + str(numOfValues) + '\n'+str(generateNumList)
        print(lst)
        saveToFile(lst)
    else:
        noDuplicates == False
        generateNumList=[]
        while len(generateNumList) < numOfValues:
            generateNumList.append(random.randint(lowerLimit,upperLimit))
        else:
            lst = "lowerLimit=" + str(lowerLimit) +'\n'+ "upperLimit=" + str(upperLimit) + '\n'+"numOfValues=" + str(numOfValues) + '\n'+str(generateNumList)
        print(lst)
        saveToFile(lst)
            
start_time = time.time()
rNGenerator(noDuplicates,lowerLimit,upperLimit,numOfValues)
print("The generation takes {:.5f} seconds" .format(time.time() - start_time))


    



