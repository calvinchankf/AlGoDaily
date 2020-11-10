/*
    I dont think it is a good question
    - bad leading zeros description
    - negative sign is present while it said "You may assume there is no extra space or special characters in the input string"

    Time    O(n) n: length of the string
    Space   O(1)
    76 ms, faster than 76.33%
*/
var validIPAddress = function(IP) {
    const canBeIp4 = IP.indexOf(".")
    const canBeIp6 = IP.indexOf(":")
    if ((canBeIp4 == -1 && canBeIp6 == -1) || (canBeIp4 > -1 && canBeIp6 > -1)) {
        return 'Neither'
    }
    if (canBeIp4 > - 1) {
        const subs = IP.split('.')
        if (subs.length != 4) {
            return 'Neither'
        }
        for (let sub of subs) {
            const num = parseInt(sub)
            if (num < 0 || num > 255 || `${num}` !=  sub) {
                return 'Neither'
            }
        }
        return 'IPv4'
    }
    if (canBeIp6 > - 1) {
        const subs = IP.split(':')
        if (subs.length != 8) {
            return 'Neither'
        }
        for (let sub of subs) {
            if (sub.length == 0 || sub.length > 4) {
                return 'Neither'
            }
            for (let c of sub) {
                if ('0123456789abcdefABCDEF'.indexOf(c) == -1) {
                    return 'Neither'
                }
            }
        }
        return 'IPv6'
    }
    return 'Neither'
};