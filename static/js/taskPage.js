let taskMemberButton = $("#member-button");
let assignButton = $("#assign-expand-button")
let taskMemberDiv = $("#task-member-container");
let taskMemberTabOpen = $("#member-tab-open");
let searchDiv = $("#member-search-container");
let searchTabOpen = $("#search-tab-open");
let finishButton = $("#finish-button");

let inTask = $("#in-task").attr("value").split(",");
let memberLinks = $(".member-link");

console.log(inTask)
function render()
{
    
    memberLinks.each(function()
    {
        let arrowUp = $($($(this).children()[1]).children()[1]);
        var id = $(this).attr("id");
        if(inTask.includes(id))
        {
            arrowUp.removeClass("fa-arrow-up");
            arrowUp.addClass("fa-arrow-down");
            $(this).addClass("in-task");
        }
        else if(selectedMember.includes(id))
        {
            $(this).addClass("in-task");
        }
        else
        {
            $(this).removeClass("in-task")
            
        }
        
        if(deassignedMembers.includes(id))
        {
            $(this).addClass("deassign-user");
            arrowUp.addClass("fa-arrow-up");
            arrowUp.removeClass("fa-arrow-down");
        }
        else
        {
            $(this).removeClass("deassign-user");
            
        }
        
    });
}


taskMemberButton.on('click', function()
{
    if (taskMemberTabOpen[0].innerHTML == "False")
    {
        console.log("A")
        if(searchTabOpen[0].innerHTML == "True")
        {
            assignButton.click();   
        }
        taskMemberDiv.css({"left" : "calc(100% - 24rem)"});
        taskMemberTabOpen[0].innerHTML = "True"; 
    }
    else
    {
        console.log("B")
        taskMemberDiv.css({"left" : "100%"});
        taskMemberTabOpen[0].innerHTML = "False";
    }
});


assignButton.on('click', function()
{
    if(searchTabOpen[0].innerHTML == "False")
    {
        if(taskMemberTabOpen[0].innerHTML == "True")
        {
            taskMemberButton.click();
        }
        searchDiv.css({"left" : "calc(100% - 24rem)"});
        searchTabOpen[0].innerHTML = "True";
    }
    else
    {
        searchDiv.css({"left" : "100%"});
        searchTabOpen[0].innerHTML = "False";
    }
});

finishButton.on('click', function()
{
    $("#confirm-finish-container").css({"display" : "block"});
    $("#bg").css({"pointer-events" : "none", "filter":"blur(8px)", "overflow" : "hidden"});
    
});

$(".x-button-container").on('click', function()
{
    $("#bg").css({"pointer-events" : "auto", "filter":"blur(0)"});
    $("#confirm-finish-container").css({"display" : "none"});
});


$("#assign-button").on('click', function(){
    // make state in db into True
    let form = $("#assign-member-form");
    console.log($("#in-task").attr("value"))

    $("#in-task").attr("value", inTask + "," + selectedMember.join(","));
    $("#deassigned-members").attr("value", deassignedMembers.join(","));
    selectedMember=[];
    deassignedMembers=[];
    form.submit();
});


let selectedMember = []
let deassignedMembers = []
$(".assign-member-button").on('click', function()
{
    let memberLink = $(this).parent().parent();
    let id = memberLink.attr("id");
    console.log(id)
    if(selectedMember.includes(id))//deselect member
    {
        selectedMember.splice(selectedMember.indexOf(id), 1);
    }
    else
    {
        if(inTask.includes(id))//selecting a user that is already in task
        {
            //deassign the user
            if(deassignedMembers.includes(id))//if already selected for deassignment, deselect
            {
                deassignedMembers.splice(selectedMember.indexOf(id), 1);
            }
            else
            {
                deassignedMembers.push(id);
            } 

        }
        else
        {
            selectedMember.push(id);
        }
        
    }
    render();
});

$("#reset-button").on('click', function()
{
    selectedMember=[];
    deassignedMembers=[];
    render();
})


render();