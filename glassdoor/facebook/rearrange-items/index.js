/*
    Given an input array and another array that describes a new index for each element, 
    mutate the input array so that each element ends up in their new index. 
    Discuss the runtime of the algorithm and how you can be sure there won't be any infinite loops.
*/

// e.g.
let a = ["a", "b", "c", "d", "e", "f"];
const b = [2, 3, 4, 0, 5, 1];
// result: a = ["d", "f", "a", "b", "c", "e"]

/*
    1st: hashtable
    Time    O(N)
    Space   O(N)
*/
const rearrangeItems1 = (items, indices) => {
	const clone = [...items];
	for (let i = 0; i < indices.length; i++) {
		const j = indices[i];
		const c = clone[i];
		items[j] = c;
	}
};

rearrangeItems1(a, b);
console.log(a);

console.log("-----");

/*
    2nd: cyclic sort

    Time    O(N)
    Space   O(1)
*/
a = ["a", "b", "c", "d", "e", "f"];
function rearrangeItems2(arr, indices) {
	let i = 0;
	while (i < arr.length) {
		if (indices[i] === i) {
			i++;
		} else {
			let temp = arr[i];
			arr[i] = arr[indices[i]];
			arr[indices[i]] = temp;

			temp = indices[i];
			indices[i] = indices[indices[i]];
			indices[temp] = temp;
			console.log(arr);
			console.log(indices);
		}
	}
	return arr;
}
rearrangeItems2(a, b);
console.log(a);
