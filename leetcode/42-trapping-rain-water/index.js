/*
    1st: min-max 2 arrays
    - similar to lc42, 135, 487, 689, 915, 1493

    Time    O(3N)
    Space   O(2N)
    92 ms, faster than 41.18%
*/
var trap = function (heights) {
	const n = heights.length;
	const forwards = Array(n).fill(0);
	let fmax = 0;
	for (let i = 0; i < n; i++) {
		fmax = Math.max(fmax, heights[i]);
		forwards[i] = fmax;
	}

	const backwards = Array(n).fill(0);
	let bmax = 0;
	for (let i = n - 1; i >= 0; i--) {
		bmax = Math.max(bmax, heights[i]);
		backwards[i] = bmax;
	}

	let res = 0;
	for (let i = 0; i < n; i++) {
		res += Math.min(forwards[i], backwards[i]) - heights[i];
	}
	return res;
};

/*
    2nd approach: optimize the 1st approach
    - calculate max from the front
    - calculate max from the end
    - the min(forward[i], backward[i]) - height[i] is the volumn of the trapping water on that cell

    ref:
    - https://www.youtube.com/watch?v=2LjNzbK2cmA

    Time    O(N)
    Space   O(N) the result array
    88 ms, faster than 70.71%
*/
var trap = function(height) {
    const n = height.length
    let leftMax = 0
    let rightMax = 0
    let left = 0
    let right = n - 1
    let res = 0
    while (left < right) {
        if (height[left] < height[right]) {
            leftMax = Math.max(leftMax, height[left])
            res += leftMax - height[left]
            left += 1
        } else {
            rightMax = Math.max(rightMax, height[right])
            res += rightMax - height[right]
            right -= 1
        }
    }
    return res
};