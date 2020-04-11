/*
    Codility. Software Engineer

    Jack plays a game of battleships with his friend Stacy. The game is played on a square map of N
    rows, numbered from 1 to N. Each row contains N cells, labeled with consecutive English upper-case
    letters (A, B, C, etc.). Each cell is identified by a string composed of its row number followed by its
    column number: for example, "9C" denotes the third cell in the 9th row, and "15D" denotes the
    fourth cell in the 15th row.
    
    Jack marks the positions of all his ships on the map (which is not shown to Stacy). Ships are defined
    by rectangles with a maximum area of 4 cells. Stacy picks map cells to hit some ships. A ship is
    considered to be hit if at least one of its constituent cells is hit. If all of a ship's cells are hit, 
    the ship is sunk.
    
    The goal is to count the number of sunk ships and the number of ships that have been hit but not sunk.
    
    Example 1:
    N = 4, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A"
    ./eg1.png
    ./eg1_result.png
    return (1, 1)

    Example 2: 
    N = 3, S = "1A 1B,2C 2C" and T = "1B"
    ./eg2.png
    return (0, 1)

    ref: https://leetcode.com/discuss/interview-question/538068/
*/

// 10C -> [9, 2]
const symbolToCoor = (symbol) => {
	const n = symbol.length;
	const row = parseInt(symbol.substring(0, n - 1)) - 1;
	const col = symbol[n - 1].charCodeAt(0) - 65;
	return [row, col];
};

const zombieInMatrix = (N, S, T) => {
	const coorMapToShip = {};
	const shipAreas = {};

	const shipsStrs = S.split(",");
	shipsStrs.forEach((shipsStr, idx) => {
		const [top_left, bottom_right] = shipsStr.split(" ");
		const [top, left] = symbolToCoor(top_left);
		const [bottpm, right] = symbolToCoor(bottom_right);
		for (let i = top; i <= bottpm; i++) {
			for (let j = left; j <= right; j++) {
				const key = i + "," + j;
				coorMapToShip[key] = idx;
				if (shipAreas[idx] === undefined) {
					shipAreas[idx] = 1;
				} else {
					shipAreas[idx] += 1;
				}
			}
		}
	});

	const shipAreasFuture = { ...shipAreas };

	console.log(coorMapToShip);
	console.log(shipAreas);
	console.log(shipAreasFuture);

	const hits_str = T.split(" ");
	hits_str.forEach((symbol) => {
		const [i, j] = symbolToCoor(symbol);
		const key = i + "," + j;
		if (coorMapToShip[key] !== undefined) {
			const ship = coorMapToShip[key];
			shipAreasFuture[ship] -= 1;
		}
	});

	console.log(shipAreasFuture);

	let destroyed = 0;
	let damaged = 0;
	for (const key in shipAreas) {
		const area = shipAreas[key];
		const areaFuture = shipAreasFuture[key];
		if (area > areaFuture && areaFuture > 0) {
			damaged += 1;
		} else if (areaFuture == 0) {
			destroyed += 1;
		}
	}

	return `${destroyed},${damaged}`;
};

// return 1,1
N = 4;
S = "1B 2C,2D 4D";
T = "2B 2D 3D 4D 4A";
console.log(zombieInMatrix(N, S, T));

// return 0,1
N = 3;
S = "1A 1B,2C 2C";
T = "1B";
console.log(zombieInMatrix(N, S, T));

// 1,0
N = 12;
S = "1A 2A,12A 12A";
T = "12A";
console.log(zombieInMatrix(N, S, T));
