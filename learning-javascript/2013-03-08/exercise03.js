function capitalizeWord(word) {
	var char = word.charAt(0);
	var rest = word.slice(1);
	return char.toUpperCase().concat(rest);
}

function capitalizeText(text) {
	return text.split(" ").map(function(item) {
		return capitalizeWord(item);
	}).join(" ");
}

capitalizeText("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.");