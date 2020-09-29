/*
    2nd: another BFS approach
    - instead of BFS through the bus stops, we BFS through the bus routes

    Time    O(RRS + RR) ???
    Space   O(N)
    1080 ms, faster than 7.32%
*/
var numBusesToDestination = function (routes, S, T) {
	if (S == T) {
		return 0;
	}

	// { rid1: [stop1, stop2, stop3...], id2: [..], ... }
	const busStops = [];
	for (let i = 0; i < routes.length; i++) {
		busStops[i] = new Set(routes[i]);
	}
	// route connections { rid1: { rid2, rid3,...}, rid2: { rid1,..}... }
	const collections = [];
	for (let i = 0; i < routes.length; i++) {
		collections[i] = new Set();
	}
	// BFS on bus routes
	const q = [];
	for (let i = 0; i < routes.length; i++) {
		for (let b of routes[i]) {
			if (b == S) {
				q.push([i, 1]);
			}

			for (let j = 0; j < busStops.length; j++) {
				if (busStops[j].has(b) && i != j) {
					collections[i].add(j);
					collections[j].add(i);
				}
			}
		}
	}

	// console.log(busStops)
	// console.log(collections)
	// console.log(q)

	const seen = {};
	while (q.length > 0) {
		const [r, steps] = q.shift();
		// console.log(r, steps)
		if (r in seen) {
			continue;
		}
		seen[r] = true;
		if (busStops[r].has(T)) {
			return steps;
		}
		const nbs = collections[r];
		for (let nb of nbs) {
			q.push([nb, steps + 1]);
		}
	}

	return -1;
};
