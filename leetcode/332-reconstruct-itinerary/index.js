/*
    2nd approach: sort + post order traversal
    - learned from others
    - reverse the post order traversal of the nodes is the result 

    ref:
    - https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
    - https://www.youtube.com/watch?v=4udFSOWQpdg

    Time    O(ElogE)
    Space   O(E)
    68 ms, faster than 51.01% 
*/
var findItinerary = function (tickets) {
	const connections = {};
	for (let i = 0; i < tickets.length; i++) {
		const [from, to] = tickets[i];
		if (from in connections) {
			connections[from].push(to);
		} else {
			connections[from] = [to];
		}
	}
	// ['ABC', 'AAC', 'ACC'] -> 'ABC', 'AAC', 'ACC']
	for (let key in connections) {
		connections[key] = connections[key].sort((a, b) => {
			if (a === b) {
				return 0;
			}
			if (a > b) {
				return 1;
			}
			return -1;
		});
	}

	const res = [];
	const postorder = (node) => {
		while (node in connections && connections[node].length > 0) {
			const p = connections[node].shift();
			postorder(p);
		}
		res.push(node);
	};
	postorder("JFK");
	return res.reverse();
};
