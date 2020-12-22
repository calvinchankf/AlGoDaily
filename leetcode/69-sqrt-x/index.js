/*
    2nd: upper bound binary search
    - since 1 <= x <= x^2 for all x > 0
    - we are going to search for a number that which sqaure is just right a bit larger than x

    e.g. 8
    1 2 3 4 5 6 7 8
    ^             ^

    1 2 3 4 5 6 7 8
    ^     ^

    1 2 3 4 5 6 7 8
        ^   ^

    1 2 3 4 5 6 7 8
        ^
    3^2 = 9 is larger than 8, therefore answer should be 3-1=2

    Time    O(logN)
    Space   O(1)
    96 ms, faster than 73.18%
*/
var mySqrt = function (x) {
	if (x <= 0) {
        return 0
    }
    let left = 1
    let right = x
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (mid*mid < x) {
            left = mid + 1
        } else if (mid*mid > x) {
            right = mid - 1
        } else {
            return mid
        }
    }
    return right
};
