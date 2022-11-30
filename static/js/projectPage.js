let createPopUp = $("#create-container");
let createForm = $("#create-form");
let projectInfoPopUp = $("#info-container");

$("#create-task-button").on('click', function()
{
    createPopUp.css({"display":"block"});
    $("#bg").css({"pointer-event" : "none", "filter":"blur(8px)"});
});

$("#project-id-button").on('click', function()
{
    projectInfoPopUp.css({"display" : "block"});
    $("#bg").css({"pointer-event" : "none", "filter":"blur(8px)"});
});

$(".x-button-container").on('click', function()
{
    createPopUp.css({"display" : "none"});
    projectInfoPopUp.css({"display" : "none"})
    $("#bg").css({"pointer-event" : "none", "filter":"blur(0px)"});
});

