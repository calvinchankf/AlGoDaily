/*
    2nd approach: dynamic programming
    
    Time    O(n)
    Space   O(1)
    144 ms, faster than 6.35%
*/
var rob = function (nums) {
	let rob = 0;
	let notRob = 0;
	for (let x of nums) {
		let temp = rob;
		rob = Math.max(rob, notRob + x);
		notRob = temp;
	}
	return Math.max(rob, notRob);
};
