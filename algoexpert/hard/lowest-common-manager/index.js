/*
    1st: recursion
    - lowest common ancestor

    Time    O(N)
    Space   O(H)
*/
function getLowestCommonManager(topManager, reportOne, reportTwo) {
	// Write your code here.
	if (
		topManager === null ||
		topManager === reportOne ||
		topManager === reportTwo
	) {
		return topManager;
	}
	// const left = getLowestCommonManager()
	const nodes = [];
	for (let child of topManager.directReports) {
		const node = getLowestCommonManager(child, reportOne, reportTwo);
		if (node !== null) {
			nodes.push(node);
		}
	}
	if (nodes.length === 2) {
		return topManager;
	} else if (nodes.length === 1) {
		return nodes[0];
	}
	return null;
}

// This is an input class. Do not edit.
class OrgChart {
	constructor(name) {
		this.name = name;
		this.directReports = [];
	}
}

// Do not edit the line below.
exports.getLowestCommonManager = getLowestCommonManager;
