package main

import (
	"fmt"
	"math"
)

/*
	intuitive approach: bfs
	- for each node, there are 2 options to add in the next level,
		therefore we can calculate all paths and get the min path sum

	Time	O(2^n)
	Space	O(1)
	TLE
*/

/*
	1st approach: dynamic programming
	- reuse the approach in I):leetcode 256

	mind the corner cases:
	e.g.1 []
	e.g.2 [[8]]
	e.g.3 [[8],[9]]

	Time	O(N * K^2)
	Space	O(1)
	4 ms, faster than 100.00%
*/
func minCost(costs [][]int) int {
	// cost0 := 0
	// cost1 := 0
	// cost2 := 0
	// for i := 0; i < len(costs); i++ {
	// 	// since we need to use cost<k> values, we need to store the next results with extra space
	// 	temp0 := costs[i][0] + findMin(cost1, cost2)
	// 	temp1 := costs[i][1] + findMin(cost0, cost2)
	// 	temp2 := costs[i][2] + findMin(cost0, cost1)
	// 	// set now
	// 	cost0 = temp0
	// 	cost1 = temp1
	// 	cost2 = temp2
	// }
	// return findMin(cost0, findMin(cost1, cost2))
	if len(costs) == 0 || len(costs[0]) == 0 {
		return 0
	}
	if len(costs[0]) == 1 {
		return costs[0][0]
	}
	dp := []int{}
	for i := 0; i < len(costs[0]); i++ {
		dp = append(dp, 0)
	}

	for i := 0; i < len(costs); i++ {
		temp := []int{}
		for j := 0; j < len(costs[i]); j++ {
			temp = append(temp, costs[i][j]+findMinExcept(dp, j))
		}
		dp = temp
	}
	res := findMinExcept(dp, -1)
	if res == math.MaxInt64 {
		return costs[0][0]
	}
	return res
}

func findMinExcept(nums []int, except int) int {
	res := math.MaxInt64
	for i, num := range nums {
		if i != except && num < res {
			res = num
		}
	}
	return res
}

func main() {
	// 10
	a := [][]int{
		{17, 2, 17},
		{16, 16, 5},
		{14, 3, 19},
	}
	fmt.Println(minCost(a))
	// 43
	a = [][]int{
		{5, 8, 6},
		{19, 14, 13},
		{7, 5, 12},
		{14, 15, 17},
		{3, 20, 10},
	}
	fmt.Println(minCost(a))
}
