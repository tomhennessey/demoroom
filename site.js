// Opens and closes collapsible content after being clicked
function openCollapsible() {
	var coll = document.getElementsByClassName("collapsible");
	var i;
	
	for (i = 0; i < coll.length; i++) {
		coll[i].addEventListener("click", function() {
			this.classList.toggle("active");
			var content = this.nextElementSibling;
			if (content.style.display === "block") {
				content.style.display = "none";
			} else {
				content.style.display = "block";
			}
		});
	}
}

// If it exists, returns _GET string in URL to populate form field
function valueFromUrl () {
	if (location.search.includes("?")) {
		var queryStr = location.search.slice(1).split("=");
		if (queryStr[1].search(/_/) != -1) {
			document.getElementById(queryStr[0]).value = queryStr[1].replace(/_/g, " ");
		}
		else if (queryStr[1].search(/%20/) != -1) {
			document.getElementById(queryStr[0]).value = queryStr[1].replace(/%20/g, " ");
		}
		else {
			document.getElementById(queryStr[0]).value = queryStr[1];
		}
	}
}

// Event listener for clicking add demo button
var demoCount = 0;
window.onload = function() {
	document.getElementById("add").addEventListener("click", addDemo);
}
	
// Adds the next field for multiple demos
function addDemo() {
	demoCount++;
	var node = document.createElement("input");
    node.type = "text";
	node.name = "demo-name" + demoCount;
	node.classList.add("demo-name");
	node.id = "demo-name" + demoCount;
	var textnode = document.createTextNode("");
	node.appendChild(textnode);
    var currentNode = document.getElementById("add-Area");
	currentNode.parentNode.insertBefore(node, currentNode);
}
