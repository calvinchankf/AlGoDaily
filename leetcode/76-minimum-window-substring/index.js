/*
    2nd approach: hashtable
    - move forward the fast pointer until the window contains "satisfies" the target
    - if the window satisfies the target, keep moving the slow pointer to find the minimum window

    e.g. string = azjskfzs, target = az

    first satisfying window
    azjskfzs
    L  R

    move slow(left) pointer to find the minimum
    azjskfzs
     L R

    now the window can not satisfy the target, gonna move the fast(right) poiner next
    azjskfzs
      LR
    
    nice, we see a satisfying window but its length is larger than the intermediate result
    azjskfzs
      L   R
    
    another satisfying window but its length is larger than the intermediate result
    azjskfzs
       L  R
    
    cannot satisfy, move fast pointer next
    azjskfzs
        L R
    
    satisfy now, move the slow pointer next
    azjskfzs
        L  R

    great, this window is satisfying and with shorter length than the intermediate result
    azjskfzs
          LR

    ref:
    - https://www.youtube.com/watch?v=eS6PZLjoaq8

    Time    O(128n) 128 ascii-characters
    Space   O(n)
    568 ms, faster than 5.01%
*/
var minWindow = function (s, t) {
	const smallHt = constructHt(t);
	let res = s;
	const curHt = {};
	let cur = "";
	let j = 0;
	for (let i = 0; i < s.length; i++) {
		const c = s[i];
		cur += c;

		if (c in curHt) {
			curHt[c] += 1;
		} else {
			curHt[c] = 1;
		}

		while (ifAContainB(curHt, smallHt)) {
			if (cur.length < res.length) {
				res = cur;
			}
			const last = s[j];
			j += 1;
			cur = cur.slice(1);
			curHt[last] -= 1;
			if (curHt[last] == 0) {
				delete curHt[last];
			}
		}
	}

	if (ifAContainB(constructHt(res), smallHt)) {
		return res;
	}
	return "";
};

var constructHt = function (s) {
	const ht = {};
	for (let c of s) {
		if (c in ht) {
			ht[c] += 1;
		} else {
			ht[c] = 1;
		}
	}
	return ht;
};

var ifAContainB = function (a, b) {
	for (let key in b) {
		if (a[key] === undefined) {
			return false;
		}
		if (a[key] < b[key]) {
			return false;
		}
	}
	return true;
};
