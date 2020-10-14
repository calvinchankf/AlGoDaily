/*
    1st: sort + 2 pointers

    Time    O(NlogN)
    Space   O(N)
    184 ms, faster than 100.00%
*/
var maxBoxesInWarehouse = function (boxes, warehouse) {
	let curMin = Number.MAX_SAFE_INTEGER;
	const houses = Array(warehouse.length).fill(Number.MAX_SAFE_INTEGER);
	for (let i = 0; i < warehouse.length; i++) {
		curMin = Math.min(curMin, warehouse[i]);
		houses[i] = curMin;
	}
	houses.reverse();
	boxes.sort((a, b) => a - b);
	let res = 0;
	let i = 0;
	let j = 0;
	while (i < boxes.length && j < houses.length) {
		if (boxes[i] <= houses[j]) {
			res += 1;
			i += 1;
			j += 1;
		} else {
			j += 1;
		}
	}
	return res;
};
