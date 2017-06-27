function submitNewPromoForm() {
    
    $("#id_name").val($("#newPromoNameInput").val());
    $("#id_description").val($("#newPromoDescriptionInput").val());
    $("#id_start_date").val($("#newPromoStartDateInput").val());
    $("#id_expiry_date").val($("#newPromoExpiryDateInput").val());
    
    $("#createNewPromotionForm").submit();

}




$(document).ready(function() {

    $("#openNewPromoModal").click(function() {
        $("#newPromoModal").modal("show");
    });

    $("#submitNewPromoForm").click(function() {
        submitNewPromoForm();
    });
    
});