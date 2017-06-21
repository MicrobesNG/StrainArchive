


$(document).ready(function() {

    $(".fundingTypeOption").click(function() {
        $("#fundingTypeDropdown").val($(this).html());
        $("#fundingTypeDropdown").text($(this).html());
    });

    $("#viewSummary").click(function() {
        $("#checkoutSummaryModal").modal("show");
    });

});