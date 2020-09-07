/*
    1st: just push the items back
*/
var duplicateZeros = function (arr) {
	let i = 0;
	while (i < arr.length) {
		if (arr[i] == 0) {
			for (let j = arr.length - 1; j > i; j--) {
				arr[j] = arr[j - 1];
			}

			i += 1;
		}
		i += 1;
	}
};
