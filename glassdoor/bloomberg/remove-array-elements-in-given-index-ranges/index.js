/*
    https://leetcode.com/discuss/interview-question/407179/Bloomberg-or-Remove-array-elements-in-given-index-ranges

    Input: 
    array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], 
    ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
    
    Output:
    [-8, 3, -5, 29, 43, 76, 73, 76]
*/
const removeItems = (nums, ranges) => {
    const intvs = mergeIntvs(ranges)
    const res = []
    for (let i = 0; i < nums.length; i++) {
        const j = bsearch(intvs, i)
        if (j >= 0 && j < intvs.length) {
            const [s, e] = intvs[j]
            if (s <= i && i <= e) {
                continue
            }
        }
        res.push(nums[i])
    }
    return res
}

const mergeIntvs = (intvs) => {
    intvs.sort((a, b) => a[0] - b[0])
    const res = []
    for (let [s, e] of intvs) {
        if (res.length > 0 && s <= res[res.length-1][1]) {
            res[res.length-1][1] = Math.max(res[res.length-1][1], e)
        } else {
            res.push([s, e])
        }
    }
    return res
}

const bsearch = (nums, target) => {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target == nums[mid][0]) {
			return mid;
		} else if (target < nums[mid][0]) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	return right
};

let a, b

a = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
b = [[5, 8], [10, 13], [3, 6], [20, 25]]
console.log(removeItems(a, b))