/*
    1st: 2 pointers

    Time of shortest()      O(A+B)
    Space of class          O(N)
    112 ms, faster than 81.17%
*/
class WordDistance {
    constructor(words) {
        this.ht = {}
        for (let i=0; i < words.length; i++) {
            const w = words[i]
            if (w in this.ht == false) {
                this.ht[w] = []
            }
            this.ht[w].push(i)
        }
    }
    shortest(word1, word2) {
        if (word1 in this.ht == false || word2 in this.ht == false) {
            return 2**32
        }
        const A = this.ht[word1]
        const B = this.ht[word2]
        let res = 2**32
        let i = 0
        let j = 0
        while (i < A.length && j < B.length) {
            const diff = Math.abs(A[i] - B[j])
            res = Math.min(res, diff)
            if (A[i] < B[j]) {
                i += 1
            } else {
                j += 1
            }
        }
        return res
    }
}
/*
    2nd: binary search

    Time of shortest()      O(AlogB)
    Space of class          O(N)
    108 ms, faster than 89.61% 
*/
class WordDistance {
    constructor(words) {
        this.ht = {}
        for (let i=0; i < words.length; i++) {
            const w = words[i]
            if (w in this.ht == false) {
                this.ht[w] = []
            }
            this.ht[w].push(i)
        }
    }
    shortest(word1, word2) {
        if (word1 in this.ht == false || word2 in this.ht == false) {
            return 2**32
        }
        const A = this.ht[word1]
        const B = this.ht[word2]
        let res = 2**32
        for (let a of A) {
            const i = nearestBsearch(B, a)
            const b = B[i]
            if (Math.abs(a - b) < res) {
                res = Math.abs(a - b)
            }
        }
        return res 
    }
}

const nearestBsearch = (nums, target) => {
    let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target == nums[mid]) {
			return mid;
		} else if (target < nums[mid]) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	// bounds checking
	if (right < 0) {
		return 0;
	}
	if (left > nums.length - 1) {
		return nums.length - 1;
	}
	if (Math.abs(target - nums[right]) < Math.abs(target - nums[left])) {
		return right;
	}
	return left;
}

