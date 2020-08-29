function hasSingleCycle(array) {
	// Write your code here.
	const n = array.length;
	const hs = new Set();
	let start = 0;
	let cur = start;
	while (1) {
		if (hs.has(cur)) {
			break;
		}
		hs.add(cur);
		const steps = array[cur] % n;
		cur = (cur + n + steps) % n;
	}
	return hs.size == n && cur == start;
}

let a;

a = [2, 3, 1, -4, -4, 2];
console.log(hasSingleCycle(a));

a = [1, 1, 1, 1, 2];
console.log(hasSingleCycle(a));

a = [10, 11, -6, -23, -2, 3, 88, 908, -26];
console.log(hasSingleCycle(a));
