const is_B_rotation_of_A = (A, B) => {
    if (A.length !== B.length) {
        return false
    }
    const C = [...A, ...A]
    const strC = C.join(",")
    const strB = B.join(",")
    return strC.includes(strB)
}

let a, b

a = [1,2,3,4,5]
b = [3,4,5,1,2]
console.assert(is_B_rotation_of_A(a, b) == true)

a = [1,2,3,4,5]
b = [3,4,5,1,3]
console.assert(is_B_rotation_of_A(a, b) == false)

a = [1,2,3,4,5]
b = [3,4,5,1,2,2]
console.assert(is_B_rotation_of_A(a, b) == false)