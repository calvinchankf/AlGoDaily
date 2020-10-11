package main

/*
	classic approach: Catalan Number
	- https://www.youtube.com/watch?v=YDf982Lb84o
	- https://www.youtube.com/watch?v=GgP75HAvrlY

	f(0) = 1
	f(1) = 1
	f(2) = f(1)f(0) + f(1)f(0)
	f(3) = f(2)f(0) + f(1)f(1) + f(2)f(0)
	f(4) = f(3)f(0) + f(1)f(2) + f(2)f(1) + f(3)f(0)
	f(5) = f(4)f(0) + f(1)f(3) + f(2)f(2) + f(3)f(1) + f(4)f(0)
	f(6) = f(5)f(0) + f(1)f(4) + f(2)f(3) + f(3)f(2) + f(4)f(1) + f(5)f(0)

	Time 	O(n^2) for each number, we need to iterate through the previous items and sum up the results
	Space	O(n)
	0ms beats 100%
	...
*/
func numTrees(n int) int {
	if n < 2 {
		return 1
	}
	dp := make(map[int]int)
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	f(n, dp)
	return dp[n]
}

func f(k int, dp map[int]int) int {
	if v, x := dp[k]; x {
		return v
	}
	sum := 0
	for i := 0; i < k; i++ {
		sum += f(i, dp) * f(k-i-1, dp)
	}
	dp[k] = sum
	return sum
}

func main() {

}
