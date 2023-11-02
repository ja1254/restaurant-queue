function joinWaitList()
{
    let btnx = document.getElementById("Btn");
    let url = btnx.getAttribute("data-url");
    //redirect to the add page
    window.location.href = url;
}