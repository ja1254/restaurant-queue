function joinWaitList()
{
    let btnx = document.getElementById("Btn");

    //redirect to the add page
    window.location.href = "{% url 'queueforRestaurant:add_to_queue' %}";
}