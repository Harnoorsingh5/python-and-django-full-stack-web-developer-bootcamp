$('h1')
$('li')
var x = $('li')
x.css('color','red')

var header = $('h1');

var myCSS = {
    'color': 'white',
    'background': 'red',
    'border': '20px solid green'
};

header.css(myCSS);

var list = $('li');
list.eq(0).css('color', 'blue'); //eq is used to access particular element from the array of elements using index 0 to 1.
list.eq(-1).css('color', 'blue'); //last element

console.log(header.text());
$('h1').text("Jquery is good");

$('input').eq(0).css('color','green'); // changes color of text in text box
$('input').eq(1).attr('type','checkbox'); //changes type of submit button to checkbox

// We can even add CSS classes defined in html css files using jquery
$('h1').addClass('turnBlue');
$('h1').removeClass('turnBlue');

// you can use toggle class and not worry about adding and removing class
$('h1').toggleClass('turnBlue');

$('h1').click(function(){
    console.log('You Clicked h1!');
    $(this).text("I was changed!");
})

$('li').click(function(){
    console.log('You Clicked list!');
})

$('input').eq(0).keypress(function(){
    $('h3').toggleClass('turnBlue');
})

$('input').eq(0).keypress(function(event){
    if(event.which === 13){ //like ASCII code
        $('h3').toggleClass('turnBlue');
    }
})

$('h1').on('mouseenter', function(){
    $(this).toggleClass('turnBlue');
})

$('input').eq(1).on('click',function(){
    $('.container').fadeOut(3000);
})

$('input').eq(1).on('click',function(){
    $('.container').slideUp(3000);
})