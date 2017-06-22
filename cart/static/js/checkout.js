function populateSummaryModal() {

    $("#nameFieldSummary").text($("#nameInput").val());
    $("#emailFieldSummary").text($("#emailInput").val());
    $("#fundingFieldSummary").text($("#fundingTypeDropdown").text());

    if ($("#fundingTypeDropdown").val() == "B") {
        $("#bbrscCodeSummary").text($("#bbsrcCodeInput").val());
    } else {
        $("#bbrscCodeSummary").text("N/A");
    }
    $("#billingAddressSummary").val($("#billingAddressInput").val());
    $("#deliveryAddressSummary").val($("#deliveryAddressInput").val());

    $("#noteSummary").text($("#noteInput").val());

}

function submitBasket() {
    $("#quoteForm").submit(function() {
        
    });
}


$(document).ready(function() {

    $("#bbsrcCodeInput").prop("disabled", true);

    $(".fundingTypeOption").click(function() {
        $("#fundingTypeDropdown").val($(this).attr("id"));
        $("#fundingTypeDropdown").text($(this).html());

        if ($(this).attr("id") == "B") {
            $("#bbsrcCodeInput").prop("disabled", false);
        } else {
            $("#bbsrcCodeInput").prop("disabled", true);
        }

    });

    $("#viewSummary").click(function() {
        populateSummaryModal();
        $("#checkoutSummaryModal").modal("show");
    });

});