function getSelectedTaxClass(taxClassOption, taxClassCode) {

    var output = [];

    $('.selectedOption.' + taxClassOption).each(function() {
        output.push($(this).attr("id").replace(taxClassCode + "_", ""));
    });
    
    return output;

}


$(document).ready(function() {

    $("#blastSearchForm").submit(function() {
        $("#id_query_string").val($("#blastSearchInput").val());
        if ($("#blastnRadio").is(":checked")) {
            $("#id_blast_type").val("N");
        }
        if ($("#blastpRadio").is(":checked")) {
            $("#id_blast_type").val("P");
        }
        
        $("#id_blast_parameters").val($("#parameterInput").val());

        
    });

    $("#searchParameterForm").submit(function() {

        $("#id_selected_family_ids").val(getSelectedTaxClass("familyDropdownOption", "F"));
        $("#id_selected_genus_ids").val(getSelectedTaxClass("generaDropdownOption", "G"));
        $("#id_selected_species_ids").val(getSelectedTaxClass("speciesDropdownOption", "S"));

    });

});