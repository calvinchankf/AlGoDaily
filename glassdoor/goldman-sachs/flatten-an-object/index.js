const flatten = (obj) => {
    let res = {}
    for (let key in obj) {
        const val = obj[key]
        if (val instanceof Object && Array.isArray(val) === false) {
            res = {...res, ...flatten(val)}
        } else {
            res[key] = val
        }
    }
    return res
}

let a

a = {
    a: 1,
    b: 2,
    whatever: {
        c: 3,
        whatever: {
            d: 4,
        }
    },
    e: 5
}
console.log(flatten(a))

a = {
    a: 1,
    b: 2,
    c: 3
}
console.log(flatten(a))

a = {
    a: 1,
    b: 2,
    whatever: {
        c: 3,
        whatever: {
            d: [101,102],
        }
    },
    e: 5
}
console.log(flatten(a))