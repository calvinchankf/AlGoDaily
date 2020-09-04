function isPalindrome(s) {
	// Write your code here.
	const n = s.length;
	let i = 0;
	let j = n - 1;
	while (i < j) {
		if (s[i] !== s[j]) {
			return false;
		}
		i += 1;
		j -= 1;
	}
	return true;
}

// Do not edit the line below.
exports.isPalindrome = isPalindrome;
