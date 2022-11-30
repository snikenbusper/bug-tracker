let currentTab = 0;
let tabs = $(".tab")
$("#prev-button").click(function(){switchTab(-1)});
$("#next-button").click(function(){switchTab(1)});
console.log($("#next-button")[0].onclick)


showTab(currentTab)


function showTab(index)
{
    tabs[index].style.display="block";
    if (index==0)// first tab
    {
        console.log($("#prev-button"));
        $("#prev-button")[0].style.display = "none";
    }
    else
    {
        $("#prev-button")[0].style.display = "inline";
    }

    if (index==tabs.length-1)
    {
        $('#next-button')[0].innerHTML = "Submit";
        $('#next-button')[0].type = "submit"
    }
    else
    {
        $('#next-button')[0].innerHTML = "Next";
        $('#next-button')[0].type = "button"
    }
}

function switchTab(i)
{
    if(i==1 && currentTab >= tabs.length-1)
    {
        alert("submitted")
        return;
    }
    tabs[currentTab].style.display = "none";
    currentTab += i;
    showTab(currentTab);
    console.log(currentTab)
}