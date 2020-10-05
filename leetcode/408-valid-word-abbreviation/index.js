/*
    2nd approach: 2 pointers
    - one pointer to iterate 'word'
    - another pointer to iterate 'abbr'
    - when we see a number in abbr, move the word pointer forward with that number
    - return true if both pointers finally reach to the end

    e.g. s = internationalization, abbr = i12iz4n

    
    internationalization, i12iz4n
    ^                     ^
    i=0                   j=0

    internationalization, i12iz4n
                 ^           ^
            i=1+12=13       j=3
    
    internationalization, i12iz4n
                  ^           ^
            i=1+12=14       j=4
    
    internationalization, i12iz4n
                       ^        ^
                i=15+4=19       j=6
    
    internationalization, i12iz4n
                        ^        ^
                        end     end

    Time    O(n)
    Space   O(1)
    76 ms, faster than 81.52%
*/
var validWordAbbreviation = function (word, abbr) {
	let i = 0;
	let j = 0;
	let num = 0;
	while (i < word.length && j < abbr.length) {
		if (word[i] === abbr[j]) {
			i += 1;
			j += 1;
		} else if (!isNaN(abbr[j])) {
			if (abbr[j] == "0") {
				return false;
			}
			while (j < abbr.length && !isNaN(abbr[j])) {
				num = 10 * num + parseInt(abbr[j]);
				j += 1;
			}
			i += num;
			num = 0;
		} else {
			return false;
		}
	}
	return i == word.length && j == abbr.length;
};
