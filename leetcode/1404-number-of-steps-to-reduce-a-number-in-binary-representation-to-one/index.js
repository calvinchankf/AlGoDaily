/*
    1st: bit op
    
    /2:  x >>= 1
    +1:  flip all the 1 from the right until we meet 0
        e.g.
            100111 (39)
                +1
            -----------
            101000 (40)
    
    Time     O(NlogN)
    Space    O(N)
    60 ms, faster than 83.80%
*/

/**
 * Time     O(NlogN)
 * Space    O(N)
 * 60 ms, faster than 83.80%
 * @param {string} s
 * @return {number}
 */
var numSteps = function (s) {
	const arr = Array.from(s);
	let steps = 0;
	while (arr.length > 1) {
		if (arr[arr.length - 1] == 0) {
			// divide by 2
			arr.pop();
		} else {
			// +1
			let i;
			for (i = arr.length - 1; i >= 0; i--) {
				if (arr[i] == 1) {
					arr[i] = 0;
				} else {
					arr[i] = 1;
					break;
				}
			}
			if (i == -1) {
				arr.unshift(1);
			}
		}
		steps += 1;
	}
	return steps;
};
