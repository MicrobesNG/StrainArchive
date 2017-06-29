
// send request for details of order with pk = orderPK
function getOrderDetails(orderPK) {
    $.ajax({
        url: "/management/getOrderDetails/" + orderPK,
        success: function(data) {

            $("#orderDetailsStatus").text(data["status"]);
            $("#orderDetailsPaymentMethod").text(data["payment_method"]);
            $("#orderDetailsCreationDate").text(data["start_date"]);
            $("#orderDetailsPostDate").text(data["post_date"]);
            $("#orderDetailsReceiveDate").text(data["received_date"]);

            $("#orderDetailsModal").modal("show");
        }
    });
}


function populateEditOrderModal() {
    
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
        populateEditOrderModal();
        $("#editOrderModal").modal("show");
    });

    $(".viewOrder").click(function() {
        getOrderDetails($(this).attr("id").replace("order_", ""));
    });

});