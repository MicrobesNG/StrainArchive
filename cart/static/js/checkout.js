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

function displayErrorModal(message) {

}

function submitBasket() {
        
        $("#id_customer_name").val($("nameInput").val());
        $("#id_email").val($("#emailInput").val());
        $("#id_billing_address").val($("#billingAddressInput").val());
        $("#id_delivery_address").val($("#deliveryAddressInput").val());
        $("#id_funding_type").val($("#fundingTypeDropdown").val());
        
        if ($("#fundingTypeDropdown").val() == "B") {
            $("#id_bbsrc_code").val($("#bbsrcCodeInput").val());    
        }

        $("#id_note").val($("#noteInput").val());

        $("#quoteForm").submit();
}

function validateEmail() {
    if ($("#emailInput").val() == $("#confirmEmailInput").val()) {
        return true;
    } else {
        return false;
    }
}

function validateBBSRCCode() {
    if ($("#fundingTypeDropdown").val() == "B") {
        if ($("#bbsrcCodeInpuut").val() == "") {
            return false;
        }
    }
    return true;
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

        if (validateEmail()) {
            if (validateBBSRCCode()) {
                populateSummaryModal();
                $("#checkoutSummaryModal").modal("show");
            } else {
                displayErrorModal("BBSRC Code required for BBSRC funded purchases.")
            }
        } else {
            displayErrorModal("Please ensure your email is correct.")
        }

    });


    $("#confirmQuoteForm").click(function() {
        submitBasket();
    });

});