function identity(n) {
	var matrix = "";
	for (var i = 1; i<=n; i++) {
		for(var j = 1; j<=n; j++) {
			if (i!==j)
				matrix += 0;
			else
				matrix += 1;
			if (j<10)
				matrix += ",";
			matrix += "\t"
		}
		matrix += "\n";
	}
	return matrix;
}