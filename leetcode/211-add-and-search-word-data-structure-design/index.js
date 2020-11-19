class Node {
    constructor() {
        this.children = {}
        this.isWord = false
    }
}

/*
    1st: trie + dfs

    Time of search      O(N) worst case if word = "............."
    Space               O(N)
    216 ms, faster than 78.17%
*/

/**
 * Initialize your data structure here.
 */
var WordDictionary = function() {
    this.root = new Node()
};

/**
 * Adds a word into the data structure. 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    let cur = this.root
    for (let c of word) {
        if (cur.children[c] === undefined) {
            cur.children[c] = new Node()
        }
        cur = cur.children[c]
    }
    cur.isWord = true
};

/**
 * Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
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
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */