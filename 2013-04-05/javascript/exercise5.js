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


// ramp1
step2D = SIMPLICIAL_COMPLEX([[0,0], [0,3.7], [5,3.7], [5,1.85]])([[0,1,2,3]]);
step3D = EXTRUDE([17])(step2D);

step3D = MAP([S1,S3,S2])(step3D);

ramp = STRUCT(REPLICA(10)([step3D, T([1,3])([5,3.7])]));

ramp1 = T([1,2,3])([38.5, 95.5, 4])(ramp);



// ramp2
step2D = SIMPLICIAL_COMPLEX([[0,0], [0,3.7], [5,3.7], [5,1.85]])([[0,1,2,3]]);
step3D = EXTRUDE([17])(step2D);

step3D = MAP([S1,S3,S2])(step3D);

ramp = STRUCT(REPLICA(10)([step3D, T([1,3])([5,3.7])]));

ramp2 = T([1,2,3])([38.5, 95.5, 41])(ramp);


// ramp3
step2D = SIMPLICIAL_COMPLEX([[0,0], [0,3.7], [5,3.7], [5,1.85]])([[0,1,2,3]]);
step3D = EXTRUDE([17])(step2D);

step3D = MAP([S1,S3,S2])(step3D);

ramp = STRUCT(REPLICA(10)([step3D, T([1,3])([5,3.7])]));

ramp3 = T([1,2,3])([88.5, 95.5, 78])(ramp);

VIEW(STRUCT([building, ramp1, ramp2, ramp3]));