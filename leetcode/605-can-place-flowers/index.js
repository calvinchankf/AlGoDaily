/*
    brute force

    Time    O(N)
    Space   O(1)
    76 ms beats 95.11%
*/
var canPlaceFlowers = function(flowerbed, n) {
    const N = flowerbed.length
    let count = 0
    for (let i = 0; i < N; i++) {
        if (i == 0 && i == N - 1) {
            if (flowerbed[i] == 0) {
                count += 1
                flowerbed[i] = 1
            }
        } else if (i == 0) {
            if (flowerbed[i] == 0 && i + 1 < N && flowerbed[i+1] == 0) {
                count += 1
                flowerbed[i] = 1
            }
        } else if (i == N - 1) {
            if (flowerbed[i] == 0 && i-1 >= 0 && flowerbed[i-1] == 0) {
                count += 1
                flowerbed[i] = 1
            }
        } else {
            if (flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0) {
                count += 1
                flowerbed[i] = 1
            }
        }
    }
    return count >= n
};