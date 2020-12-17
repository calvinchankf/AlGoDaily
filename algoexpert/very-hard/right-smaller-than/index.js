/*
    1st: binary search
    - maintain a sorted array A
    - use lowerBsearch to get the number of elements smaller than x
    - use upperBsearch to insert x to A

    Time    O(N(logN+K)) worst O(N^2)
    Space   O(N)
*/
function rightSmallerThan(array) {
    const n = array.length
      const res = Array(n).fill(0)
      const sorted = []
      for (let i = n - 1; i >= 0; i--) {
              const x = array[i]
              const j = _lowerBsearch(sorted, x)
              res[i] = j
              const k = _upperBsearch(sorted, x)
              sorted.splice(k, 0, x)
      }
      return res
}

const _lowerBsearch = (nums, target) => {
      let left = 0;
      let right = nums.length;
      while (left < right) {
              const mid = Math.floor((left + right) / 2);
              if (target <= nums[mid]) {
                      right = mid;
              } else {
                      left = mid + 1;
              }
      }
      return left;
};

const _upperBsearch = (nums, target) => {
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
}

// Do not edit the line below.
exports.rightSmallerThan = rightSmallerThan;
