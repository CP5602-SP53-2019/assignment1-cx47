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

def insert_sort(alist):
    n = len(alist)	
    for j in range(1, n): 
        for i in range(j, 0, -1): 
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break
    return alist

def rNGenerator(noDuplicates,lowerLimit,upperLimit,numOfValues):
    if noDuplicates == True:
        generateNumList=[]
        while len(generateNumList) < numOfValues:
            x = random.randint(lowerLimit,upperLimit)
            if x not in generateNumList:
                generateNumList.append(x)
        lst = insert_sort(generateNumList)
        lstf = "lowerLimit=" + str(lowerLimit) +'\n'+ "upperLimit=" + str(upperLimit) + '\n'+"numOfValues=" + str(numOfValues) + '\n'+str(lst)
        print(lstf)
        saveToFile(lstf)

    else:
        noDuplicates == False
        generateNumList=[]
        while len(generateNumList) < numOfValues:
            generateNumList.append(random.randint(lowerLimit,upperLimit))
        else:
            lst = insert_sort(generateNumList)
            lstf = "lowerLimit=" + str(lowerLimit) +'\n'+ "upperLimit=" + str(upperLimit) + '\n'+"numOfValues=" + str(numOfValues) + '\n'+str(lst)
            print(lstf)
            saveToFile(lstf)
start_time = time.time()            
rNGenerator(noDuplicates,lowerLimit,upperLimit,numOfValues)
print("The generation takes {:.5f} seconds" .format(time.time() - start_time))


    



