
// send request for details of order with pk = orderPK
function getOrderDetails(orderPK) {
    $.ajax({
        url: "/management/getOrderDetails/" + orderPK,
        success: function(data) {
            $("#orderDetailsModal").modal("show");
        }
    });
}




$(document).ready(function() {

    $(".viewOrder").click(function() {

        getOrderDetails($(this).attr("id").replace("order_", ""));

    });

});