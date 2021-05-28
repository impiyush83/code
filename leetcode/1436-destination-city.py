class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startingCities, destinationCities = set(), set()
        for route in paths:
            startingCities.add(route[0])
            destinationCities.add(route[1])
        return list(destinationCities.difference(startingCities))[0]


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(paths))
        return (B-A)[0]


'''
Time Complexity

O(N) - Interating over the loop once


'''