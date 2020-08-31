/*
    1st: brute force
    TLE 
*/
var getWinner = function (arr, k) {
	if (k >= arr.length) {
		return Math.max(...arr);
	}
	let winner = 0;
	let winnerCount = 0;
	while (true) {
		const first = arr[0];
		const second = arr[1];
		if (first > second) {
			if (first === winner) {
				winnerCount += 1;
			} else {
				winner = first;
				winnerCount = 1;
			}
			arr = [first, ...arr.slice(2), second];
		} else {
			if (second === winner) {
				winnerCount += 1;
			} else {
				winner = second;
				winnerCount = 1;
			}
			arr = [...arr.slice(1), first];
		}
		if (winnerCount === k) {
			return winner;
		}
	}
};

/*
    2nd
    - in fact, we dont need to shift the array, we just iterate through it and keep track of the global winner

    Time    O(N)
    Space   O(1)
    100 ms, faster than 100.00%
*/
var getWinner = function (arr, k) {
	let cur = arr[0];
	let winCount = 0;
	for (let i = 1; i < arr.length; i++) {
		if (arr[i] > cur) {
			cur = arr[i];
			winCount = 1;
		} else {
			winCount += 1;
		}
		if (winCount == k) {
			break;
		}
	}
	return cur;
};
