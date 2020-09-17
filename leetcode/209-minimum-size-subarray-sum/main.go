package main

import (
	"fmt"
	"math"
)

/*
	questions to ask:
	- will there be no subarray add up to the s?
	- will there be negative?
	- will there be s=3, nums = [1,2,3], so the ans = 1?
	- let's say if s=0, nums = [0,0,0,0,0], the ans = 1?
*/

/*
	1st approach
	- store an array for each item, find the target in the subarray
	e.g.
  	[23, 2, 4, 6, 7]
	23	25 29 35	42
			2		6	12	19
					4	10	13
							6	 7
	^		^		^	 ^	 ^
	if i-j+1 < res, res = i-j+1
	Time	O(n^2) n(n+1)/2
	Space O(n)
	2488 ms beats 5.8%
	23jan2019
*/
func minSubArrayLen(s int, nums []int) int {
	res := math.MaxInt64
	layer := []int{}
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		temp := []int{}
		for j := 0; j < len(layer); j++ {
			x := layer[j] + num
			if x >= s && i-j+1 < res {
				res = i - j + 1
			}
			temp = append(temp, x)
		}
		if num >= s {
			res = 1
		}
		temp = append(temp, num)
		layer = temp
	}
	if res == math.MaxInt64 {
		return 0
	}
	return res
}

/*
	2nd approach
	- for each item, calculate from arr[i] to arr[j], if sum >= s and j-1+1<res, res = j - 1 + 1
	Time	O(n^2)
	Space O(1)
	96 ms beats 20.29%
	23jan2019
*/
func minSubArrayLen1(s int, nums []int) int {
	res := len(nums) + 1
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			if sum >= s {
				if j-i+1 < res {
					res = j - i + 1
				}
				break
			}
		}
	}
	if res == len(nums)+1 {
		return 0
	}
	return res
}

/*
	3rd: 2 pointers
	- similar to lc3, 76
	- learned from others https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
	- fast pointer to find the next item which sum up > target
	- once each the target, move the slow pointer to the right to see if the sum persist if sum = sum - nums[slow]

	Time	O(2n)
	Space 	O(1)
	8ms ms beats 100%
	23jan2019
*/
func minSubArrayLen2(s int, nums []int) int {
	res := len(nums) + 1
	sum := 0
	slow := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
		for sum >= s {
			if i-slow+1 < res {
				res = i - slow + 1
			}
			sum -= nums[slow]
			slow++
		}
	}
	if res == len(nums)+1 {
		return 0
	}
	return res
}

func main() {
	fmt.Println(minSubArrayLen2(5, []int{2, 3, 1, 2, 4, 3}))
	fmt.Println(minSubArrayLen2(6, []int{2, 3, 1, 2, 4, 3}))
	fmt.Println(minSubArrayLen2(7, []int{2, 3, 1, 2, 4, 3}))
	fmt.Println(minSubArrayLen2(9, []int{2, 3, 1, 2, 4, 3}))
	fmt.Println(minSubArrayLen2(15, []int{1, 2, 3, 4, 5}))
}
