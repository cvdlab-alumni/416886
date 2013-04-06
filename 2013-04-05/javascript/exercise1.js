T = function (dims) {
	dims = dims.map(function (v) {
		return v-1; 
	});
	return function(values){
		return function(object) {
			return object.clone().translate(dims, values);
		};
	};
}


R = function (dims) {
	dims = dims.map(function (v) {
		return v-1; 
	});
	return function(angle){
		return function(object) {
			return object.clone().rotate(dims, angle);
		};
	};
}


S = function (dims) {
	dims = dims.map(function (v) {
		return v-1; 
	});
	return function(values){
		return function(object) {
			return object.clone().scale(dims, values);
		};
	};
}


S3 = S2;
S2 = S1;
S1 = S0;

GRID = SIMPLEX_GRID;

VIEW = DRAW;


function cyl() { 
	return CYL_SURFACE([2, 33])([36, 1]);
}


// pillars0

cyl01 = T([1,2,3])([24, 18.5, 4])(cyl());

cylinders01 = STRUCT(REPLICA(5)([cyl01, T([1])([39])]));

cyl02 = T([1,2,3])([24, 93.5, 4])(cyl());

parallels02 = GRID([[-43,4,-14,4,-35,4,-35,4], [-91.5,4], [-4, 33]]);

pillars0 = STRUCT([cylinders01, cyl02, parallels02]);



// pillars1

parallels11 = GRID([[-22,4,-35,4,-35,4,-35,4,-35,4], [-16.5, 4], [-41, 33]]);

parallels12 = GRID([[-22,4,-35,4,-35,4,-74,4], [-91.5, 4], [-41, 33]]);

cyl12 = T([1,2,3])([141, 93.5, 41])(cyl());

pillars1 = STRUCT([parallels11, parallels12, cyl12]);



// pillars2

parallels21 = GRID([[-22,4,-35,4,-113,4], [-16.5, 4], [-78, 33]]);

parallels22 = GRID([[-22,4,-35,4,-35,4,-35,4,-35,4], [-91.5, 4], [-78, 33]]);

pillars2 = STRUCT([parallels21, parallels22]);



// pillars3

parallels31 = GRID([[-100,4,-74,4], [-16.5, 4], [-115, 33]]);

miniparallels32 = GRID([[-23,2,-37,2], [-92.5, 2], [-115, 33]]);

parallels32 = GRID([[-100,4,-35,4,-35,4], [-91.5, 4], [-115, 33]]);

parallel33 = GRID([[-178,4], [-108.5, 4], [-115, 33]]);

pillars3 = STRUCT([parallels31, miniparallels32, parallels32, parallel33]);





building = STRUCT([pillars0, pillars1, pillars2, pillars3]);

VIEW(building);