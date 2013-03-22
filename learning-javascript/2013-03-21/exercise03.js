function Triangle(e1, e2, e3) {
	this.e1 = e1;
	this.e2 = e2;
	this.e3 = e3;
}

Triangle.prototype.perimeter = function() {
	return this.e1.length + this.e2.length + this.e3.length;
}

Triangle.prototype.area = function() {
	return Math.sqrt((this.e1.length + this.e2.length + this.e3.length)*
		(-this.e1.length + this.e2.length + this.e3.length)*
		(this.e1.length - this.e2.length + this.e3.length)*
		(this.e1.length + this.e2.length - this.e3.length))/4;
}