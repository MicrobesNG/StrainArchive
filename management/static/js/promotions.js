

// populate the view codes modal
function populateCodesModal(data) {

    // clear the table
    $("#codesTableBody").empty();

    // loop through returned codes and add row to table for each one
    for (var i = 0; i < data.length; i++) {

        // get the code at index i
        var currentCode = data[i];
        
        var row_class;
        if (currentCode["number_of_uses"] == currentCode["max_usages"]) {
            row_class = "promo_limit";
        } else if (!currentCode["active"]) {
            row_class = "promo_inactive";
        } else {
            row_class = "promo_active";
        }

        // construct table row html
        var tableRow = "<tr class='" + row_class + "' id='" + currentCode["pk"] + "'>";
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

    $(".promoTypeOption").click(function() {
        $(this).parent().parent().find("button").val($(this).attr("id"));
        $(this).parent().parent().find("button").text($(this).text());

        switch ($(this).attr("id")) {
            case "FPR":
                $("#fprContainer").show();
                $("#prContainer").hide();
                break;
            case "PR":
                $("#fprContainer").hide();
                $("#prContainer").show();
                break;
            case "NS":
                $("#fprContainer").hide();
                $("#prContainer").hide();
                break;
        }

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
        $("#id_initially_active").val($("#codesInitiallyActive").is(":checked"));
        $("#id_promo_pk").val(parseInt($("#selectedPromoID").attr("class")));

    });

    // submit the new promotion form
    $("#createNewPromotionForm").submit(function() {
        
        $("#id_name").val($("#newPromoNameInput").val());
        $("#id_description").val($("#newPromoDescriptionInput").val());
        $("#id_start_date").val($("#newPromoStartDateInput").val());
        $("#id_expiry_date").val($("#newPromoExpiryDateInput").val());
        $("#id_promo_type").val($("#promoTypeDropdown").val());

        $("#id_fixed_amount").val($("#newPromoFPRAmount").val());
        $("#id_percentage_amount").val($("#newPromoPRAmount").val());
        alert($("#id_fixed_amount").val());
    });
});