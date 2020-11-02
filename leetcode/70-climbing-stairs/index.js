/*
    2nd approach: top-down recursive
    - use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	n for hashtable, n for recursive callstack
	72 ms, faster than 82.57%
*/
var climbStairs = function(n) {
    return dfs(n, {})
};

const dfs = (n, ht) => {
    if (n < 0) {
        return 0
    } else if (n == 0) {
        return 1
    }
    if (n in ht) {
        return ht[n]
    }
    const count = dfs(n-2, ht) + dfs(n-1, ht)
    ht[n] = count
    return count
}