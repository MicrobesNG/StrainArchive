function populateSummaryModal() {

    $("#nameFieldSummary").text($("#nameInput").val());
    $("#emailFieldSummary").text($("#emailInput").val());
    $("#fundingFieldSummary").text($("#fundingTypeDropdown").val());
    $("#billingAddressSummary").val($("#billingAddressInput").val());
    $("#deliveryAddressSummary").val($("#deliveryAddressInput").val());

}


$(document).ready(function() {

    $(".fundingTypeOption").click(function() {
        $("#fundingTypeDropdown").val($(this).html());
        $("#fundingTypeDropdown").text($(this).html());
    });

    $("#viewSummary").click(function() {
        populateSummaryModal();
        $("#checkoutSummaryModal").modal("show");
    });

});