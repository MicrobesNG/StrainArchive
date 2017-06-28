



function openSendQuoteConfirmationModal(customerName) {

    var message = "By clicking confirm, you will be sending a quote via email to ";
        message += "<b>" + customerName + "</b>. ";
        message += "This cannot be undone. ";
        message += "Please check quote before sending."
    
    $("#confirmationTitle").text("Send Quote: Are You Sure?");
    $("#confirmationText").html(message)
    $("#confirmationModal").modal("show");
    
}

$(document).ready(function() {

    $(".sendQuote").click(function() {
        var selectedQuoteCustomerName = $(this).parent().parent().find(".customerCell").html();
        openSendQuoteConfirmationModal(selectedQuoteCustomerName);
    });

});