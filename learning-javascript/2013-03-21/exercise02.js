function Edge(v1, v2) {
	this.v1 = v1;
	this.v2 = v2;
}

Edge.prototype.length = function() {
	return Math.sqrt(Math.pow(this.v1.x - this.v2.x, 2) + Math.pow(this.v1.y - this.v2.y, 2));
}