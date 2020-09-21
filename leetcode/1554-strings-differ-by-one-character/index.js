/*
    1st: hashtable
    
    e.g. ["abcd","acbd", "aacd"]
    #bcd
    a#cd <- 
    ab#d
    abc#
    -----
    #cbd
    a#bd
    ac#d
    acb#
    -----
    #acd
    a#cd <- 

    Time    O(NKK)
    Space   O(NK)
    700 ms, faster than 100.00%
*/
var differByOne = function (dict) {
	const hs = new Set();
	for (let w of dict) {
		for (let i = 0; i < w.length; i++) {
			const s = w.slice(0, i) + "#" + w.slice(i + 1);
			if (hs.has(s)) {
				return true;
			}
			hs.add(s);
		}
	}
	return false;
};
