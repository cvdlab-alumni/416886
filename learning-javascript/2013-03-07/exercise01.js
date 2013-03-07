function identity(n) {
	for (var i = 1; i<=n; i++) {
		var row = "";
		for(var j = 1; j<=n; j++) {
			if (i!==j)
				row += 0;
			else
				row += 1;
			if (j<10)
				row += ",";
			row += "\t"
		}
		console.log(row);
	}
}