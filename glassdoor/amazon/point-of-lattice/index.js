/*
    ref: https://leetcode.com/discuss/interview-question/396418/
*/

/*
    findGcd(100, 40)
    
    -> 40, 100%40
    findGcd(40, 20)
    
    -> 40, 40%20
    findGcd(20, 0)

    so gcd = 20
*/
const findGcd = (a, b) => {
	if (b === 0) {
		return a;
	}
	return findGcd(b, a % b);
};

const lattice = (ax, ay, bx, by) => {
	const dx = bx - ax;
	const dy = by - ay;
	// turn right: m' = -1/m
	const turn90_x = dy;
	const turn90_y = -dx;
	/*
    given that
        turn90_y   result_y - by
        -------- = -------------
        turn90_x   result_x - bx
    if we want to find the neaest, we should find a pair of smallest_y:smallest_x which has the same ratio as turn90_y:turn90_x
        smallest_y   turn90_y   result_y - by
        ---------- = -------- = -------------
        smallest_x   turn90_x   result_x - bx
    , then
        result_y   smallest_y + by  
        -------- = ---------------
        result_x   smallest_x + bx
    */
	const gcd = Math.abs(findGcd(turn90_x, turn90_y));
	const smallest_x = turn90_x / gcd;
	const smallest_y = turn90_y / gcd;
	return [bx + smallest_x, by + smallest_y];
};

let ax = -1;
let ay = 3;
let bx = 3;
let by = 1;
console.log(lattice(ax, ay, bx, by));
