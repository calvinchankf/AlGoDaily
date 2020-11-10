/**
 * // This is the FontInfo's API interface.
 * // You should not implement it, or speculate about its implementation
 * function FontInfo() {
 *
 *		@param {number} fontSize
 *		@param {char} ch
 *     	@return {number}
 *     	this.getWidth = function(fontSize, ch) {
 *      	...
 *     	};
 *
 *		@param {number} fontSize
 *     	@return {number}
 *     	this.getHeight = function(fontSize) {
 *      	...
 *     	};
 * };
 */


/*
    1st: upper bound binary search
    - similar to lc778, 875, 1011, 1283, 1482, 1617

    Time    O(NlogF)
    Space   O(1)
    104 ms, faster than 100.00%
*/
var maxFont = function(text, w, h, fonts, fontInfo) {
    let left = 0
    let right = fonts.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        
        const [_w, _h] = getDimension(text, fonts[mid], fontInfo)
        
        if (_w <= w && _h <= h) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    if (right-1 >= 0 && right-1 < fonts.length) {
        return fonts[right-1]
    }
    return -1
};

const getDimension = (text, font, fontInfo) => {
    let w = 0
    let h = fontInfo.getHeight(font)
    for (let c of text) {
        w += fontInfo.getWidth(font, c)
    }
    return [w, h]
}