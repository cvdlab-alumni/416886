function pushFirstNNumbers(array, n) {
	for(var i = 1; i<=n; i++) {
		array.push(i);
	}
}

function filterOddNumbers(array) {
	return array.filter(function(item) {
		return (item%2)===0;	
	})
}

function doubleEachNumber(array) {
	return array.map(function(item) {
		return item*2;
	})
}

function divisibleForFour(array) {
	return array.filter(function(item) {
		return (item%4)===0;
	})
}

function sumAll(array) {
	return array.reduce(function(prev, cur) {
		return prev+cur;
	})
}

function exercise01(array, n) {
	pushFirstNNumbers(array, n);
	var result = filterOddNumbers(array);
	result = doubleEachNumber(result);
	result = divisibleForFour(result);
	return sumAll(result);
}

exercise01([], 10);