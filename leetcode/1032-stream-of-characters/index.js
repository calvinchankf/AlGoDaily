/*
    Time    O(N) <- depends on the input. it will be fast if the tree is balanced
    Space   O(N)
    604 ms, faster than 85.00% 
*/
class Node {
	constructor() {
		this.children = Array(26).fill(null);
		this.isWord = false;
	}
}

class Trie {
	constructor() {
		this.root = new Node();
	}
	insert(word) {
		let cur = this.root;
		for (let c of word) {
			const key = c.charCodeAt(0) - "a".charCodeAt(0);
			if (cur.children[key] === null) {
				cur.children[key] = new Node();
			}
			cur = cur.children[key];
		}
		cur.isWord = true;
	}
	search(s) {
		let cur = this.root;
		for (let c of s) {
			const key = c.charCodeAt(0) - "a".charCodeAt(0);
			if (cur.children[key] === null) {
				return false;
			}
			cur = cur.children[key];
			if (cur.isWord) {
				return true;
			}
		}
		return false;
	}
}

/**
 * @param {string[]} words
 */
var StreamChecker = function (words) {
	this.trie = new Trie();
	for (let w of words) {
		const r = w.split("").reverse();
		this.trie.insert(r);
	}
	this.userInput = "";
};

/**
 * @param {character} letter
 * @return {boolean}
 */
StreamChecker.prototype.query = function (letter) {
	this.userInput = letter + this.userInput;
	const b = this.trie.search(this.userInput);
	return b;
};

/**
 * Your StreamChecker object will be instantiated and called as such:
 * var obj = new StreamChecker(words)
 * var param_1 = obj.query(letter)
 */
