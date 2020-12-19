/*
    tedious

    Time    O(N)
    Space   O(N)
    80ms
*/
var interpret = function(command) {
    let res = ''
    let i = 0
    while (i < command.length) {
        if (command[i] == 'G') {
            res += 'G'
            i += 1
        } else if (command[i] == '(') {
            if (i+1 < command.length & & command[i+1] == ')') {
                res += 'o'
                i += 2
            } else if (
                i+3 < command.length & &
                command[i+1] == 'a' & &
                command[i+2] == 'l' & &
                command[i+3] == ')'
            ) {
                res += 'al'
                i += 4
            }
        } else {
            break
        }
    }
    return res
}
