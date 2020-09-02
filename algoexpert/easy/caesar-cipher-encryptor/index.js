function caesarCipherEncryptor(s, key) {
	// Write your code here.
	const alphabets = "abcdefghijklmnopqrstuvwxyz";
	let res = "";
	for (let c of s) {
		let idx = c.charCodeAt() - "a".charCodeAt();
		idx = (idx + key) % 26;
		res += alphabets[idx];
	}
	return res;
}

// Do not edit the line below.
exports.caesarCipherEncryptor = caesarCipherEncryptor;
