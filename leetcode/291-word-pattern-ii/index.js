/*
    1st: backtracking (using recursion + hashtable)
    - similar to lc139, 140, 472
    - use 2 hashtables to save the exact mapping of each of the pattern charactors : portion of string
    - use recursion to try all the possibilites when we slice the remaining pattern and the remaining string

    Look at the corner case:
    p = twt
    s = ttwtt
    Be careful that for the last p = "" and s = "t", we cannot just backtrack directly 
    because t:tt was also mapped earlier in the beginning
    Therefore, we need to check if a mapping was made earlier before we backtrack

    Time    O(?) <- it is hard to determine
    Space   O(P+S)
    304 ms, faster than 5.26%
*/
var wordPatternMatch = function (pattern, s) {
	const forward = {};
	const backward = {};
	const res = dfs(pattern, s, forward, backward);
	// console.log(forward)
	// console.log(backward)
	return res;
};

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

		// A: need to check if the mapping was made earlier in a previous recursion
		let wasMapped = false;
		if (forward[p] === undefined && backward[cand] === undefined) {
			forward[p] = cand;
			backward[cand] = p;
		} else {
			wasMapped = true;
		}

		// explore all possibilities with the remaining pattern and the remaining string
		const b = dfs(pattern.slice(1), s.slice(i + 1), forward, backward);
		if (b) {
			return true;
		}

		// B: need to check if the mapping was made earlier in a previous recursion
		if (wasMapped === false) {
			delete forward[p];
			delete backward[cand];
		}
	}
	return false;
};

let a, b;

// T
a = "abab";
b = "redblueredblue";
console.log(wordPatternMatch(a, b));

// T
a = "aaaa";
b = "asdasdasdasd";
console.log(wordPatternMatch(a, b));

// T
a = "itwasthebestoftimes";
b = "ittwaastthhebesttoofttimes";
console.log(wordPatternMatch(a, b));

// F
a = "itwasthebestoftimes";
b = "ittwaastthhebesttoofttimesss";
console.log(wordPatternMatch(a, b));
