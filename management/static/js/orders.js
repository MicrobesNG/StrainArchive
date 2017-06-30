



// send request for details of order with pk = orderPK
function getOrderDetails(orderPK) {
    $.ajax({
        url: "/management/getOrderDetails/" + orderPK,
        success: function(data) {
            
            $("#orderDetailsCustomerName").text(data["customer_name"]);
            $("#orderDetailsCustomerEmail").text(data["customer_email"]);
            $("#orderDetailsStatus").text(data["status"]);
            $("#orderDetailsPaymentMethod").text(data["payment_method"]);
            $("#orderDetailsCreationDate").text(data["start_date"]);
            $("#orderDetailsPostDate").text(data["post_date"]);
            $("#orderDetailsReceiveDate").text(data["received_date"]);
            $("#orderDetailsDeliveryAddress").text(data["delivery_address"]);


            $("#orderDetailsCIRMS").text(data["cirms_number"]);
            $("#orderDetailsFinanceNumber").text(data["finance_reference_number"]);

            $("#paymentOrderDetailsReferenceNumber").text(data["payment_order_reference_number"]);
            $("#payment_order_filename").text(data["payment_order_pdf"]);
            $("#onlineShopOrderNumberDetails").text(data["shop_order_details"]);
            $("#onlineShopTransactionNumberDetails").text(data["shop_transaction_number"]);

            $("#editOrderIDContainer").removeClass();
            $("#editOrderIDContainer").addClass(orderPK);

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

    $(".orderStatusOption").click(function() {
        $(this).parent().parent().find("button").val($(this).attr("id"));
        $(this).parent().parent().find("button").text($(this).text());
    });

    $(".paymentMethodOption").click(function() {
        $(this).parent().parent().find("button").val($(this).attr("id"));
        $(this).parent().parent().find("button").text($(this).text());

        switch ($(this).attr("id")) {
            case "PO":
                $("#poSection").show();
                $("#osSection").hide();
                break;
            case "OS":
                $("#poSection").hide();
                $("#osSection").show();
                break;
            case "NS":
                $("#poSection").hide();
                $("#osSection").hide();
                break;
            default:
                break;
        }

    });
 
    $("#editOrder").click(function() {
        populateEditOrderModal();
        $("#editOrderModal").modal("show");
    });

    $(".viewOrder").click(function() {
        getOrderDetails($(this).attr("id").replace("order_", ""));
    });

    $("#editOrderForm").submit(function() {

        $("#id_selected_order_pk").val($("#editOrderIDContainer").attr("class"));

        $("#id_status").val($("#orderStatusDropdown_edit").val());
        $("#id_cirms_number").val($("#cirmsNumberInput").val());
        $("#id_finance_reference_number").val($("#financeReferenceNumber").val());
        $("#id_invoice_file").val($("#invoiceFileInput").val());


        var paymentMethod = $("#paymentMethodDropdown_edit").val();
        
        $("#id_payment_method").val(paymentMethod);

        if (paymentMethod == "PO") {
            $("#id_payment_order_pdf").val($("#paymentOrderFileInput").val());
            $("#id_payment_order_reference_number").val($("#paymentOrderReferenceNumber").val());
        } else if (paymentMethod == "OS") {
            $("#id_online_shop_order_number").val($("#onlineShopOrderNumber").val());
            $("#id_online_shop_transaction_number").val($("#onlineShopTransactionNumber").val());
        }

        
        
        $("#id_post_date").val($("#postageDate").val());
        $("#id_received_date").val($("#receiveDate").val());

        console.log($("#id_selected_order_pk").val());
        console.log($("#id_status").val());
        console.log($("#id_cirms_number").val());
        console.log($("#id_finance_reference_number").val());
        console.log($("#id_invoice_file").val());
        console.log($("#id_payment_method").val());
        console.log($("#id_payment_order_pdf").val());
        console.log($("#id_payment_order_reference_number").val());
        console.log($("#id_online_shop_order_number").val());
        console.log($("#id_online_shop_transaction_number").val());
        console.log($("#id_post_date").val());
        console.log($("#id_received_date").val());

        alert("L");

        
    });

});