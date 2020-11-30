package main

import (
	"fmt"
	"math"
)

/*
	1st approach: sliding window

	Time	O(N)
	Space	O(1)
	124 ms, faster than 100.00%
*/
func findMaxAverage(nums []int, k int) float64 {
	if len(nums) == 0 || k < 1 {
		return 0
	}
	resSum := math.MinInt64
	windowSum := 0
	for i := 0; i < k && i < len(nums); i++ {
		windowSum += nums[i]
	}
	resSum = windowSum

	for i := k; i < len(nums); i++ {
		windowSum += nums[i] - nums[i-k]
		if windowSum > resSum {
			resSum = windowSum
		}
	}

	return float64(resSum) / float64(k)
}

func main() {
	fmt.Println(findMaxAverage([]int{1, 12, -5, -6, 50, 3}, 4))
}
