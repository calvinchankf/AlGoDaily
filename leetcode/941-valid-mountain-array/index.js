/*
    1st: 2 pointers
    
    Time    O(N)
    Space   O(1)
    68 ms, faster than 98.31%
*/
var validMountainArray = function (A) {
	if (A.length <= 2) {
		return false;
	}
	const n = A.length;
	let i = 0;
	while (i + 1 < n && A[i + 1] > A[i]) {
		i += 1;
	}
	let j = n - 1;
	while (j - 1 >= 0 && A[j - 1] > A[j]) {
		j -= 1;
	}
	return i == j && i != 0 && j != n - 1;
};

/*
    Go forward only
    
    Time    O(N)
    Space   O(1)
*/
var validMountainArray = function(arr) {
    let peak = -1
    for (let i = 1; i < arr.length; i++) {
        if (arr[i-1] > arr[i]) {
            peak = i - 1
            break
        } else if (arr[i-1] == arr[i]) {
            return false
        }
    }
    if (peak <= 0 || peak == arr.length -1) {
        return false
    }
    for (let i = peak+1; i < arr.length; i++) {
        if (arr[i-1] < arr[i] || arr[i-1] == arr[i]) {
            return false
        }
    }
    return true
};