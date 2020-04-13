package main

import (
	"fmt"
)

// attemp 1: hash table
// O(n) with O(n) space
// beats 51.63%
func singleNumber(nums []int) int {
	hash := make(map[int]bool)
	result := 0
	for i := 0; i < len(nums); i++ {
		if !hash[nums[i]] {
			hash[nums[i]] = true
			result += nums[i]
		} else {
			result -= nums[i]
		}
	}
	return result
}

// attemp 2: math
// 2(a+b+c)-(2a+2b+c) = c
// O(n+n) with O(n) space
// beats 51.63%
func singleNumber1(nums []int) int {
	hash := make(map[int]bool)
	result := 0
	for i := 0; i < len(nums); i++ {
		if !hash[nums[i]] {
			hash[nums[i]] = true
			result += 2 * nums[i]
		}
	}
	for i := 0; i < len(nums); i++ {
		result -= nums[i]
	}
	return result
}

// attempt 3: beat operation
// use XOR: exclusive or
// A	B		XOR(^)
// F	F		F
// F	T		T
// T	F		T
// T	T		F
// beats 100%
func singleNumber2(nums []int) int {
	result := 0
	for i := 0; i < len(nums); i++ {
		result ^= nums[i]
	}
	return result
}

func main() {
	fmt.Println(singleNumber2([]int{2, 2, 1}))
	fmt.Println(singleNumber2([]int{4, 1, 2, 1, 2}))
}
