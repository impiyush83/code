class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        distanceMapper = dict()
        for index in range(0, len(list1)):
            distanceMapper[list1[index]] = index

        shortestDistance = 9999999999
        currentSum = 0
        finalList = []
        for index in range(0, len(list2)):
            if distanceMapper.get(list2[index]) != None:
                currentSum = index + distanceMapper.get(list2[index])
                if currentSum < shortestDistance:
                    finalList, shortestDistance = [], currentSum
                    finalList.append(list2[index])
                elif currentSum == shortestDistance:
                    finalList.append(list2[index])
        return finalList


'''
O(l1 + l2) - iterating over 2 loops

'''