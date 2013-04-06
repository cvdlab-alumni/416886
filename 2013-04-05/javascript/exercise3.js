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


// nord
nord = STRUCT([GRID([[-182,2], [-25.5,91], [-36,19,-14,19,-14,19,-14,17]]), 
	GRID([[-182,2], [-25.5,13,-74,4], [-36,-19,14,-19,14,-19,14]]),
	GRID([[-182,2], [-18.5,7], [-36,4,-36,4,-30,4,-34,4]]),
	GRID([[-182,2], [-18.5,3], [-36,-4,36,-4,30,-4,34]])])


// sud
sud = STRUCT([GRID([[-20,2], [-16.5,98.5], [-33,4,-29,6,-29,16,-16,20.5]]),
	GRID([[-20,2], [-16.5,4], [-33,4+29+6+29+16+16+20.5]]),
	GRID([[-20,2], [-16.5-4-70.5,4,-15,5], [-37,29]]), 
	GRID([[-20,2], [-16.5-4-70.5,24], [-33-4-29,6+29+16]]),
	GRID([[-20,2], [-16.5-4-70.5,2,-11,11], [-33-4-29-6-29-16,16]])])



// east
east = STRUCT([GRID([[-22,161], [-16.5,2], [-33,19,-14,19,-14,19,-14,22]]),
	GRID([[-22,83,-35,43], [-16.5,2], [-33-19,14,-19,14]]),
	GRID([[-22-83-35,43], [-16.5,2], [-33-19-14-19-14-19,14]])])


// west
west = STRUCT([GRID([[-22,161], [-112.5,2], [-33,19,-14,87]]), 
	GRID([[-22,136], [-112.5,2], [33]]),
	GRID([[-22,89,-36,36], [-112.5,2], [-33-19,14]])])


building = STRUCT([nord, sud, east, west, building])
