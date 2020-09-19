function diskStacking(disks) {
	// Write your code here.
	const n = disks.length;
	disks.sort((a, b) => a[0] * a[1] * a[2] - b[0] * b[1] * b[2]);
	const dp = [];
	for (let i = 0; i < n; i++) {
		dp.push([disks[i]]);
	}
	for (let i = 0; i < n; i++) {
		const [w1, d1, h1] = disks[i];
		let maxH = 0;
		let maxHStack = null;
		for (let j = 0; j < i; j++) {
			const [w2, d2, h2] = disks[j];
			if (w2 < w1 && d2 < d1 && h2 < h1) {
				const h = calculateHeight(dp[j]);
				if (h + h1 > maxH) {
					maxH = h + h1;
					maxHStack = dp[j];
				}
			}
		}
		if (maxHStack) {
			dp[i] = maxHStack.concat(dp[i]);
		}
	}
	// console.log(dp);
	let maxH = 0;
	let maxHStack = null;
	for (let i = 0; i < n; i++) {
		const h = calculateHeight(dp[i]);
		if (h > maxH) {
			maxH = h;
			maxHStack = dp[i];
		}
	}
	return maxHStack;
}

function calculateHeight(stack) {
	let total = 0;
	for (let i = 0; i < stack.length; i++) {
		const [w, d, h] = stack[i];
		total += h;
	}
	return total;
}

let a;

a = [
	[2, 1, 2],
	[3, 2, 3],
	[2, 2, 8],
	[2, 3, 4],
	[1, 3, 1],
	[4, 4, 5],
];
console.log(diskStacking(a));

// Do not edit the line below.
exports.diskStacking = diskStacking;
