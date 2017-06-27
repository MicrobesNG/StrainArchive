function submitNewPromoForm() {
    
    $("#id_name").val($("#newPromoNameInput").val());
    $("#id_description").val($("#newPromoDescriptionInput").val());
    $("#id_start_date").val($("#newPromoStartDateInput").val());
    $("#id_expiry_date").val($("#newPromoExpiryDateInput").val());
    
    $("#createNewPromotionForm").submit();

}


function getPromotionCodes(promoPK) {
    $.ajax({
        url: "/management/getPromoCodes/" + promoPK,
        success: function(data) {
            console.log(data)
        }
    });
}

function generatePromotionCodes(promoPK) {
    $.ajax({
        url: "/management/getPromoCodes/" + promoPK,
        success: function(data) {
            console.log(data)
        }
    });
}




$(document).ready(function() {

    $("#openNewPromoModal").click(function() {
        $("#newPromoModal").modal("show");
    });

    $("#submitNewPromoForm").click(function() {
        submitNewPromoForm();
    });

    $(".viewCodes").click(function() {
        var promoPK = $(this)
                        .parent()
                        .parent()
                        .parent()
                        .attr("id")
                        .replace("promo_", "");
        
        getPromotionCodes(parseInt(promoPK));

    });

    $(".generateCodes").click(function() {
        var promoName = $(this)
                            .parent()
                            .parent()
                            .parent()
                            .find(".promoNameCell")
                            .html();
        var promoPK = $(this)
                        .parent()
                        .parent()
                        .parent()
                        .attr("id")
                        .replace("promo_", "");

        $("#generateCodesModalTitle").text("Generate Codes For: " + promoName);
        
        $("#selectedPromoID").removeClass();
        $("#selectedPromoID").addClass(promoPK);

        $("#generateCodesModal").modal("show");

    });

    $("#generateCodesSubmission").click(function() {

        var promoPK = parseInt($("#selectedPromoID").attr("class"));

        generatePromotionCodes(promoPK);

    });
    
});