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