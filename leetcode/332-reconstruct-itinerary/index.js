/*
    1st approach: backtracking
    - create a graph
    - recursively consume an edge and try all remaining possibilties, remove the edge b4 we go into the next recursion
    - after a recursion is done(and fail), add back the edge and try consume another edge

    Time    O(E^F) E: edge, F: flight
    Space   O(h)
    112 ms, faster than 35.40%
*/
var findItinerary = function(tickets) {
    let res = null
    const graph = {}
    for (let [from, to] of tickets) {
        if (from in graph == false) {
            graph[from] = []
        }
        graph[from].push(to)
    }
    for (let key in graph) {
        graph[key].sort()
    }
    const backtracking = (graph, path) => {
        if (Object.keys(graph) == 0) {
            res = path
            return true
        }
        const node = path[path.length-1]
        if (node in graph == false) {
            return false
        }
        for (let i = 0; i < graph[node].length; i++) {
            const x = graph[node][i]
            graph[node].splice(i, 1)
            if (graph[node].length == 0) {
                delete graph[node]
            }
            
            if (backtracking(graph, path.concat([x]))) {
                return true
            }
            
            if (node in graph == false) {
                graph[node] = []
            }
            graph[node].splice(i, 0, x)
        }
        return false
    }
    backtracking(graph, ['JFK'])
    
    return res
};
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
