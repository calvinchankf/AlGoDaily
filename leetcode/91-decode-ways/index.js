var numDecodings = function (s) {
	const ht = {};

	const dfs = (remain) => {
		if (remain.length == 0) {
			return 1;
		}

		if (remain in ht) {
			return ht[remain];
		}

		let total = 0;

		const first = remain[0];
		if (first == 0) {
			// coercion
			return 0;
		}
		total += dfs(remain.slice(1));

		if (remain.length >= 2) {
			const ab = remain.slice(0, 2);
			if (ab <= 26) {
				total += dfs(remain.slice(2));
			}
		}

		ht[remain] = total;
		return total;
	};

	return dfs(s);
};
