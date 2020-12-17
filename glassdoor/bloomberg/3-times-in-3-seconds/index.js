const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
/*
    https://leetcode.com/discuss/interview-question/522824/Bloomberg-or-Phone-or-New-Grad-SWE-(London)-next-round

    Write a function which returns True if called more than 3 times in 3 seconds

    Time    O(logK + K)
    Space   O(K)
*/
class ThreeTimes {
    constructor() {
        this.calls = []
    }
    click() {
        const t = new Date().getTime()
        this.calls.push(t)

        const threeSecAgo = t - 3000
        const i = upperBsearch(this.calls, threeSecAgo)
        const diff = this.calls.length - i
        
        this.calls = this.calls.slice(i)

        return diff > 3
    }
}
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
/*

    9 - 4 = 5

    0 1 2 3  4  5  6  7  8
    1,2,3,10,11,12,12,12,13
             ^

    13 - 3 = 10
*/
const f = async () => {

    let s
    
    s = new ThreeTimes()
    console.log(s.click())
    console.log(s.click())
    console.log(s.click())
    console.log(s.click())
    console.log(s.calls)
    // FFFT

    s = new ThreeTimes()
    console.log(s.click())
    console.log(s.click())
    console.log(s.click())
    console.log(s.click())
    console.log(s.click())
    await sleep(3000)
    console.log(s.click())
    console.log(s.calls)
    // FFFTTF
}
f()