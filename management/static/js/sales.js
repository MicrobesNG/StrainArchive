
// populate quote details modal with data from backend
function populateQuoteDetailsModal(data) {

    // set customer details and funding type
    $("#quoteDetailsCustomerName").text(data["customer_name"]);
    $("#quoteDetailsCustomerEmail").text(data["customer_email"]);
    $("#quoteDetailsFundingType").text(data["funding_type"]);

    // if bbsrc funding, display the bbsrc code
    if (data["bbsrc_code"] != "") {
        $("#quoteDetailsBBSRCCode").text("(" + data["bbsrc_code"] + ")");
    } else {
        $("#quoteDetailsBBSRCCode").text(data["bbsrc_code"]);
    }
    
    // display addresses
    $("#quoteDetailsBillingAddress").text(data["billing_address"]);
    $("#quoteDetailsDeliveryAddress").text(data["delivery_address"]);
    
    // display customer note if present
    $("#quoteDetailsCustomerNotes").text(data["customer_notes"]);

    // iterate over purchases and add list element for each one
    for (var i = 0; i < data["basket"]["purchases"].length; i++) {

        // get current purchase at index i
        var currentPurchase = data["basket"]["purchases"][i];
        
        // construct html for element in list
        var listElement = "<li>";
            listElement += currentPurchase["quantity"] + "x ";
            listElement += currentPurchase["strain_name"] + " - ";
            listElement += "£" + currentPurchase["cost"];
            listElement += "</li>";

        // add new list element to list
        $("#basketContentList").append(listElement);

    }

}

// send request for details of quote with pk = quotePK
function getQuoteDetails(quotePK) {
    $.ajax({
        url: "/management/getQuoteDetails/" + quotePK,
        success: function(data) {
            // populate and display quote details modal
            populateQuoteDetailsModal(data);
            $("#checkoutSummaryModal").modal("show");
        }
    });
}

// send request for details of order with pk = orderPK
function getOrderDetails(orderPK) {
    $.ajax({
        url: "/management/getOrderDetails/" + orderPK,
        success: function(data) {
            console.log(data);
        }
    });
}

// when page is ready, execute this code
$(document).ready(function() {

    // get the details for quote on button click
    $(".viewQuote").click(function() {
        getQuoteDetails($(this).parent().parent().attr("id"));    
    });

});