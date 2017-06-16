function getSelectedTaxClass(taxClassOption, taxClassCode) {

    var output = [];

    $('.selectedOption.' + taxClassOption).each(function() {
        output.push($(this).attr("id").replace(taxClassCode + "_", ""));
    });
    
    return output;

}


$(document).ready(function() {

    $("#searchParameterForm").submit(function() {

        $("#id_selected_family_ids").val(getSelectedTaxClass("familyDropdownOption", "F"));
        $("#id_selected_genus_ids").val(getSelectedTaxClass("generaDropdownOption", "G"));
        $("#id_selected_species_ids").val(getSelectedTaxClass("speciesDropdownOption", "S"));

    });

});