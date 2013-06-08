// es6

function lar_to_obj(model) {
	var v = model[0];
	var fv = model[1];

	var obj = "# List of Vertices \n";

	obj += v.map(function(vert) {
		return "v ".concat(vert.join(" "));
		}).join("\n");


	obj += "\n\n# Face Definitions\n"


	obj += fv.map(function(vert) {
		return "f ".concat(vert.join(" "));
		}).join("\n");

	return obj;
}


// example

v = [[1,2,3],[4,5,6],[7,8,9,10]];

fv = [[1,2,3,4],
		[5,6,7,8],
		[9,10,11,12],
		[13,14,15,16]];

// lar_to_obj([v,fv]);