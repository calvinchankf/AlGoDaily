"""
    1st approach:
	1. separate the number portion by portion with 3 digits, 123456789 -> 123, 456, 789
	2. for each 3 digits, translate to english
	3. append Thousand, Million and Billion in between the portions

	Time		O(N)
	Space		O(N)
	20 ms, faster than 100.00%
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        d = ["", "Thousand", "Million", "Billion"]
        result = ""
        i = 0
        while num > 0:
            remain = num % 1000
            num = num // 1000
            threeDigitWord = self.threeDigitsToWords(remain)
            # imagine if we have 1,000,000, we should check if the '3digits' is empty before appending to the result
            if len(threeDigitWord) > 0:
                result = threeDigitWord + " " + d[i] + " " + result
            i += 1
        return result.strip()

    def threeDigitsToWords(self, num):
        digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                  "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        a = num // 100
        bc = num % 100
        temp = ""
        if a > 0:
            temp += digits[a] + " Hundred"
        if bc < 20:
            temp += " " + digits[bc]
        else:
            b = bc // 10
            c = bc % 10
            temp += " " + tens[b]
            temp += " " + digits[c]
        return temp.strip()


"""
    2nd: similar to 1st but using an array instead of a string for the result construction

    Time		O(N)
	Space		O(N)
    20 ms, faster than 70.44%
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        d = ["", "Thousand", "Million", "Billion"]
        result = []
        i = 0
        while num > 0:
            remain = num % 1000
            num = num // 1000
            threeDigitWord = self.threeDigitsToWords(remain)
            # imagine if we have 1,000,000, we should check if the '3digits' is empty before appending to the result
            if len(threeDigitWord) > 0:
                result.insert(0, threeDigitWord + ' ' + d[i])
            i += 1
        return ' '.join(result).strip()

    def threeDigitsToWords(self, num):
        digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                  "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        a = num // 100
        bc = num % 100
        expression = []
        if a > 0:
            expression.append(digits[a])
            expression.append("Hundred")
        if bc < 20:
            expression.append(digits[bc])
        else:
            b = bc // 10
            c = bc % 10
            expression.append(tens[b])
            expression.append(digits[c])
        return ' '.join(expression).strip()
