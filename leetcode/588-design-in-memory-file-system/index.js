/*
    approach: trie
    - nothing special but the descrition is ambiguous

    e.g. `If it is a file path, return a list that only contains this file's name`
    - it means `return the target file only`

    Time of insert()        O(N)    N: number of folder in the path
    Time of searchFile()    O(N)
    Time of startWith()     O(N)
    Space                   O(A)    A: all folders
    100 ms, faster than 56.10%
*/
class Node {
	constructor() {
		this.children = {};
		this.content = "";
		this.isFile = false;
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
Trie.prototype.insert = function (path) {
	path = path.slice(1);
	if (path == "") {
		return this.root;
	}

	const folders = path.split("/");
	let cur = this.root;
	for (let f of folders) {
		if (cur.children[f] === undefined) {
			cur.children[f] = new Node();
		}
		cur = cur.children[f];
	}
	return cur;
};

Trie.prototype.search = function (path) {
	path = path.slice(1);
	if (path == "") {
		return this.root;
	}

	const folders = path.split("/");
	let cur = this.root;
	for (let f of folders) {
		if (cur.children[f] === undefined) {
			return null;
		}
		cur = cur.children[f];
	}
	return cur;
};

var FileSystem = function () {
	this.trie = new Trie();
};

/**
 * @param {string} path
 * @return {string[]}
 */
FileSystem.prototype.ls = function (path) {
	const f = this.trie.search(path);
	if (f == null) {
		return [];
	}
	if (f.isFile) {
		const folders = path.split("/");
		return [folders[folders.length - 1]];
	}
	const res = [];
	for (let k in f.children) {
		res.push(k);
	}
	return res.sort();
};

/**
 * @param {string} path
 * @return {void}
 */
FileSystem.prototype.mkdir = function (path) {
	this.trie.insert(path);
};

/**
 * @param {string} filePath
 * @param {string} content
 * @return {void}
 */
FileSystem.prototype.addContentToFile = function (filePath, content) {
	const f = this.trie.insert(filePath);
	f.isFile = true;
	f.content += content;
};

/**
 * @param {string} filePath
 * @return {string}
 */
FileSystem.prototype.readContentFromFile = function (filePath) {
	const f = this.trie.search(filePath);
	if (f == null) {
		return "";
	}
	return f.content;
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * var obj = Object.create(FileSystem).createNew()
 * var param_1 = obj.ls(path)
 * obj.mkdir(path)
 * obj.addContentToFile(filePath,content)
 * var param_4 = obj.readContentFromFile(filePath)
 */
