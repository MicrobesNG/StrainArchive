
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
        
        var button = $(this).parent().parent().find("button");
        
        if (button.text() == "Active") {
            
            button.text("Not Active");
            $(this).text("Activate");

        } else{

            button.text("Active");
            $(this).text("Deactivate");

        }
        
        updateStatus(userPK);

    });


});