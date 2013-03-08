function pushNRandomNumbers(array, n) {
	for(var i = 0; i<n; i++) {
		array.push(Math.ceil(Math.random()*100));
	}
} 

function filterOddNumbers(array) {
	return array.filter(function(item) {
		return item%2 === 1;
	})
}

function sortFromSmallest(array) {
	array.sort(function(item1, item2) {
		return item1-item2;
	})
}

function exercise02(array, n) {
	pushNRandomNumbers(array, n);
	var result = filterOddNumbers(array);
	sortFromSmallest(result);
	return result;
}

exercise02([], 10);