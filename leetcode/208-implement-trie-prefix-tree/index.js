class Node {
	constructor() {
		this.children = Array(26).fill(null);
		this.isWord = false;
	}
}
class Trie {
    constructor() {
        this.root = new Node()
    }
    insert(word) {
        let cur = this.root
        for (let c of word) {
            const i = c.charCodeAt() - 'a'.charCodeAt()
            if (cur.children[i] == null) {
                cur.children[i] = new Node()
            }
            cur = cur.children[i]
        }
        cur.isWord = true
    }
    search(word) {
        let cur = this.root
        for (let c of word) {
            const i = c.charCodeAt() - 'a'.charCodeAt()
            if (cur.children[i] == null) {
                return false
            }
            cur = cur.children[i]
        }
        return cur.isWord
    }
    startsWith(word) {
        let cur = this.root
        for (let c of word) {
            const i = c.charCodeAt() - 'a'.charCodeAt()
            if (cur.children[i] == null) {
                return false
            }
            cur = cur.children[i]
        }
        return true
    }
    /*
        followup: all the words which start with the prefix
    */
    wordsStartsWith(prefix) {
        let cur = this.root;
        for (let c of prefix) {
            const i = c.charCodeAt() - "a".charCodeAt();
            if (cur.children[i] === null) {
                return false;
            }
            cur = cur.children[i];
        }
        const alphabets = "abcdefghijklmnopqrstuvwxyz";
        const res = [];
        const dfs = (node, suffix) => {
            if (node === null) {
                return;
            }
            if (node.isWord) {
                res.push(`${prefix}${suffix}`);
            }
            for (let i = 0; i < 26; i++) {
                const child = node.children[i];
                const c = alphabets[i];
                dfs(child, `${suffix}${c}`);
            }
        };
        dfs(cur, "");
        return res;
    }
}