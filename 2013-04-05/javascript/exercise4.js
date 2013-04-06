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


windows = COLOR([0,0,0])(STRUCT([(GRID([[-21,1], [-16.5-4,70.5], [-33-4,29,-6,29]]))]))

building = STRUCT([building, windows])