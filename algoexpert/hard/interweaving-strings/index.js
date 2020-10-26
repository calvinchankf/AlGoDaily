function interweavingStrings(a, b, c) {
	// Write your code here.
	return dfs(a, 0, b, 0, c, 0, {});
}

const dfs = (a, i, b, j, c, k, ht) => {
	if (i == a.length && j == b.length && k == c.length) {
		return true;
	} else if (i == a.length && j == b.length) {
		return false;
	} else if (k == c.length && (i == a.length || j == b.length)) {
		return false;
	}

	const key = `${i},${j},${k}`;
	if (key in ht) {
		return ht[key];
	}

	let canForm = false;
	if (a[i] == c[k]) {
		canForm = canForm || dfs(a, i + 1, b, j, c, k + 1, ht);
	}
	if (b[j] == c[k]) {
		canForm = canForm || dfs(a, i, b, j + 1, c, k + 1, ht);
	}
	// console.log(i, j, k, a[i], b[j], c[k], canForm);
	ht[key] = canForm;
	return canForm;
};

let a, b, c;
a = "algoexpert";
b = "your-dream-job";
c = "your-algodream-expertjob";
console.log(interweavingStrings(a, b, c));

// Do not edit the line below.
exports.interweavingStrings = interweavingStrings;
