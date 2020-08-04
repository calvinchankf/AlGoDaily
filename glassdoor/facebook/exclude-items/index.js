/*
    Given input:

    // could be potentially more than 3 keys in the object above
    items = [
    {color: 'red', type: 'tv', age: 18},
    {color: 'silver', type: 'phone', age: 20}
    ...
    ]

    excludes = [
    {k: 'color', v: 'silver'},
    {k: 'type', v: 'tv'},
    ....
    ]
    function excludeItems(items, excludes) {
    excludes.forEach(pair => {
        items = items.filter(item => item[pair.k] === item[pair.v]);
    });
    return items;
    }
*/

let items = [
	{ color: "red", type: "tv", age: 18 },
	{ color: "silver", type: "phone", age: 20 },
	{ color: "blur", type: "car", age: 20 },
];

const excludes = [
	{ k: "color", v: "silver" },
	{ k: "color", v: "gold" },
	{ k: "type", v: "tv" },
];

// naive
function excludeItems1(items, excludes) {
	return items.filter((item) => {
		const keys = Object.keys(item);
		let found = false;
		keys.forEach((key) => {
			const val = item[key];
			excludes.forEach((ex) => {
				if (ex.k === key && ex.v === val) {
					found = true;
				}
			});
		});
		return !found;
	});
}
console.log(excludeItems1(items, excludes));

console.log("-----");

// optimized
items = [
	{ color: "red", type: "tv", age: 18 },
	{ color: "silver", type: "phone", age: 20 },
	{ color: "blur", type: "car", age: 20 },
];
function excludeItems2(items, excludes) {
	const exHashes = new Set();
	for (let { k, v } of excludes) {
		exHashes.add(`${k},${v}`);
	}

	return items.filter((item) => {
		const hashes = [];
		for (let key of Object.keys(item)) {
			hashes.push(`${key},${item[key]}`);
		}
		for (let h of hashes) {
			if (exHashes.has(h)) {
				return false;
			}
		}
		return true;
	});
}
console.log(excludeItems2(items, excludes));
