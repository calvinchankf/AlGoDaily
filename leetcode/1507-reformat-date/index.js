/*
    1st: string?

    Time    O(N)
    Space   O(N)
    76 ms, faster than 100.00% 
*/
var reformatDate = function (date) {
	const dayMap = {
		"1st": "1",
		"2nd": "2",
		"3rd": "3",
	};

	const monthMap = {
		Jan: "01",
		Feb: "02",
		Mar: "03",
		Apr: "04",
		May: "05",
		Jun: "06",
		Jul: "07",
		Aug: "08",
		Sep: "09",
		Oct: "10",
		Nov: "11",
		Dec: "12",
	};

	const [day, month, year] = date.split(" ");

	let resultDay = "";
	const n = day.length;
	const dayPreffix = day.slice(0, n - 3);
	const daySuffix = day.slice(n - 3);
	if (daySuffix in dayMap) {
		resultDay = `${dayPreffix}${dayMap[daySuffix]}`;
	} else {
		resultDay = day.slice(0, n - 2);
	}
	if (resultDay.length == 1) {
		resultDay = `0${resultDay}`;
	}
	return `${year}-${monthMap[month]}-${resultDay}`;
};
