class Node {
	constructor() {
		this.children = Array(26).fill(null);
		this.isWord = false;
	}
}
/**
 * Initialize your data structure here.
 */
var Trie = function () {
	this.root = new Node();
};

/**
 * Inserts a word into the trie.
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
	let cur = this.root;
	for (let c of word) {
		const idx = c.charCodeAt(0) - "a".charCodeAt(0);
		if (cur.children[idx] === null) {
			cur.children[idx] = new Node();
		}
		cur = cur.children[idx];
	}
	cur.isWord = true;
};

/**
 * Returns if the word is in the trie.
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
	let cur = this.root;
	for (let c of word) {
		const idx = c.charCodeAt(0) - "a".charCodeAt(0);
		if (cur.children[idx] === null) {
			return false;
		}
		cur = cur.children[idx];
	}
	return cur.isWord;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix.
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
	let cur = this.root;
	for (let c of prefix) {
		const idx = c.charCodeAt(0) - "a".charCodeAt(0);
		if (cur.children[idx] === null) {
			return false;
		}
		cur = cur.children[idx];
	}
	return true;
};

/*
    words start with prefix
*/
Trie.prototype.wordsStartsWith = function (prefix) {
	let cur = this.root;
	for (let c of prefix) {
		const idx = c.charCodeAt(0) - "a".charCodeAt(0);
		if (cur.children[idx] === null) {
			return false;
		}
		cur = cur.children[idx];
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
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Object.create(Trie).createNew()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
