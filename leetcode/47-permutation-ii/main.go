package main

import (
	"fmt"
	"sort"
	"strconv"
)

// naive approach
// recursively dfs all the possibilities and avoid duplicate paths by using a hashtable
// time		O(N!) -> O(N x N!)
// space	O(n!)
// beats 	7.41%
func permuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}
	hash := make(map[string]bool)
	var dfs func(arr []int, path []int, prefix string)
	dfs = func(arr []int, path []int, prefix string) {
		if len(arr) == 0 {
			if _, x := hash[prefix]; !x {
				hash[prefix] = true
				result = append(result, path)
			}
		} else {
			for i := 0; i < len(arr); i++ {
				temp := arr[i]

				copy := []int{}
				copy = append(copy, arr...)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(nextpath, temp)

				// dfs [:i]+[i+1:]
				dfs(trim, nextpath, prefix+strconv.Itoa(temp))
			}
		}
	}
	dfs(nums, []int{}, "")
	return result
}

// optimize the above naive approach
// recursively dfs all the possibilities and avoid duplicate paths by using a hashtable
/*
e.g. 2,-1,3,-1
sort it such that nums = -1,-1,2,3

compute permutations of -1(index 0)
skip computation for index 1 becos -1(index 0) has been considered
compute permutations of 2(index 2)
compute permutations of 3(index 3)
*/
// time		O(n!) worst case
// space	O(n!)
// beats 	100%
func permuteUnique1(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}

	var dfs func(arr []int, path []int)
	dfs = func(arr []int, path []int) {
		if len(arr) == 0 {
			result = append(result, path)
		} else {
			hash := make(map[int]bool)
			for i := 0; i < len(arr); i++ {

				if _, x := hash[arr[i]]; x {
					continue
				}
				hash[arr[i]] = true

				temp := arr[i]

				copy := []int{}
				copy = append(copy, arr...)
				trim := append(copy[:i], copy[i+1:]...)

				nextpath := []int{}
				nextpath = append(nextpath, path...)
				nextpath = append(nextpath, temp)

				dfs(trim, nextpath)
			}
		}
	}
	dfs(nums, []int{})
	return result
}

func main() {
	// [-1,2,-1,2,1,-1,2,1]
	fmt.Println(permuteUnique1([]int{1, 1, 2, 2}))
}
