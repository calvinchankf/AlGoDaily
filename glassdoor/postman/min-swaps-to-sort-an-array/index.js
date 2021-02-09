/*
    selection sort takes O(N^2) but it takes min number of swaps
*/
const f = (arr) => {
    const sorted = [...arr]
    sorted.sort((a, b) => a - b)
    let count = 0
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == sorted[i]) {
            continue
        }
        let maxJ = i
        for (let j = i+1; j < arr.length; j++) {
            if (arr[j] == sorted[i]) {
                maxJ = j
            }
        }
        [arr[i], arr[maxJ]] = [arr[maxJ], arr[i]]
        count += 1
    }
    return count
}

let a
/*
    sorted
    [1, 2, 3, 4, 4, 5, 6]
    
    orig
    [3, 4, 2, 1, 3, 5, 6]
     1        3
        2  4
           3  4
              3  4
    so the result = 4
*/
a = [3, 4, 2, 1, 3, 5, 6]
console.log(f(a))

a = [5, 1, 2, 2, 2, 2, 2, 2, 2]
console.log(f(a))