"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

"""
    1st: array
    - bad description
    - in short, lets say we want to read the first 5 characters from "leetcode" using read4()

    1. when we call read4(interanlBuffer), interanlBuffer = [l, e, e, t]
    so then we push all 4 items from interanlBuffer to our result by buf.push()

    2. when we call read4(interanlBuffer), interanlBuffer = [c, o, d, e]
    since we only need 1 more character, we only have to push the "c" into buff

    As a result,
    interanlBuffer = [o, d, e]
    buff = [l, e, e, t, c]

    Caveat:
    - buf4 should be of length 4 to use read4()
    - buf is of length 512, so please use index to assign the value

    Time    O(N)
    Space   O(4)
    32 ms, faster than 58.76%
"""
class Solution:
    def __init__(self):
        self.buf4 = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total = 0
        while total < n:
            if len(self.buf4) == 0:
                buf4 = 4 * ['']
                c = read4(buf4)
                if c == 0:
                    break
                self.buf4 = buf4[:c]
            while total < n and len(self.buf4) > 0:
                top = self.buf4.pop(0)
                buf[total] = top
                total += 1
        return total