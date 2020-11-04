package main

import "fmt"

/*
	questions to ask:
	- other characters? no
	- empty string? yes
	- min number of deletion = min number of addition !!!
*/

/*
	1st approach: stack
	- similar to lc1614
	1. for each add, push to stack
	2. for each close and no counterpart in stack, result++
	3. result = res + len(stack)

	Time	O(n)
	Space	O(n)
	0 ms, faster than 100.00%
*/
func minAddToMakeValid(S string) int {
	res := 0
	stack := []byte{}
	for i := 0; i < len(S); i++ {
		if S[i] == '(' {
			stack = append(stack, '(')
		} else {
			if len(stack) > 0 {
				stack = stack[1:]
			} else {
				res++
			}
		}
	}
	return res + len(stack)
}

func main() {
	fmt.Println(minAddToMakeValid(""))
	fmt.Println(minAddToMakeValid("()"))
	fmt.Println(minAddToMakeValid(")(("))
	fmt.Println(minAddToMakeValid("()((())"))
	fmt.Println(minAddToMakeValid("()))(("))
	fmt.Println(minAddToMakeValid("()())()"))
}
