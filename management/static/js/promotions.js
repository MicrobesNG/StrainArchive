
function getPromotionCodes(promoPK) {
    $.ajax({
        url: "/management/getPromoCodes/" + promoPK,
        success: function(data) {
            console.log(data)
        }
    });
}





$(document).ready(function() {

    // opens the promotion creation modal
    $("#openNewPromoModal").click(function() {
        $("#newPromoModal").modal("show");
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


    // gets relevant data and opens code generation modal
    $(".generateCodes").click(function() {

        // get promotion name and pk
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
        
        // set modal title
        $("#generateCodesModalTitle").text("Generate Codes For: " + promoName);

        // remove previous classes and store promoPK as class
        $("#selectedPromoID").removeClass();
        $("#selectedPromoID").addClass(promoPK);

        // open the modal
        $("#generateCodesModal").modal("show");

    });
    
    // submit the code generation form
    $("#generateCodesForm").submit(function() {
        $("#id_number_of_codes").val($("#newCodesInput").val());
        $("#id_max_number_of_uses").val($("#maxUsesInput").val());
        $("#id_initially_active").val($("#codesInitiallyActive").attr("checked"));
        $("#id_promo_pk").val(parseInt($("#selectedPromoID").attr("class")));
    });

    // submit the new promotion form
    $("#createNewPromotionForm").submit(function() {
        
        $("#id_name").val($("#newPromoNameInput").val());
        $("#id_description").val($("#newPromoDescriptionInput").val());
        $("#id_start_date").val($("#newPromoStartDateInput").val());
        $("#id_expiry_date").val($("#newPromoExpiryDateInput").val());

    });
});