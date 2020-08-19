// Do not edit the class below except for the buildHeap,
// siftDown, siftUp, peek, remove, and insert methods.
// Feel free to add new properties and methods to the class.
class MinHeap {
	constructor(array) {
		this.heap = array;
		this.buildHeap(array);
	}

	buildHeap(array) {
		// Write your code here.
		const n = array.length;
		for (let i = Math.floor(n / 2); i >= 0; i--) {
			this.siftDown(i);
		}
	}

	siftDown(fromIdx) {
		// Write your code here.let cur = fromIdx
		let cur = fromIdx;
		while (cur < this.heap.length) {
			const left = cur * 2 + 1;
			const right = cur * 2 + 2;
			if (left < this.heap.length && right < this.heap.length) {
				if (
					this.heap[cur] < this.heap[left] &&
					this.heap[cur] < this.heap[right]
				) {
					break;
				} else if (this.heap[left] < this.heap[right]) {
					const temp = this.heap[cur];
					this.heap[cur] = this.heap[left];
					this.heap[left] = temp;
					cur = left;
				} else {
					const temp = this.heap[cur];
					this.heap[cur] = this.heap[right];
					this.heap[right] = temp;
					cur = right;
				}
			} else if (left < this.heap.length) {
				if (this.heap[left] < this.heap[cur]) {
					const temp = this.heap[cur];
					this.heap[cur] = this.heap[left];
					this.heap[left] = temp;
					cur = left;
				}
				break;
			} else {
				break;
			}
		}
	}

	siftUp(fromIdx) {
		// Write your code here.
		let curIdx = fromIdx;
		while (curIdx > 0) {
			const parentIdx = Math.floor((curIdx - 1) / 2);
			if (this.heap[parentIdx] > this.heap[curIdx]) {
				const temp = this.heap[curIdx];
				this.heap[curIdx] = this.heap[parentIdx];
				this.heap[parentIdx] = temp;
				curIdx = parentIdx;
			} else {
				break;
			}
		}
	}

	peek() {
		// Write your code here.
		return this.heap[0];
	}

	remove() {
		// Write your code here.
		const temp = this.heap[0];
		this.heap[0] = this.heap[this.heap.length - 1];
		this.heap[this.heap.length - 1] = temp;
		const p = this.heap.pop();
		this.siftDown(0);
		return p;
	}

	insert(value) {
		// Write your code here.
		this.heap.push(value);
		let curIdx = this.heap.length - 1;
		this.siftUp(curIdx);
	}
}

// Do not edit the line below.
exports.MinHeap = MinHeap;
