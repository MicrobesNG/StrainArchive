function populateQuoteDetailsModal(data) {

    console.log(data);

    $("#quoteDetailsCustomerName").text(data["customer_name"]);
    $("#quoteDetailsCustomerEmail").text(data["customer_email"]);
    $("#quoteDetailsFundingType").text(data["funding_type"]);
    if (data["bbsrc_code"] != "") {
        $("#quoteDetailsBBSRCCode").text("(" + data["bbsrc_code"] + ")");
    } else {
        $("#quoteDetailsBBSRCCode").text(data["bbsrc_code"]);
    }
    $("#quoteDetailsBillingAddress").text(data["billing_address"]);
    $("#quoteDetailsDeliveryAddress").text(data["delivery_address"]);
    $("#quoteDetailsCustomerNotes").text(data["customer_notes"]);

    for (var i = 0; i < data["basket"]["purchases"].length; i++) {

        var currentPurchase = data["basket"]["purchases"][i];
        
        var row = "<li>";
            row += currentPurchase["quantity"] + "x ";
            row += currentPurchase["strain_name"] + " - ";
            row += "£" + currentPurchase["cost"];
            row += "</li>";

        $("#basketContentList").append(row);
    }

}


function getQuoteDetails(quotePK) {
    $.ajax({
        url: "/management/getQuoteDetails/" + quotePK,
        success: function(data) {
            populateQuoteDetailsModal(data);
            $("#checkoutSummaryModal").modal("show");
        }
    });
}



$(document).ready(function() {

    $(".viewQuote").click(function() {
        getQuoteDetails($(this).parent().parent().attr("id"));
        
    });

});