/**
 * @param {string} s
 * @return {number}
 */
var minCut = function (s) {
	const partitions = dfs(s, {});
	return partitions - 1;
};

const dfs = (s, ht) => {
	if (s.length == 0) {
		return 0;
	}
	if (s in ht) {
		return ht[s];
	}
	let minGroupLen = Number.MAX_SAFE_INTEGER;
	let forwardSub = "";
	let backwardSub = "";
	for (let i = 0; i < s.length; i++) {
		forwardSub += s[i];
		backwardSub = s[i] + backwardSub;
		if (forwardSub == backwardSub) {
			const groupLen = dfs(s.slice(i + 1), ht) + 1;
			if (groupLen < minGroupLen) {
				minGroupLen = groupLen;
			}
		}
	}
	ht[s] = minGroupLen;
	return ht[s];
};

const reverse = (str) => {
	let cur = "";
	for (let i = str.length - 1; i >= 0; i--) {
		cur += str[i];
	}
	return cur;
};
