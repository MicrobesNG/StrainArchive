
// populate the view codes modal
function populateCodesModal(data) {

    // clear the table
    $("#codesTableBody").empty();

    // loop through returned codes and add row to table for each one
    for (var i = 0; i < data.length; i++) {

        // get the code at index i
        var currentCode = data[i];

        // construct table row html
        var tableRow = "<tr>";
            tableRow += "<td>" + currentCode["pk"] + "</td>";
            tableRow += "<td>" + currentCode["code"] + "</td>";
            tableRow += "<td>" + currentCode["number_of_uses"] + "</td>";
            tableRow += "<td>" + currentCode["max_usages"] + "</td>";
            if (currentCode["active"]) {
                tableRow += "<td>YES</td>";
            } else {
                tableRow += "<td>NO</td>";
            }
            

        // add table row to table
        $("#codesTableBody").append(tableRow);

    }

}


// ajax function to get codes related to promotion with pk == promoPK
function getPromotionCodes(promoPK) {
    $.ajax({
        url: "/management/getPromoCodes/" + promoPK,
        success: function(data) {
            populateCodesModal(data);
            $("#viewCodesModal").modal("show");
        }
    });
}


$(document).ready(function() {

    // opens the promotion creation modal
    $("#openNewPromoModal").click(function() {
        $("#newPromoModal").modal("show");
    });


    // sends get request for promotion's code
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