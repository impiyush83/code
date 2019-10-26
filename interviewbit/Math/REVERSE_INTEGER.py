class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, x):
        output_range = [-pow(2,31), pow(2,31)-1]
        x = str(x)
        # string reverse
        x = x[::-1]
        if x[-1] == '-':
            # for negative numbers
            output = int("-"+x[0:-1])
        else:
            # for postive numbers
            output = int(x[:])
        if output < output_range[0] or output > output_range[-1]:
                return 0
        return output