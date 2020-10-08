/*
    2nd approach: math

    originally, 	        abcdef=720
	now, 				    abcdcf=540

	and 					a+b+c+d+e+f=21
	now 					a+b+c+d+c+f=20
	
    so...
	e/c = 720/540 = 4/3
	e-c = 1
	
    solve the equation
	c = 3, e = 4

    However, when N=10000000, x! will stackoverflow the int32
	therefore we should not use 'mutiply'
    
    lets say for [1, 2, 3, 3, 5, 6] what if we...
	a^2 + b^2 + c^2 + d^2 + e^2 + f^2 = 91
    a^2 + b^2 + c^2 + c^2 + d^2 + f^2 = 84
    --------------------------------------
                            e^2 - c^2 = 7

	there will be an equation, e^2 - c^2 = 91-75 = 7
	e - c = 1
	e + c = 7
	c=3, e=4

    Time    O(n)
    Space   O(n)
    180 ms, faster than 59.58%
*/
var findErrorNums = function (nums) {
	const n = nums.length;
	let p1 = 0;
	let p2 = 0;
	let s1 = 0;
	let s2 = 0;
	for (let i = 1; i <= n; i++) {
		p1 += i * i;
		s1 += i;
	}
	for (let i = 0; i < n; i++) {
		p2 += nums[i] ** 2;
		s2 += nums[i];
	}
	const p_diff = p1 - p2;
	const s_diff = s1 - s2;
	const dup = (p_diff / s_diff - s_diff) / 2;
	const missing = s_diff + dup;
	return [dup, missing];
};
