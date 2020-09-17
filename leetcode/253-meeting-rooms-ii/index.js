/*
    1st approach
    - sort the array
    - create an array to store the end time of the latest meeting in every room
    - each interval, compare the last meeting(since sorted) amongst the meeting in the meeting rooms
    - if there is no collision, put the meeting in that room, else create a new meeting room for the interval

    Time		O(NlogN)    sort
    Space 	    O(N)	    result array
    104 ms, faster than 35.74%
*/
var minMeetingRooms = function (intervals) {
	if (intervals.length === 0) {
		return 0;
	}
	// sort
	intervals.sort((a, b) => {
		if (a[0] === b[0]) {
			return a[1] - b[1];
		}
		return a[0] - b[0];
	});
	// rooms only store the end time of the latest meeting in every room
	const rooms = [];
	// iterate through the intervals
	for (let i = 1; i < intervals.length; i++) {
		const [s, e] = intervals[i];
		// look for a vacancy from the existing rooms
		let foundRoom = false;
		for (let j = 0; j < rooms.length; j++) {
			if (rooms[j] <= s) {
				rooms[j] = e;
				foundRoom = true;
				break;
			}
		}
		// add a room if no vacancy
		if (!foundRoom) {
			rooms.push(e);
		}
	}
	return rooms.length;
};
