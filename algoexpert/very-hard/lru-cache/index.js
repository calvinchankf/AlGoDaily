class ListNode {
	constructor(key, val) {
		this.key = key;
		this.val = val;
		this.prev = null;
		this.next = null;
	}
}

// Do not edit the class below except for the insertKeyValuePair,
// getValueFromKey, and getMostRecentKey methods. Feel free
// to add new properties and methods to the class.
class LRUCache {
	constructor(maxSize) {
		this.maxSize = maxSize || 1;
		this.map = {};
		this.listHead = new ListNode(-1, -1);
		this.listTail = new ListNode(-1, -1);
		this.listLength = 0;
		this.listHead.next = this.listTail;
		this.listTail.prev = this.listHead;
	}

	insertKeyValuePair(key, value) {
		// Write your code here.
		let node = this.map[key];
		if (node == undefined) {
			node = new ListNode(key, value);
			this._addToTail(node);
			this.listLength++;
		} else {
			node.val = value;
			this._moveToTail(node);
		}
		this.map[key] = node;
		if (this.listLength > this.maxSize) {
			this._removeHead();
			this.listLength--;
		}
	}

	getValueFromKey(key) {
		// Write your code here.
		if (this.map[key] !== undefined) {
			this._moveToTail(this.map[key]);
			return this.map[key].val;
		}
		return null;
	}

	getMostRecentKey() {
		// Write your code here.
		if (this.listTail.prev != this.listHead) {
			return this.listTail.prev.key;
		}
		return null;
	}

	_addToTail(node) {
		let last = this.listTail.prev;
		last.next = node;
		node.prev = last;
		node.next = this.listTail;
		this.listTail.prev = node;
	}

	_moveToTail(node) {
		node.prev.next = node.next;
		node.next.prev = node.prev;
		this._addToTail(node);
	}

	_removeHead() {
		let first = this.listHead.next;
		this.listHead.next = first.next;
		first.next.prev = this.listHead;
		delete this.map[first.key];
	}
}

// Do not edit the line below.
exports.LRUCache = LRUCache;
