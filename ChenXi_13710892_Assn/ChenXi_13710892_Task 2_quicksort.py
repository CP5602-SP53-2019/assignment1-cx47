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


def quick_sort(li):
    if len(li)<2:
        return li
    mid = li.pop(0)
    left, right = [],[]
    for i in li:
        if i>mid:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)


def rNGenerator(noDuplicates,lowerLimit,upperLimit,numOfValues):
    if noDuplicates == True:
        generateNumList=[]
        while len(generateNumList) < numOfValues:
            x = random.randint(lowerLimit,upperLimit)
            if x not in generateNumList:
                generateNumList.append(x)
        lst = quick_sort(generateNumList)
        lstf = "lowerLimit=" + str(lowerLimit) +'\n'+ "upperLimit=" + str(upperLimit) + '\n'+"numOfValues=" + str(numOfValues) + '\n'+str(lst)
        print(lstf)
        saveToFile(lstf)
        
    else:
        noDuplicates == False
        generateNumList=[]
        while len(generateNumList) < numOfValues:
            generateNumList.append(random.randint(lowerLimit,upperLimit))
        else:
            lst = quick_sort(generateNumList)
            lstf = "lowerLimit=" + str(lowerLimit) +'\n'+ "upperLimit=" + str(upperLimit) + '\n'+"numOfValues=" + str(numOfValues) + '\n'+str(lst)
            print(lstf)
            saveToFile(lstf)
start_time = time.time()
rNGenerator(noDuplicates,lowerLimit,upperLimit,numOfValues)
print("The generation takes {:.5f} seconds" .format(time.time() - start_time))



    



