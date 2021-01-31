/*
    1st approach: 2 stacks

    - 1st stack for counts
    - 2nd stack for substrings

    e.g. ab2[c3[de]]f

    when it comes to 2[
    cntStack = [2]
    strStack = ['ab', '']

    when it comes to 3[
    cntStack = [2, 3]
    strStack = ['ab', 'c', '']

    when it comes to the character before 1st ], 
    cntStack = [2, 3]
    strStack = ['ab', 'c', 'de']
    
    when it comes to 1st ], multiply 3 with 'de' and append to 'c'
    cntStack = [2]
    strStack = ['ab', 'cdedede']

    when it comes to 2nd ], , multiply 2 with 'cdedede' and append to 'abc'
    cntStack = []
    strStack = ['abcdededecdedede']

    when it comes to f
    cntStack = []
    strStack = ['abcdededecdededef']

    Time    O(n)
    Space   O(n)
    76 ms, faster than 68.48%
*/
var decodeString = function(s) {
    const count_stack = []
    const chars_stack = ['']
    let num = 0
    for (let c of s) {
        if (parseInt(c) >= 0 && parseInt(c) <= 9) {
            num = num * 10 + parseInt(c)
        } else if (c == '[') {
            chars_stack.push('')
            count_stack.push(num)
            num = 0
        } else if (c == ']') {
            const count = count_stack.pop()
            const sub = chars_stack.pop()
            chars_stack[chars_stack.length-1] += sub.repeat(count)
        } else {
            chars_stack[chars_stack.length-1] += c
        }
    }
    return chars_stack[0]
};

/*
    2nd approach: recursion

    Time    O(2n)
    Space   O(n)
    108 ms, faster than 6.34%
*/
var decodeString = function (s) {
	const q = [];
	for (let x of s) {
		q.push(x);
	}
	return recur(q);
};

const recur = (q) => {
	if (q.length === 0) {
		return "";
	}
	let s = "";
	let num = 0;
	while (q.length > 0) {
		const x = q.shift();
		if (parseInt(x) >= 0 && parseInt(x) < 10) {
			num = num * 10 + parseInt(x);
		} else if (x === "[") {
			const single = recur(q);
            s += single.repeat(num);
            num = 0;
		} else if (x === "]") {
			return s;
		} else {
			s += x;
		}
	}
	return s;
};
