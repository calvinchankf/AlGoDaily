class Node {
    constructor() {
        this.children = {}
        this.isWord = false
    }
}

/*
    1st: trie + backtracking

    Time of search      O(N) worst case if word = "............."
    Space               O(N)
    216 ms, faster than 78.17%
*/
class WordDictionary {
    constructor() {
        this.root = new Node()
    }
    addWord(word) {
        let cur = this.root
        for (let c of word) {
            if (cur.children[c] === undefined) {
                cur.children[c] = new Node()
            }
            cur = cur.children[c]
        }
        cur.isWord = true
    }
    search(word) {
        const dfs = (s, node) => {
            if (node == null) {
                return false
            }
            if (s.length === 0) {
                return node.isWord
            }
            const c = s[0]
            const remain = s.slice(1)
            if (c === '.') {
                for (let k in node.children) {
                    if (dfs(remain, node.children[k])) {
                        return true
                    }
                }
                return false
            }
            return dfs(remain, node.children[c])
        }
        
        return dfs(word, this.root)
    }
}

/*
    2nd: trie + BFS

    Time of search      O(N) worst case if word = "............."
    Space               O(N)
    228 ms, faster than 54.76%
*/
class Node {
    constructor() {
        this.children = {}
        this.isWord = false
    }
}

class WordDictionary {
    constructor() {
        this.root = new Node()
    }
    addWord(word) {
        let cur = this.root
        for (let c of word) {
            if (c in cur.children == false) {
                cur.children[c] = new Node()
            }
            cur = cur.children[c]
        }
        cur.isWord = true
    }
    search(word) {
        const q = [[word, this.root]]
        while (q.length > 0) {
            const [s, cur] = q.shift()
            if (s.length === 0) {
                if (cur.isWord) {
                    return true
                }
                continue
            }
            const c = s[0]
            const remain = s.slice(1)
            if (c === '.') {
                for (let key in cur.children) {
                    q.push([remain, cur.children[key]])
                }
            } else if (c in cur.children) {
                q.push([remain, cur.children[c]])   
            }
        }
        return false
    }
}