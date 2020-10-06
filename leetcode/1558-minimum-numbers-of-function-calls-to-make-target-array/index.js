/*
    1st: math
    - think backward:
        - if all items in an array are even, divide them by 2
        - else subtract every number by 1
    - instead of doing it in a brute force fashion, we can look at the /2 and -1 on each of the numbers

    e.g. [3, 2, 2, 4]
    /2    1  1  1  2 <=== we can do 2 times operation2
    -1    2  1  1  1 <=== there are 5 times operation1
    So the answer 2 + 5 = 7

    Time    O(NlogM)
    Space   O(1)
    108 ms, faster than 100.00% 
*/
var minOperations = function (nums) {
	let a = 0;
	let b = 0;
	for (let x of nums) {
		const [one, two] = divide(x);
		a += one;
		b = Math.max(b, two);
	}
	return a + b;
};

const divide = (x) => {
	let two = 0;
	let one = 0;
	while (x > 0) {
		if (x % 2 == 0) {
			two += 1;
			x = Math.floor(x / 2);
		} else {
			one += 1;
			x -= 1;
		}
	}
	return [one, two];
};
