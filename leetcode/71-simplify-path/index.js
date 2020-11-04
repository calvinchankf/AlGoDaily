/*
    2nd : string construction + stack
    - put every substring (not '.' and '..') into a stack
    - when we see a '..', pop the stack
    - join the stack to return a result

    Time    O(N)
    Space   O(N)
    48 ms, faster than 7.40% 
*/
var simplifyPath = function (path) {
	const stack = [];
	let i = 0;
	let cur = "";
	while (i <= path.length) {
		if ((i < path.length && path[i] == "/") || i == path.length) {
			if (cur.length > 0) {
				if (cur == "..") {
					if (stack.length > 0) {
						stack.pop();
					}
				} else if (cur !== ".") {
					stack.push(cur);
				}
			}
			cur = "";
		} else {
			cur += path[i];
		}
		i += 1;
	}
	// console.log(stack)
	return "/" + stack.join("/");
};
