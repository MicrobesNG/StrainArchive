
function updateStatus(userPK) {
    $.ajax({
        url: "/management/updateUserStatus/" + userPK,
        success: function(data) {
            if (data["status"] != "OK") {
                alert("BALLS!");
            }
        }
    });
}

$(document).ready(function() {

    $(".promoTypeOption").click(function() {
         var userPK = $(this)
            .parent()
            .parent()
            .parent()
            .parent()
            .attr("id");
        
        updateStatus(userPK);

    });


});