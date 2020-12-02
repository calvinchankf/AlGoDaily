/*
    similar to lc238
*/
function arrayOfProducts(nums) {
    // Write your code here.
      const n = nums.length
      const res = Array(n).fill(1)
      for (let i = 1; i < n; i++) {
          res[i] = nums[i-1] * res[i-1]
      }
      let p = 1
      for (let i = n - 1; i >= 0; i--) {
          res[i] *= p
          p *= nums[i]
      }
      return res
  }
  
  // Do not edit the line below.
  exports.arrayOfProducts = arrayOfProducts;
  