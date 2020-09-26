function balancedBrackets(s) {
	// Write your code here.
	const m = {
		"]": "[",
		"}": "{",
		")": "(",
	};
	const stack = [];
	for (let i = 0; i < s.length; i++) {
		const c = s[i];
		if (c == "[" || c == "(" || c == "{") {
			stack.push(c);
		} else if (c == "]" || c == ")" || c == "}") {
			if (stack.length > 0 && stack[stack.length - 1] == m[c]) {
				stack.pop();
			} else {
				return false;
			}
		}
	}
	return stack.length == 0;
}

// Do not edit the line below.
exports.balancedBrackets = balancedBrackets;
