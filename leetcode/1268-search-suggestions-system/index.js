/*
    1st: trie

    Time    O(NN)
    Space   O(N) 
    800 ms, faster than 5.18%
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

	insert = (word) => {
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

	startWith = (prefix) => {
		let cur = this.root;
		for (let c of prefix) {
			const idx = c.charCodeAt(0) - "a".charCodeAt(0);
			if (cur.children[idx] === null) {
				return [];
			}
			cur = cur.children[idx];
		}

		const res = [];
		const dfs = (node, suffix) => {
			if (node === null) {
				return;
			}
			if (node.isWord) {
				res.push(`${prefix}${suffix}`);
			}
			const alphabets = "abcdefghijklmnopqrstuvwxyz";
			for (let i = 0; i < 26; i++) {
				const child = node.children[i];
				const c = alphabets[i];
				dfs(child, `${suffix}${c}`);
			}
		};
		dfs(cur, "");
		return res;
	};
}

/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts = function (products, searchWord) {
	const trie = new Trie();
	for (let p of products) {
		trie.insert(p);
	}
	const res = [];
	let prefix = "";
	for (let c of searchWord) {
		prefix += c;
		const cands = trie.startWith(prefix);
		res.push(cands.slice(0, 3));
	}
	return res;
};

let a = ["mobile", "mouse", "moneypot", "monitor", "mousepad"];
let b = "mouse";
console.log(suggestedProducts(a, b));

console.log("-----");

/*
    1st: trie

    Time    O(NlogN)
    Space   O(N) 
    208 ms, faster than 24.64%
*/

class Node {
	constructor() {
		this.children = Array(26).fill(null);
		// this.isWord = false;
		this.arr = [];
	}
}

class Trie {
	constructor() {
		this.root = new Node();
	}

	insert = (word) => {
		let cur = this.root;
		for (let c of word) {
			const idx = c.charCodeAt(0) - "a".charCodeAt(0);
			if (cur.children[idx] === null) {
				cur.children[idx] = new Node();
			}
			cur = cur.children[idx];
			cur.arr.push(word);
		}
		// cur.isWord = true;
	};

	startWith = (prefix) => {
		let cur = this.root;
		for (let c of prefix) {
			const idx = c.charCodeAt(0) - "a".charCodeAt(0);
			if (cur.children[idx] === null) {
				return [];
			}
			cur = cur.children[idx];
		}
		return cur.arr;
	};
}

/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts = function (products, searchWord) {
	const trie = new Trie();
	for (let p of products) {
		trie.insert(p);
	}
	const res = [];
	let prefix = "";
	for (let c of searchWord) {
		prefix += c;
		const cands = trie.startWith(prefix);
		res.push(cands.sort().slice(0, 3));
	}
	return res;
};
