/*
    2nd approach:

    The basic idea is to use a stack.
    when we encounter, we do operation with the last item in the stack with the last operator and the current number
    e.g. + 1 + 2 * 3 + ...
    lastOp = *
    cur = 3
    stack = [1, 2]
    when it reaches to the last +, we pop the 2, multipy with the current number and put it back to the stack => [1, 6]


    1. use 1 stack
    2. 1 buffer for number(cos it might have more than one digit)
    3. 1 buffer for operator
    4. if the current character is an operator
        1. operate the current number with the previous operator
        2. and put the result into the stack
        3. set the current character as the next operator
    5. sum up all the numbers in the stack to get the result

    Time    O(2n)
    Space   O(n) the stack
    108 ms, faster than 53.03%
*/
var calculate = function (s) {
	let sign = "+";
	let num = 0;
	const stack = [];
	for (let i = 0; i < s.length; i++) {
		const c = s[i];
		if ("0123456789".indexOf(parseInt(c)) > -1) {
			num = num * 10 + parseInt(c);
		}
		if (i + 1 == s.length || "+-*/".indexOf(c) > -1) {
			if (sign == "+") {
				stack.push(num);
			} else if (sign == "-") {
				stack.push(-num);
			} else if (sign == "*") {
				const n = stack.length;
				stack[n - 1] = stack[n - 1] * num;
			} else if (sign == "/") {
				const n = stack.length;
				// in js, -3/2 = -2,
				// but the question wants "The integer division should truncate toward zero"
				// so should be -3/2 = -1
				const isNegative = stack[n - 1] < 0;
				const temp = Math.abs(stack[n - 1]);
				stack[n - 1] = Math.floor(temp / num);
				if (isNegative) {
					stack[n - 1] = -stack[n - 1];
				}
			}
			sign = c;
			num = 0;
		}
	}
	let res = 0;
	for (let num of stack) {
		res += num;
	}
	return res;
};
