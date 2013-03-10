function select(data, key, values) {
	return data.filter(function(itemData) {
		return values.some(function(itemValues) {
			return itemData[key]===itemValues;
		});
	});
}

var data = [
  {id:'01', name:'duffy'},
  {id:'02', name:'michey'},
  {id:'03', name:'donald'},
  {id:'04', name:'goofy'},
  {id:'05', name:'minnie'},
  {id:'06', name:'scrooge'}
];
var key = 'name';
var values = ['goofy', 'scrooge'];

select(data, key, values);