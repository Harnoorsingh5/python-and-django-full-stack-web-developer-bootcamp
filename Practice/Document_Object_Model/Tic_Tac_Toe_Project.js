var squaresforXO = document.querySelectorAll("td");
var restart = document.querySelector("#restart")
console.log(squaresforXO);

function clearAllSquares(){
    for(var i=0; i<squaresforXO.length; i++){
        squaresforXO[i].textContent = '';
    }
}

function markXO(){
    if(this.textContent === ''){
        this.textContent = 'X';
    }else if(this.textContent === 'X'){
        this.textContent = 'O';
    }else{
        this.textContent = '';
    }
}

for(var i=0; i<squaresforXO.length; i++){
    squaresforXO[i].addEventListener('click', markXO);
}

restart.addEventListener('click', clearAllSquares);