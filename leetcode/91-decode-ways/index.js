var numDecodings = function (s) {
	const ht = {};

	const dfs = (remain) => {
		if (remain.length == 0) {
            return 1
        }
        
        if (remain in ht) {
            return ht[remain]
        }
        
        let total = 0
        
        const a = parseInt(remain[0])
        const b = parseInt(remain.slice(0, 2)) 
        
        if (a >= 1 && a <= 9) {
            total += dfs(remain.slice(1))
        }
        if (b >= 10 && b <= 26) {
            total += dfs(remain.slice(2))
        }
        
        ht[remain] = total
        return total
	};

	return dfs(s);
};
