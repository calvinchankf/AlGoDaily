/*
    1st: trie

    Time    O(NlogN + NM) M = average length of every word 
    Space   O(N)
    300 ms, faster than 40.00%
*/
class Node {
    constructor() {
        this.isLeaf = false
		this.children = {};
	}
}
class Trie {
	constructor() {
		this.root = new Node();
	}
	insert(word) {
		let cur = this.root;
		for (let c of word) {
			if (cur.children[c] === undefined) {
				cur.children[c] = new Node();
			}
            cur = cur.children[c];
            if (cur.isLeaf) {
                return false
            }
		}
        cur.isLeaf = true
        return true
	}
}
/**
 * @param {string[]} folders
 * @return {string[]}
 */
var removeSubfolders = function(folders) {
    const paths = []
    for (let f of folders) {
        const p = f.slice(1).split('/')
        paths.push(p)
    }
    paths.sort((a, b) => a.length < b.length ? -1 : 1)
    const trie = new Trie()
    const res = []
    for (let p of paths) {
        const b = trie.insert(p)
        if (b) {
            res.push('/' + p.join('/'))
        }
    }
    return res
};