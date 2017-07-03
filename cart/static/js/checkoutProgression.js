
var CHECKOUT_FRAMES = [
    "paymentDetailsTab",
    "addressTab",
    "promotionsTab",
    "notesTab"
];

function validatePaymentDetails() {

    return true;

}


$(document).ready(function() {

    $(".nextButton").click(function() {
        if (validatePaymentDetails) {
            var nextId = $(this).parents('.tab-pane').next().attr("id");
            $('[href="#'+nextId+'"]').tab('show');
        } else {
            // display an error modal
        }

    });

});