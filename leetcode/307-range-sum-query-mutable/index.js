/*
    2nd approach: Binary Indexed Tree(Fenwick Tree)

    ref:
    - https://www.youtube.com/playlist?list=PLDV1Zeh2NRsCvoyP-bztk6uXAYoyZg_U9
    - https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
    - https://www.youtube.com/watch?v=uSFzHCZ4E-8

    2's complement binary representation for negative numbers
    - youtube.com/watch?v=4qH4unVtJkE&vl=en

    Time of build   O(n)
    Time of update  O(logn)
    Time of query   O(logn)
    Space           O(n)
    224ms beats 40.96%
*/

/**
 * @param {number[]} nums
 */
var NumArray = function (nums) {
	this.nums = nums;
	this.fenwickTree = Array(nums.length + 1).fill(0);

	for (let i = 0; i < nums.length; i++) {
		this._build(i, nums[i]);
	}
};

NumArray.prototype._buildTree = function (i, val) {
	let k = i + 1;
	while (k < this.fenwickTree.length) {
		this.fenwickTree[k] += val;
		k += k & -k;
	}
};

NumArray.prototype._getSum = function (i, val) {
	let s = 0;
	let k = i + 1;
	while (k > 0) {
		s += this.fenwickTree[k];
		k -= k & -k;
	}
	return s;
};

/**
 * @param {number} i
 * @param {number} val
 * @return {void}
 */
NumArray.prototype.update = function (i, val) {
	this._buildTree(i, val - this.nums[i]);
	// remember to update the value at this.nums[i]
	this.nums[i] = val;
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function (i, j) {
	return this._getSum(j) - this._getSum(i - 1);
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(i,val)
 * var param_2 = obj.sumRange(i,j)
 */
