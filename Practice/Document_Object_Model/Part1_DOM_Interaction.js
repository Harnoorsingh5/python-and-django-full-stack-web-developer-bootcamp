var header = document.querySelector("h1");
console.log(header);

header.style.color = "red";

function generateRandomColor(){
    var codes = '0123456789ABCDEF';
    var color = '#';
    for(var i=0; i<6; i++){
        color = color + codes[Math.floor((Math.random() * 16))];
    }
    return color;
}

function changeColor(){
    var color = generateRandomColor();
    header.style.color = color;
}

setInterval("changeColor()",100);