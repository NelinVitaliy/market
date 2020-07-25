$(document).ready(function(){
    let checkData = localStorage.getItem('checkbox');
    $(`#${checkData}`).css("color", "#81b51b");

    $(".selected-item").click(function(e){
        localStorage.setItem('checkbox', e.target.id)
    })
})




