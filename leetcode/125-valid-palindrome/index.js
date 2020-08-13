/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
	if (s.length === 0) {
		return true;
	}
	const S = s.toLowerCase();
	let left = 0;
	let right = s.length - 1;
	while (left <= right) {
		const isLeftAlphaNum = isAlphaNum(S[left]);
		const isRightAlphaNum = isAlphaNum(S[right]);
		if (S[left] === S[right]) {
			left += 1;
			right -= 1;
		} else if (isLeftAlphaNum === false) {
			left += 1;
		} else if (isRightAlphaNum === false) {
			right -= 1;
		} else {
			return false;
		}
	}
	return true;
};

const isAlphaNum = (s) => {
	const c = s.charCodeAt(0);
	const a = "a".charCodeAt(0);
	if (c - a >= 0 && c - a < 26) {
		return true;
	}
	const z = "0".charCodeAt(0);
	if (c - z >= 0 && c - z < 10) {
		return true;
	}
	return false;
};
