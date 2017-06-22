function populateSummaryModal() {

    $("#nameFieldSummary").text($("#nameInput").val());
    $("#emailFieldSummary").text($("#emailInput").val());
    $("#fundingFieldSummary").text($("#fundingTypeDropdown").val());
    $("#billingAddressSummary").val($("#billingAddressInput").val());
    $("#deliveryAddressSummary").val($("#deliveryAddressInput").val());

}


$(document).ready(function() {

    $("#bbsrcCodeInput").prop("disabled", true);

    $(".fundingTypeOption").click(function() {
        $("#fundingTypeDropdown").val($(this).html());
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