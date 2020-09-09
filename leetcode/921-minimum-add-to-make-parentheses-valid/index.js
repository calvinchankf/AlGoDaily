/*
    1st approach: stack
    
    e.g. ()))((

            ( ) ) ) ( ( (
                        ^
    open    1 0 0 0 1 2 3
    close   0 0 1 2 2 2 2

	Time	O(n)
	Space	O(n)
    20 ms, faster than 96.69%
*/
var minAddToMakeValid = function (S) {
	let open = 0;
	let close = 0;
	for (let c of S) {
		if (c == "(") {
			open += 1;
		} else if (open > 0) {
			open -= 1;
		} else {
			close += 1;
		}
	}
	return open + close;
};
