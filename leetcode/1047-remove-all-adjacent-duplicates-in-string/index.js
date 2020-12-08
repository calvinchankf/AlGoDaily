/*
    1st approach: stack
    - similar to parentheses problem
    - when the last item is equal to the current item, pop stack

    Time    O(N)
    Space   O(N)
    92 ms, faster than 79.96%
*/
var removeDuplicates = function(S) {
    const stack = []
    for (let c of S) {
        if (stack.length > 0 && stack[stack.length-1] == c) {
            stack.pop()
        } else {
            stack.push(c)
        }
    }
    return stack.join('')
};