/*
    1st: brute force

    Time    O(N^2)
    Space   O(N)
    LTE: 33 / 35 test cases passed.
*/
var bulbSwitch = function (n) {
	if (n <= 0) {
		return 0;
	}
	const A = Array(n).fill(false);
	for (let i = 1; i <= n; i++) {
		for (let j = i; j <= n; j += i) {
			A[j - 1] = !A[j - 1];
		}
	}
	let res = 0;
	for (let x of A) {
		if (x === true) {
			res += 1;
		}
	}
	return res;
};

/*
    2nd: observation + math
    - look at the result from 1st, we can see that the intervals between 1s are increasing with 2

    e.g. 50
    10010000100000010000000010000000000100000000000010
     2   4      6       8       10          12

    therefore we can just compute the number of 1s by constructing a string virtually

    Time    O(logN) ?
    Space   O(1)
    76 ms, faster than 47.54%
*/
var bulbSwitch = function (n) {
	if (n <= 0) {
		return 0;
	}
	let i = 0;
	let j = 0;
	while (j < n) {
		i += 1;
		j += 2 * i + 1;
	}
	return i;
};

/*
    3nd: observation + math
    - look at the results again

    1st : 1
    2nd : 1 0
    3rd : 1 0 0
    4th : 1 0 0 1
    5th : 1 0 0 1 0
    6th : 1 0 0 1 0 0
    7th : 1 0 0 1 0 0 0
    8th : 1 0 0 1 0 0 0 0
    9th : 1 0 0 1 0 0 0 0 1
   10th : 1 0 0 1 0 0 0 0 1 0 
   11th : 1 0 0 1 0 0 0 0 1 0 0 
   12th : 1 0 0 1 0 0 0 0 1 0 0 0 
   13th : 1 0 0 1 0 0 0 0 1 0 0 0 0
   14th : 1 0 0 1 0 0 0 0 1 0 0 0 0 0 
   15th : 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0
   16th : 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 

    - the 1s are at: 1, 4, 9, 16...etc the sqaure numbers
    - so the question is essentially asking us to compute the number of square numbers before n

    Time    O(square of N) ?
    Space   O(1)
    76 ms, faster than 47.54%
*/
var bulbSwitch = function (n) {
	return parseInt(Math.sqrt(n));
};
