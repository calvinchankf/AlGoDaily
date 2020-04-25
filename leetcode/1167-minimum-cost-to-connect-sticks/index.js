/*
    1st: heap

    Time    O(NlogN)
    Space   O(1)
    204 ms, faster than 31.47%
*/
class Heap {
	constructor() {
		this.arr = [];
	}

	heapify(values) {
		// O(nlogn) version
		for (let i = 0; i < values.length; i++) {
			this.heapPush(values[i]);
		}
		/*
        O(n) version
        bottom-up
        shift down from bottom to up such that we minimize the number of shift operations
        n/2 + n/8 + n/16.... = O(n)
      */
		this.arr = values;
		const n = values.length;
		for (let i = Math.floor(n / 2); i >= 0; i--) {
			this._shiftDown(i);
		}
	}

	heapPush(value) {
		this.arr.push(value);
		let curIdx = this.arr.length - 1;
		this._shiftUp(curIdx);
	}

	heapPop() {
		const temp = this.arr[0];
		this.arr[0] = this.arr[this.arr.length - 1];
		this.arr[this.arr.length - 1] = temp;
		const p = this.arr.pop();
		this._shiftDown(0);
		return p;
	}

	// used by heapify, pop
	_shiftDown(fromIdx) {
		let cur = fromIdx;
		while (cur < this.arr.length) {
			const left = cur * 2 + 1;
			const right = cur * 2 + 2;
			if (left < this.arr.length && right < this.arr.length) {
				if (
					this.arr[cur] < this.arr[left] &&
					this.arr[cur] < this.arr[right]
				) {
					break;
				} else if (this.arr[left] < this.arr[right]) {
					const temp = this.arr[cur];
					this.arr[cur] = this.arr[left];
					this.arr[left] = temp;
					cur = left;
				} else {
					const temp = this.arr[cur];
					this.arr[cur] = this.arr[right];
					this.arr[right] = temp;
					cur = right;
				}
			} else if (left < this.arr.length) {
				if (this.arr[left] < this.arr[cur]) {
					const temp = this.arr[cur];
					this.arr[cur] = this.arr[left];
					this.arr[left] = temp;
					cur = left;
				}
				break;
			} else {
				break;
			}
		}
	}

	// used by push
	_shiftUp(fromIdx) {
		let curIdx = fromIdx;
		while (curIdx > 0) {
			const parentIdx = Math.floor((curIdx - 1) / 2);
			if (this.arr[parentIdx] > this.arr[curIdx]) {
				const temp = this.arr[curIdx];
				this.arr[curIdx] = this.arr[parentIdx];
				this.arr[parentIdx] = temp;
				curIdx = parentIdx;
			} else {
				break;
			}
		}
	}
}

/**
 * @param {number[]} sticks
 * @return {number}
 */
var connectSticks = function (sticks) {
	let h = new Heap();
	h.heapify([...sticks]);
	let res = 0;
	while (h.arr.length > 1) {
		const a = h.heapPop();
		const b = h.heapPop();
		const total = a + b;
		res += total;
		h.heapPush(total);
	}
	return res;
};

/*
    2nd: upper bound binary search

    Time    O(NN) <- it was supposed to be NlogN but splice takes O(N) time
    Space   O(1)
    388 ms, faster than 22.38%
"""
*/

/**
 * @param {number[]} sticks
 * @return {number}
 */
var connectSticks = function (sticks) {
	sticks.sort((a, b) => a - b);
	let res = 0;
	while (sticks.length > 1) {
		const a = sticks.shift();
		const b = sticks.shift();
		const total = a + b;
		res += total;
		const idx = upperBsearch(sticks, total);
		sticks.splice(idx, 0, total);
	}
	return res;
};

const upperBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target >= nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};
