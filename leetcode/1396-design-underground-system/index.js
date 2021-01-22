/*
    1st: hashtable

    Time of checkIn()           O(1)
    Time of checkOut()          O(1)
    Time of getAverageTime()    O(1)
    Space                       O(U + S^2) U: number of users, S: number of stations
    252 ms, faster than 40.32%
*/
var UndergroundSystem = function() {
    this.usersGetIn = {}
    this.travelTimeBetween = {}
    this.travelCountBetween = {}
};
UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
    this.usersGetIn[id] = [stationName, t]
};
UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    const [startStation, startTime] = this.usersGetIn[id]
    const diff = t - startTime
    const key = `${startStation},${stationName}`
    
    if (this.travelTimeBetween[key] === undefined) {
        this.travelTimeBetween[key] = 0
    }
    this.travelTimeBetween[key] += diff
    
    if (this.travelCountBetween[key] === undefined) {
        this.travelCountBetween[key] = 0
    }
    this.travelCountBetween[key] += 1
};
UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    const key = `${startStation},${endStation}`
    const totalTime = this.travelTimeBetween[key]
    const totalCount = this.travelCountBetween[key]
    return totalTime / totalCount
};

/*
    same logic using ES6 class
    260 ms, faster than 23.87%
*/
class UndergroundSystem {
    constructor() {
        this.checkIns = {} // person: [time, station]
        this.travelTimeBetween = {} // 'from, to' : total time
        this.travelCountBetween = {} // 'from, to' : total count
    }
    checkIn(id, stationName, t) {
        this.checkIns[id] = [stationName, t]
    }
    checkOut(id, stationName, t) {
        const [src, s] = this.checkIns[id]
        const travelTime = t - s
        const key = `${src}, ${stationName}`
        
        if ((key in this.travelTimeBetween) == false) {
            this.travelTimeBetween[key]  = 0
        }
        this.travelTimeBetween[key] += travelTime
        
        if ((key in this.travelCountBetween) == false) {
            this.travelCountBetween[key]  = 0
        }
        this.travelCountBetween[key] += 1
    }
    getAverageTime(startStation, endStation) {
        const key = `${startStation}, ${endStation}`
        const totalTime = this.travelTimeBetween[key]
        const totalCount = this.travelCountBetween[key]
        return totalTime / totalCount
    }
}

/*
    2nd: similar to 1st
    - group the times and counts in one hashtable

    Time of checkIn()           O(1)
    Time of checkOut()          O(1)
    Time of getAverageTime()    O(1)
    Space                       O(U + S^2) U: number of users, S: number of stations
*/
class UndergroundSystem {
    constructor() {
        this.userCheckIns = {}
        this.timesAndCounts = {} // {(s,e): [duration, count] 
    }
    checkIn(uId, stationName, t) {
        this.userCheckIns[uId] = [stationName, t]
    }
    checkOut(uId, stationName, t) {
        if (uId in this.userCheckIns == false) {
            return
        }
        const [from, startTime] =  this.userCheckIns[uId]
        const key = `${from},${stationName}`
        if (key in this.timesAndCounts == false) {
            this.timesAndCounts[key] = [0, 0]
        }
        this.timesAndCounts[key][0] += t - startTime
        this.timesAndCounts[key][1] += 1
    }
    getAverageTime(s, e) {
        const key = `${s},${e}`
        if (key in this.timesAndCounts == false) {
            return
        }
        const totalTime = this.timesAndCounts[key][0]
        const totalCount = this.timesAndCounts[key][1]
        return totalTime / totalCount
    }
}