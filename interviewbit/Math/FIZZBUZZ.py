class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        if A % 15 == 0:
            return "FizzBuzz"
        elif A % 3 == 0:
            return "Fizz"
        elif A%5 ==0 :
            return "Buzz"
        else:
            return A