package main

import "fmt"

// dfs with not-duplicate paths
// see ./explanation.jpeg
func CoinSums(coins []int, n int) int {
	return dfs(coins, n, 0)
}

func dfs(coins []int, n int, cur int) int {
	if n == 0 {
		return 1
	} else if n < 0 {
		return 0
	}
	cnt := 0
	for i := cur; i < len(coins); i++ {
		coin := coins[i]
		cnt += dfs(coins, n-coin, i)
	}
	return cnt
}

func main() {
	a := []int{1, 2, 5, 10, 20, 50, 100, 200}
	fmt.Println(CoinSums(a, 5))
	fmt.Println(CoinSums(a, 200))
}
