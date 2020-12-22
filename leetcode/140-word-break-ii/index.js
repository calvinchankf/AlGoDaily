/*
    classic approach: bottom-up recursion + memorization
    - similar to lc131, 132, 139, 140
    - see ./idea.png

    ref:
    - https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS

    Time    O(n^2*k) Size of recursion tree can go up to n^2. The creation of list takes k time.
    Space   O(n^2*k)
    76 ms, faster than 96.35%
*/
var wordBreak = function(s, wordDict) {
    return dfs(s, wordDict, {})
};

const dfs = (s, wordDict, seen) => {
    if (s.length == 0) {
        return ['']
    }
    if (s in seen) {
        return seen[s]
    }
    const sentences = []
    for (let w of wordDict) {
        const n = w.length
        const sub = s.slice(0, n)
        if (w == sub) {
            const _sentences = dfs(s.slice(n), wordDict, seen)
            for (let _s of _sentences) {
                const temp = `${sub} ${_s}`.trim()
                sentences.push(temp)
            }
        }
    }
    seen[s] = sentences
    return seen[s]
}
