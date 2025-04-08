
def handle_uploaded_file(f):
    with open("test.txt", "wb+") as desitination:
        for chunk in f.chunks():
            desitination.write(chunk)
            # print(desitination)

def clean_file(file):
    lineFile = file.split('\n')
    lineFile.pop()
    lineFile.reverse()
    activityList = lineFile.pop()

    activityList = activityList.split(',')
    

    # return lineFile

    '''
    Indicies and Categories
    0 - Date
    1 - Move minutes 
    2 - Calories
    3 - Distance
    4 - Heart Points
    6 - Average heart rate
    7 and 8 - Max and Min heart rate
    
    '''

    catList = ['date', 'move minutes count', 'calories (kcal)', 'heart points', 'distance (m)']

    indexDict = {}

    for i in range(len(activityList) - 1):
        if(activityList[i].lower() in catList):
            indexDict[activityList[i].lower()] = i

    # print(indexDict)
    for i in range(len(lineFile)):
        lineFile[i] = lineFile[i].split(',')
        

    statList = []

    for i in range(len(lineFile)):
        statList.append([])
        for cat in catList:
            currIndex = indexDict[cat]
            if(lineFile[i][currIndex] == ''):
                statList[i].append('0')
            else:
                statList[i].append(lineFile[i][currIndex])
        
    finalList = [catList] + statList
        

    return finalList

def get_sublist(offset, list):
    start = 0
    end = int(offset) + 1
    
    return list[start:end]

def get_year_sublist(years, data):
    sublist = []
    sublist.append(data[0])
    for i in range(len(data)):
        currDate = data[i][0]
        if currDate[0:4] in years:
            sublist.append(data[i])

    return sublist

def find_average(list):

    avgList = []

    for i in range(1, len(list[0])):
        currAvg = 0
        for j in range(1, len(list)):
            currAvg += float(list[j][i])
            
        avgList.append(currAvg / len(list))


    return avgList


def get_year_list(data):
    yearList = []
    i = 1
    while i < len(data) - 1:
        currDate = data[i + 1][0]

        if currDate[0:4] not in yearList:
            yearList.append(currDate[0:4])
        i+= 1
    return yearList
        

