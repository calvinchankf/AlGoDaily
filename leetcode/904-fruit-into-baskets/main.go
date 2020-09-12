package main

/*
	1st approach: sliding window
	- the question is so confusing, lets rephrase the quesion:

	Given a string, find the max length of a substring which has only 2 distinct characters
	e.g. "ababacddc", return 5
	becos length of "ababa" = 5, where all other substrings are < 5
	e.g.
	length of "abab" = 4
	length of "cddc" = 4
	...

	To solve this,
	1. we can use 2 pointers to indicate the left and right
	2. if the substring btw left and right has more than 2 keys, move the left forwad until the substring has 2 keys

	Time	O(2n)
	Space	O(m) m: number of the distinct characters
	112 ms, faster than 57.89%
*/
func totalFruit(tree []int) int {
	res := 0
	left := 0
	ht := make(map[int]int)
	for i := 0; i < len(tree); i++ {
		// count fruits in the hashtable
		fruit := tree[i]
		if _, x := ht[fruit]; x {
			ht[fruit]++
		} else {
			ht[fruit] = 1
		}
		// check if len(ht) > 2, i.e. exceed the basket
		for len(ht) > 2 {
			last := left
			left++
			leftMostFruit := tree[last]
			ht[leftMostFruit]--
			if ht[leftMostFruit] == 0 {
				delete(ht, leftMostFruit)
			}
		}
		// result will be larger one
		if i-left+1 > res {
			res = i - left + 1
		}
	}
	return res
}

func main() {

}
