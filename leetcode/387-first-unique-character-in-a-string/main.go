package main

import "fmt"

/*
	1st: hashtable

	Time    O(N)
    Space   O(N)
	beats 10%
*/
func firstUniqChar(s string) int {
	hash := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		if _, ex := hash[s[i]]; !ex {
			hash[s[i]] = 1
		} else {
			hash[s[i]]++
		}
	}
	for i := 0; i < len(s); i++ {
		if v, _ := hash[s[i]]; v == 1 {
			return i
		}
	}
	return -1
}

// optimized solutin for the string that contains only a-z
// array
func firstUniqChar1(s string) int {
	history := [26]int{}
	for i := 0; i < len(s); i++ {
		history[s[i]-'a']++
	}
	for i := 0; i < len(s); i++ {
		if history[s[i]-'a'] == 1 {
			return i
		}
	}
	return -1
}

func main() {
	fmt.Println(firstUniqChar("loveleetcode"))
	fmt.Println(firstUniqChar("https://leetcode.com/problems/first-unique-character-in-a-string/"))
	fmt.Println(firstUniqChar1("loveleetcode"))
	fmt.Println(firstUniqChar1("irstuniquecharacterinastring"))
}
