function populateSummaryModal() {

    $("#nameFieldSummary").text($("#nameInput").val());
    $("#emailFieldSummary").text($("#emailInput").val());
    $("#fundingFieldSummary").text($("#fundingTypeDropdown").text());

    if ($("#fundingTypeDropdown").val() == "B") {
        alert($("#bbsrcCodeInput").val());
        $("#bbsrcCodeSummary").text($("#bbsrcCodeInput").val());
    } else {
        $("#bbsrcCodeSummary").text("N/A");
    }
    $("#billingAddressSummary").val($("#billingAddressInput").val());
    $("#deliveryAddressSummary").val($("#deliveryAddressInput").val());

    $("#noteSummary").text($("#noteInput").val());

}

function submitBasket() {

        $("#id_customer_name").val($("#nameInput").val());
        $("#id_email").val($("#emailInput").val());
        $("#id_billing_address").val($("#billingAddressInput").val());
        $("#id_delivery_address").val($("#deliveryAddressInput").val());
        $("#id_funding_type").val($("#fundingTypeDropdown").val());
        
        if ($("#fundingTypeDropdown").val() == "B") {
            $("#id_bbsrc_code").val($("#bbsrcCodeInput").val());
        }

        $("#id_note").val($("#noteInput").val());
        alert($("#id_customer_name").val());
        $("#quoteForm").submit();
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
        var success = true;
        if (!validateName()) {
            displayErrorModal("Name required to submit order.");
            success = false;
        }
        if (!validateEmail()) {
            displayErrorModal("Email required to submit order.");
            success = false;
        }
        if (!validateEmailConfirm()) {
            displayErrorModal("Please confirm your email is correct.");
            success = false;
        }
        if (!validateFundingTypeSelection()) {
            displayErrorModal("Please select a funding type.");
            success = false;
        }
        if (!validateBBSRCCode()) {
            displayErrorModal("BBSRC Code is required for BBSRC funded purchases.");
            success = false;
        }
        if (!validateBillingAddress()) {
            displayErrorModal("Billing Address is required to submit order.");
            success = false;
        }
        if (!validateDeliveryAddress()) {
            displayErrorModal("Delivery Address is required to submit order.");
            success = false;
        }

        if (success) {
            populateSummaryModal();
            $("#checkoutSummaryModal").modal("show");
        }

    });


    $("#confirmQuoteForm").click(function() {
        submitBasket();
    });

});