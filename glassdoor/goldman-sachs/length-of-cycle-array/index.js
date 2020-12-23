/*
    https://leetcode.com/discuss/interview-question/413065

    Given an integer array of size n. Elements of the array is >= 0. Starting from arr[startInd], follow each element to the index it points to. Find a cycle and return its length. No cycle is found -> -1.

    int lengthOfCycle(int[] arr, int startIndex) {
        // todo
    }

    Examples:
    lengthOfCycle([1, 0], 0); // 2
    lengthOfCycle([1, 2, 0], 0); // 3
    lengthOfCycle([1, 2, 3, 1], 0); // 3
*/
let lengthOfCycle

/*
    1st: hashtable
    - store the { val: steps } pair in cache
    - steps - cache[val] is the length of the cycle
*/
lengthOfCycle = (arr, startIndex) => {
    const ht = {}
    let idx = startIndex
    let steps = 0
    while (idx >= 0 && idx < arr.length && arr[idx] in ht === false) {
        ht[arr[idx]] = steps
        idx = arr[idx]
        steps += 1
    }
    if (idx < 0 || idx >= arr.length || idx == arr[idx]) {
        return -1
    }
    return steps - ht[arr[idx]]
}

/*
    2nd: Floyds' Cycle
    Distance traveled by fast pointer = a+2b+c
    Distance traveled by slow pointer = a+b
    2(a+b) = a+2b+c
    a == c

    length of circle = b + c
    which is actually = b + a
    a + b <= count
*/
lengthOfCycle = (arr, startIndex) => {
    let slow = arr[startIndex]
    let fast = arr[arr[startIndex]]
    if (slow == fast) {
        return -1
    }
    let count = 1
    while (fast != slow) {
        if (fast < 0 || fast >= arr.length) {
            return -1;
        }
        count += 1
        slow = arr[slow]
        fast = arr[arr[fast]]
    }
    return count
}

let a, b

a = [1, 0]
b = 0
console.log(lengthOfCycle(a, b))

a = [1, 2, 0]
b = 0
console.log(lengthOfCycle(a, b))

a = [1, 2, 3, 1]
b = 0
console.log(lengthOfCycle(a, b))

a = [0]
b = 0
console.log(lengthOfCycle(a, b))

a = [1,2,3,4]
b = 0
console.log(lengthOfCycle(a, b))

a = [1,2,3,4]
b = -1
console.log(lengthOfCycle(a, b))

a = [1,2,3,4]
b = 4
console.log(lengthOfCycle(a, b))

a = [2,3,4,0]
b = 0
console.log(lengthOfCycle(a, b))

a = [2,3,0]
b = 0
console.log(lengthOfCycle(a, b))

console.log("-----")

/*
    2nd: Floyds' Cycle
    a = distance from start to start of the loop
    b = distance from start of loop to point where the 2 pointers meet
    c = other half of the circle

    Distance traveled by fast pointer = a+2b+c
    Distance traveled by slow pointer = a+b
    2(a+b) = a+2b+c
    a == c

    length of circle = b + c
    which is actually = b + a
    a + b <= count
*/
lengthOfCycle = (arr, startIndex) => {
    let slow = arr[startIndex]
    let fast = arr[arr[startIndex]]
    if (slow == fast) {
        return -1
    }
    let count = 1
    while (fast != slow) {
        if (fast < 0 || fast >= arr.length) {
            return -1;
        }
        count += 1
        slow = arr[slow]
        fast = arr[arr[fast]]
    }
    return count
}

a = [1, 0]
b = 0
console.log(lengthOfCycle(a, b))

a = [1, 2, 0]
b = 0
console.log(lengthOfCycle(a, b))

a = [1, 2, 3, 1]
b = 0
console.log(lengthOfCycle(a, b))

a = [0]
b = 0
console.log(lengthOfCycle(a, b))

a = [1,2,3,4]
b = 0
console.log(lengthOfCycle(a, b))

a = [1,2,3,4]
b = -1
console.log(lengthOfCycle(a, b))

a = [1,2,3,4]
b = 4
console.log(lengthOfCycle(a, b))

a = [2,3,4,0]
b = 0
console.log(lengthOfCycle(a, b))

a = [2,3,0]
b = 0
console.log(lengthOfCycle(a, b))