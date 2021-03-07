/**
 * @param {string} S
 * @return {string[]}
 */
var letterCasePermutation = function (S) {
	const res = []
    const dfs = (s, cur) => {
        if (s.length == 0) {
            return res.push(cur)
        }
        const c = s[0]
        const remain = s.slice(1)
        if ('0123456789'.indexOf(c) > -1) {
            dfs(remain, cur + c)
        } else {
            dfs(remain, cur + c.toLowerCase())
            dfs(remain, cur + c.toUpperCase())
        }
    }
    dfs(S, '')
    return res
};
