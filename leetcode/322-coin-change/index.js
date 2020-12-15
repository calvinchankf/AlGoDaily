/*
    1st approach: top-down dfs + hashtable

    Time    O(CA) C: number of coins, A: amount
    Space   O(A)
    168 ms, faster than 27.24%
*/
var coinChange = function(coins, amount) {
    const ht = {}
    const dfs = (_amount) => {
        if (_amount == 0) {
            return 0
        }
        if (_amount < 0) {
            return 2**32
        }
        if (_amount in ht) {
            return ht[_amount]
        }
        let minCount = 2**32
        for (let c of coins) {
            const remain = _amount - c
            const count = dfs(remain) + 1
            minCount = Math.min(minCount, count)
        }
        ht[_amount] = minCount
        return ht[_amount]
    }
    const res = dfs(amount)
    if (res == 2**32) { return -1 }
    return res
};

/*
    2nd: dp
    learned from others: bottom-up
    e.g. coins = [1,2,5], amount = 7
    f(0) = 0  so if f(100-100), it output 0+1=1
    f(1) = min(f(0)) + 1
    f(2) = min(f(1)+f(0)) + 1
    f(3) = min(f(2)+f(1)) + 1
    f(4) = min(f(3)+f(2)) + 1
    f(5) = min(f(4)+f(3)+f(0)) + 1
    f(6) = min(f(5)+f(4)+f(1)) + 1
    f(7) = min(f(6)+f(5)+f(2)) + 1
    ...

    Time    O(CA) C: number of coins, A: amount
    Space   O(A)
    152 ms, faster than 42.49%
*/
var coinChange = function (coins, amount) {
	const dp = Array(amount+1).fill(0)
    for (let i = 1; i <= amount; i++) {
        let minCount = 2**32
        for (let c of coins) {
            const remain = i - c
            if (remain >= 0) {
                minCount = Math.min(minCount, dp[remain] + 1)
            }
        }
        dp[i] = minCount
    }
    if (dp[amount] == 2**32) { return -1 }
    return dp[amount]
};
