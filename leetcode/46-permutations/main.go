package main

import "fmt"

// recursive dfs
// time		O(N!) -> O(N x N!)
// space	O(N!) due to the call stack
// beats 77.21%
func permute(nums []int) [][]int {
	result := [][]int{}
	var dfs func(arr []int, path []int)
	dfs = func(arr []int, path []int) {
		if len(arr) == 0 {
			result = append(result, path)
		} else {
			for i := 0; i < len(arr); i++ {
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

// iterative insertion
//   1
//  ^ ^
//  2 2
//
//   2,1         1,2
//  ^ ^ ^       ^ ^ ^
//  3 3 3       3 3 3
// time		O(n!)
// space	O(1)
// beats 77.14%
func permute1(nums []int) [][]int {
	perms := [][]int{[]int{}}
	for i := 0; i < len(nums); i++ {
		new_perms := [][]int{}
		for j := 0; j < len(perms); j++ {
			perm := perms[j]
			for k := 0; k < len(perm)+1; k++ {

				// i really hate golang slice and concate
				cop := []int{}
				cop = append(cop, perm[:k]...)
				cop = append(cop, nums[i])
				cop = append(cop, perm[k:]...)

				new_perms = append(new_perms, cop)
			}
		}
		perms = new_perms
	}
	return perms
}

func main() {
	fmt.Println(permute([]int{1, 2, 3}))
	fmt.Println(permute1([]int{1, 2, 3}))
}
