/*
    1st: hashtable

    Time    O(N)
    Space   O(N)
    84 ms, faster than 26.26%
*/
var findDuplicate = function (nums) {
	const ht = {};
	for (let x of nums) {
		if (x in ht) {
			return x;
		} else {
			ht[x] = true;
		}
	}
};

/*
    2nd: sort

    Time    O(NlogN)
    Space   O(1)
    76 ms, faster than 40.38% 
*/
var findDuplicate = function (nums) {
	nums.sort();
	for (let i = 1; i < nums.length; i++) {
		if (nums[i - 1] == nums[i]) {
			return nums[i];
		}
	}
	return -1;
};

/*
    3rd: 2 pointers
    - similar to lc142
    
    ref:
    - https://leetcode.com/articles/find-the-duplicate-number/

    Time    O(N)
    Space   O(1)
    68 ms, faster than 65.78% 
*/
var findDuplicate = function (nums) {
	if (nums.length === 0) {
		return -1;
	}
	let slow = nums[0];
	let fast = nums[0];
	while (true) {
		slow = nums[slow];
		fast = nums[nums[fast]];
		if (slow == fast) {
			break;
		}
	}
	// Slow or fast, both work.
	// As long as one starts from original, another one starts the meeting point
	fast = nums[0];
	while (slow != fast) {
		slow = nums[slow];
		fast = nums[fast];
	}
	return slow; // slow or fast, both work
};

let a;

a = [1, 3, 4, 2, 2];
console.log(findDuplicate(a));

a = [3, 1, 3, 4, 2];
console.log(findDuplicate(a));
