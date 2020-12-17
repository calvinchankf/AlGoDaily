/*
    https://leetcode.com/discuss/interview-question/861334/
    https://leetcode.com/discuss/interview-question/394477/

    Given a 2-D String array of student-marks find the student with the highest average and output his average score. 
    If the average is in decimals, floor it down to the nearest integer.

    Example 1:

    Input:  [{"Bob","87"}, {"Mike", "35"},{"Bob", "52"}, {"Jason","35"}, {"Mike", "55"}, {"Jessica", "99"}]
    Output: 99
    Explanation: Since Jessica's average is greater than Bob's, Mike's and Jason's average.
*/
const highestAverage = (scores) => {
    const totalScoreNCount = {} // { student: [total, count] }
    for (let [student, s] of scores) {
        if (student in totalScoreNCount == false) {
            totalScoreNCount[student] = [0, 0]
        }
        totalScoreNCount[student][0] += s
        totalScoreNCount[student][1] += 1
    }
    let maxAverage = 0
    let res = null
    for (let student in totalScoreNCount) {
        const average = Math.floor(totalScoreNCount[student][0] / totalScoreNCount[student][1])
        if (average > maxAverage) {
            maxAverage = average
            res = student
        }
    }
    return {
        studuent: res,
        averageScore: maxAverage
    }
}
let a

a = [["Bob",87], ["Mike", 35],["Bob", 52], ["Jason",35], ["Mike", 55], ["Jessica", 99]]
console.log(highestAverage(a))