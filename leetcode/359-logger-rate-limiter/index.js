/*
    1st approach: hashtable

    Time    O(1)
    Space   O(n)
    204 ms, faster than 38.40%
*/
var Logger = function () {
	this.ht = {};
};

/**
 * Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. 
 * @param {number} timestamp 
 * @param {string} message
 * @return {boolean}
 */
Logger.prototype.shouldPrintMessage = function (timestamp, message) {
	if (!(message in this.ht)) {
		this.ht[message] = timestamp;
		return true;
	}
	const last = this.ht[message];
	if (timestamp - last >= 10) {
		this.ht[message] = timestamp;
		return true;
	}
	return false;
};

/**
 * Your Logger object will be instantiated and called as such:
 * var obj = new Logger()
 * var param_1 = obj.shouldPrintMessage(timestamp,message)
 */
