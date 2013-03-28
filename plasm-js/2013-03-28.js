// un rettangolo diviso in 32 
var domain2 = DOMAIN([[0,PI], [0,1]])([32, 2]);
DRAW(SKELETON(1)(domain2);

var domain = DOMAIN([[0,10]])([10]); // dominio da 0 a 10 diviso in 10 intervalli
var mapping = function(v) {
	return [v[0], v[0]];
};

var model = MAP(mapping)(domain); // bisettrice primo terzo quadrante

// ora in 3D
var mappings = [];

//per le x
mappings[0] = function(v) {
	return [v[0]];
};

//per le y
mappings[1] = function(v) {
	return [v[0]];
};

// per le z
mappings[2] = function(v) {
	return [v[0]]; 
};

var model1 = MAP(mappings)(domain);


// circonferenza
var domain = DOMAIN([[0, 2*PI]])([36]);

var x = function(v) {
	return [COS(v[0])];
};

var y = function(v) {
	return [SIN(v[0])];
};

var mappings = [x, y];
var cerchio = MAP(mappings)(domain);

