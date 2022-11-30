let content = $('#bg');
let joinForm = $('#join-container');
let joinBody = $('#join-container');
let createBody = $('#create-container');
let popUp = $('#join-pop-up');
console.log(popUp[0].innerHTML)

$('#create-project').on('click', function(){
    createBody.css({"display" : "block"});
    content.css({"pointer-events" : "none", "filter" : "blur(8px)"});
});

$('#join-project').on('click', function()
{
    joinBody.css({"display" : "block"});
    content.css({"pointer-events" : "none", "filter" : "blur(8px)"});
    popUp = "True";

});

$('.x-button-container').on('click', function()
{
    popUp = "False";
    console.log("clicked")
    joinBody.css({"display":"none"});
    createBody.css({"display":"none"});
    content.css({"pointer-events" : "auto", "filter" : "blur(0px)"});
});

if($("#join-pop-up")[0].innerHTML == "True")
{
    $('#join-project').click();
}
