var username = ""
let profilePictureUpload = $("#profile-picture-upload-container");


$("#edit-username").on('click', function(){editUsername()});

function editUsername()
{
    username = $('#username')[0].textContent;

    $('#username').remove();

    $("#edit-username").remove();
    $('#username-div').append(
    `
    <form id="username-form" method="post" action="/profile">
        <input name=\"type\" type=\"hidden\" value=\"username\"> 
        <input name=\"username\" id=\"username-input\" value=\"${username}\">
        <div id=\"done-username\" class=\"edit-link\">Done</div>
        <div id=\"cancel-username\" class=\"edit-link\">Cancel</div>
    </form>
    `
    );
    console.log($('#done-username'));
    $('#done-username').click(function()
    {
        $("#username-form").submit();
    });
    
    $('#cancel-username').on('click', function(){cancelLink()});


}

function cancelLink()
{
    console.log($("#username-input"))
    $("#username-form").remove();
    $('#cancel-username').remove();

    $("#username-div").append("<h1 class=\"text\" id=\"username\">"+username+"</h1>")
    $("#username-div").append("<div id=\"edit-username\" class=\"edit-link\">Edit</div>")
    $("#edit-username").on('click', function(){editUsername()});
}


$("#profile-picture").on("click", function()
{
    profilePictureUpload.css({"display" : "block"});
});


let profilePictureInput = $("#profile-picture-input")[0];

profilePictureInput.onchange = function ()
{
    const [file] = $("#profile-picture-input")[0].files;
    if (file) {
        $("#profile-picture-preview")[0].src = URL.createObjectURL(file);
        let img = $("#profile-picture-preview").cropme();
        img.cropme('bind',
            {
                url:file
            });

    }

    //test
    
}

$('.x-button-container').on('click', function()
{
    $("#profile-picture-upload-container").css({"display":"none"});   
});