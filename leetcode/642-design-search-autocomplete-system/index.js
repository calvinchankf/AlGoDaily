class Node {
    constructor(freq = 0) {
        this.children = {}
        this.freq = freq
    }
}

class Trie {
    constructor() {
        this.root = new Node()
    }
    insert(s, freq = 1) {
        let cur = this.root
        for (let c of s) {
            if (c in cur.children == false) {
                cur.children[c] = new Node()
            }
            cur = cur.children[c]
        }
        cur.freq += freq
    }
    wordsStartWith(prefix) {
        let cur = this.root
        for (let c of prefix) {
            if (c in cur.children == false) {
                return []
            }
            cur = cur.children[c]
        }
        const res = []
        const q = [[cur, prefix]]
        while (q.length > 0) {
            const [node, curS] = q.pop(0)
            if (node.freq > 0) {
                res.push([curS, node.freq])
            }
            for (let key in node.children) {
                const child = node.children[key]
                q.push([child, curS + key])
            }
        }
        return res
    }
}

class AutocompleteSystem {
    constructor(sentences, times) {
        this.trie = new Trie()
        for (let i = 0; i < sentences.length; i++) {
            this.trie.insert(sentences[i], times[i])
        }
        this.cur = ''
    }
    input(c) {
        if (c == '#') {
            this.trie.insert(this.cur)
            this.cur = ''
            return []
        } else {
            this.cur += c
            const cands = this.trie.wordsStartWith(this.cur)
            cands.sort((a, b) => {
                if (a[1] == b[1]) {
                    return a[0] < b[0] ? -1 : 1
                }
                return b[1] - a[1]
            })
            const top3 = cands.slice(0, 3)
            return top3.map((x) => x[0])
        }
    }
}
