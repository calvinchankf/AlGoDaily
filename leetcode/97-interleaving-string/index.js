/*
    2nd: dynamic programming, recursive dfs + hashtable
    - recursively check the suffix, to see if we can form s3 from the end

    e.g.
    s1 = abc
    s2 = def
    s3 = abdecf

    At the bottom of the recursion:
    s2[2:] = s3[5:], f = f so we return true

    then we see that:
    s1[2] == s3[4] and s2[2:] = s3[5:](the result from recursion), so we return true

    ....do the steps over and over again we will get the result

    Time    O(MN)
    Space   O(M+N)
    80 ms, faster than 88.17%
*/
var isInterleave = function (s1, s2, s3) {
	return dfs(s1, 0, s2, 0, s3, 0, {});
};

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
