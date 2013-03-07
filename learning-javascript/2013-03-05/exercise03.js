for (var i = 1; i<=10; i++) {
	var row = "";
	for(var j = 1; j<=10; j++) {
		if (i!==j)
			row += 0;
		else
			row += 1;
		if (j<10)
			row += ", ";
	}
	console.log(row);
}