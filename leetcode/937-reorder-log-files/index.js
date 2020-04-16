/*
    1st: sort tediously

    Time    O(nlogn)
    Space   O(n)
    68 ms, faster than 57.10%
*/

/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function (logs) {
	const digitLogs = [];
	const letterLogs = [];
	for (let log of logs) {
		const messages = log.split(" ");
		if (/^\d+$/.test(messages[1])) {
			digitLogs.push(log);
		} else {
			letterLogs.push(log);
		}
	}
	letterLogs.sort((a, b) => {
		const idx0 = a.indexOf(" ");
		const idx1 = b.indexOf(" ");
		const aMessage0 = a.slice(0, idx0);
		const aMessage1 = a.slice(idx0, a.length);
		const bMessage0 = b.slice(0, idx1);
		const bMessage1 = b.slice(idx1, b.length);
		if (aMessage1 == bMessage1) {
			return aMessage0 > bMessage0 ? 1 : -1;
		}
		return aMessage1 > bMessage1 ? 1 : -1;
	});
	return [...letterLogs, ...digitLogs];
};
