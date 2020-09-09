function patternMatcher(pattern, s) {
	// Write your code here.
	const forward = {};
	const backward = {};
	const res = dfs(pattern, s, forward, backward);
	if (res == false) {
		return [];
	}
	const arr = [
		forward["x"] ? forward["x"] : "",
		forward["y"] ? forward["y"] : "",
	];
	return arr;
}
const dfs = (pattern, s, forward, backward) => {
	if (s.length == 0 && pattern.length == 0) {
		return true;
	}
	if (s.length == 0 || pattern.length == 0) {
		return false;
	}
	const p = pattern[0];
	for (let i = 0; i < s.length; i++) {
		const cand = s.slice(0, i + 1);

		if (p in forward && forward[p] !== cand) {
			continue;
		}
		if (cand in backward && backward[cand] !== p) {
			continue;
		}

		let wasMapped = false;
		if (forward[p] === undefined && backward[cand] === undefined) {
			forward[p] = cand;
			backward[cand] = p;
		} else {
			wasMapped = true;
		}

		const b = dfs(pattern.slice(1), s.slice(i + 1), forward, backward);
		if (b) {
			return true;
		}

		if (wasMapped === false) {
			delete forward[p];
			delete backward[cand];
		}
	}
	return false;
};

// Do not edit the line below.
exports.patternMatcher = patternMatcher;
