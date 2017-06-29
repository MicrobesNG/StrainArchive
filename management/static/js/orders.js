
// send request for details of order with pk = orderPK
function getOrderDetails(orderPK) {
    $.ajax({
        url: "/management/getOrderDetails/" + orderPK,
        success: function(data) {
            $("#orderDetailsModal").modal("show");
        }
    });
}


function populateEditOrdermodal() {
    
    $("#orderStatusDropdown").val($("#orderDetailsStatus").attr("class"));
    $("#orderStatusDropdown").text($("#orderDetailsStatus").text());

    $("#paymentMethodDropdown").val($("#orderDetailsPaymentMethod").attr("class"));
    $("#paymentMethodDropdown").text($("#orderDetailsPaymentMethod").text());

    if ($("#orderDetailsPostDate") != "") {
        $("#postageDate").val($("#orderDetailsPostDate").val());
    }

    if ($("#orderDetailsReceiveDate") != "") {
        $("#reveiveDate").val($("#orderDetailsReceiveDate").val());
    }

}




$(document).ready(function() {

    $("#editOrder").click(function() {
        $("#editOrderModal").modal("show");
    });

    $(".viewOrder").click(function() {

        getOrderDetails($(this).attr("id").replace("order_", ""));

    });

});