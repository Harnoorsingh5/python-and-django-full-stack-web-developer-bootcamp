var p = document.querySelector("p");
p.textContent = "new text"

p.innerHTML = "<strong> bold new text </strong>"

var special = document.querySelector("#special");
var a = special.querySelector("a");
a.getAttribute("href");
a.setAttribute("href","https://www.amazon.com");