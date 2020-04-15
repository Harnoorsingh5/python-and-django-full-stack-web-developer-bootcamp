var firstName = prompt("Please Enter your first name: ");
var lastName = prompt("Please Enter your last name: ");
var age = prompt("Please Enter your age: ");
var height = prompt("Please Enter your height in centimeters: ")
var petName = prompt("Please enter name of your pet: ");

var nameFlag = false;
var ageFlag = false;
var heightFlag = false;
var petFlag = false;

if(firstName[0] === lastName[0]){
    nameFlag = true;
}else{
    nameFlag = false;
}

if(age > 20 && age < 30){
    ageFlag = true;
}else{
    ageFlag = false;
}

if(height >= 170){
    heightFlag = true;
}else{
    heightFlag = false;
}

if(petName[petName.length-1] === "y"){
    petFlag = true;
}else{
    petFlag = false;
}

if(nameFlag && ageFlag && heightFlag && petFlag){
    console.log("Congrats! you passed!");
}
else{
    console.log("Sorry you failed");
}