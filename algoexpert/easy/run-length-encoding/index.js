/*
    count chars, with limit=9

    P.S. in a real interview, the interviewer would not tell you that you can split 12A to 9A3A
*/
function runLengthEncoding(s) {
	const n = s.length
	if (n === 0) {
		return ''
	}
    // Write your code here.
	let res = []
	let count = 1
	let prev = s[0]
	for (let i = 1; i < n; i++) {
		const c = s[i]
		if (c === prev) {
			count += 1
			if (count == 9) {
				if (count > 0) { res.push(`${count}${prev}`) }
				count = 0
			}
		} else {
			if (count > 0) { res.push(`${count}${prev}`) }
			prev = c
			count = 1
		}
	}
	if (count > 0) { res.push(`${count}${prev}`) }
	return res.join('')
}

// Do not edit the line below.
exports.runLengthEncoding = runLengthEncoding;


// Do not edit the line below.
exports.runLengthEncoding = runLengthEncoding;
