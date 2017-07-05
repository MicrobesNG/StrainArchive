function displayErrorModal(message) {
    $("#errorMessage").text(message);
    $("#errorModal").modal("show");
}



function validateEmail() {
    if ($("#emailInput").val() == "") {
        return false;
    } else {
        return true;
    }
}

function validateEmailConfirm() {
    if ($("#emailInput").val() == $("#confirmEmailInput").val()) {
        return true;
    } else if ($("#confirmEmailInput").val() == "") {
        return false;
    } else {
        return false;
    }
}

function validateFundingTypeSelection() {
    if ($("#fundingTypeDropdown").val() == "") {
        return false;
    } else {
        return true;
    }

}

function validateBBSRCCode() {
    if ($("#fundingTypeDropdown").val() == "B") {
        if ($("#bbsrcCodeInput").val() == "") {
            return false;
        }
    }
    return true;
}

function validateName() {
    if ($("#nameInput").val() == "") {
        return false;
    } else {
        return true;
    }
}

function validateBillingAddress() {
    if ($("#billingAddressInput").val() == "") {
        return false;
    } else {
        return true;
    }
}

function validateDeliveryAddress() {
    if ($("#deliveryAddressInput").val() == "") {
        return false;
    } else {
        return true;
    }
}


function validateBillingAddressDetails() {
    var success = true;
    if (!validateBillingAddress()) {
        displayErrorModal("Billing address required to submit order.");
        success = false;
    }

    return success;

}


function validateDeliveryAddressDetails() {
    var success = true;
    if (!validateDeliveryAddress()) {
        displayErrorModal("Delivery address required to submit order.");
        success = false;
    }

    return success;

}

function validatePaymentDetails() {
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

    return success;
}