function addOptionToDropdownMenu(menuID, optionName, optionID, optionClass, tax, hidden) {
    
    // var checkBoxHTML = '<input type="checkbox" class="' + optionClass + 'Checkbox cb" id="' + tax + "_" + optionID + '" value=""> ' + optionName + '</label>';
    var optionHTML = "<li class='" + optionClass + "' id='" + tax + "_" + optionID + "'>" + optionName + "</li>";

    $("#" + menuID).append(optionHTML);

    if (hidden) {
        $("#" + menuID + " li:last").hide();
    }

}



function setTreeVisibility(nodeName, nodeType, hide) {
    switch (nodeType) {
        case "FAMILY":
            for (var i = 0; i < taxStructure["data"].length; i++) {
                if (taxStructure["data"][i]["name"] == nodeName) {
                    var node = taxStructure["data"][i];
                    for (var j = 0; j < node["genera"].length; j++) {
                        var currentGene = node["genera"][j];
                        if (hide) {
                            
                            $("#G_" + currentGene["pk"]).parent().hide();
                            
                            for (var k = 0; k < currentGene["species"].length; k++) {
                                
                                var currentSpecies = currentGene["species"][k];
                                $("#S_" + currentSpecies["pk"]).hide();

                            }

                        } else {

                            $("#G_" + currentGene["pk"]).show();

                        }

                        for (var k = 0; k < currentGene["species"].length; k++) {
                            var currentSpecies = currentGene["species"][k];
                            if (hide) {
                                $("#S_" + currentSpecies["pk"]).hide();
                            } else{
                                $("#S_" + currentSpecies["pk"]).show();
                            }
                        }
                    }
                    break;
                }
            }
            break;
        
        case "GENUS":

            for (var i = 0; i < taxStructure["data"].length; i++) {
                var currentFamily = taxStructure["data"][i];
                for (var j = 0; j < currentFamily["genera"].length; j++) {
                    if (currentFamily["genera"][i]["name"] == nodeName) {
                        var selectedGene = currentFamily["genera"][i];
                        for (var k = 0; k < selectedGene["species"].length; k++) {
                            
                            var currentSpecies = currentGene["species"][k];
                            if (hide) {
                                $("#S_" + currentSpecies["pk"]).hide();
                            } else{
                                $("#S_" + currentSpecies["pk"]).show();
                            }
                        }
                    }
                    break;
                }
                break;
            }
            break;
        
        default:

            break;

    }

}





$(document).ready(function() {

    for (var i = 0; i < taxStructure["data"].length; i++) {

        var currentFamily = taxStructure["data"][i];

        addOptionToDropdownMenu(
            "familyDropdownMenu",
            currentFamily["name"],
            currentFamily["pk"],
            "familyDropdownOption",
            "F",
            false
        );

        for (var j = 0; j < currentFamily["genera"].length; j++) {

            var currentGenus = currentFamily["genera"][j];

            addOptionToDropdownMenu(
                "generaDropdownMenu",
                currentGenus["name"],
                currentGenus["pk"],
                "generaDropdownOption",
                "G",
                true
            );

            for (var k = 0; k < currentGenus["species"].length; k++) {

                var currentSpecies = currentGenus["species"][k];

                addOptionToDropdownMenu(
                    "speciesDropdownMenu",
                    currentSpecies["name"],
                    currentSpecies["pk"],
                    "speciesDropdownOption",
                    "S",
                    true
                );

            }

        }
        
    }

    $("#familyDropdownMenu").on("click", ".familyDropdownOption", function() {

        if ($(this).hasClass("selectedOption")) {

            $(this).removeClass("selectedOption");

            setTreeVisibility($(this).text().replace(/\s+/g, ''), "FAMILY", true);

        } else {

            $(this).addClass("selectedOption");

            setTreeVisibility($(this).text().replace(/\s+/g, ''), "FAMILY", false);

        }



        // if ($(this).prop("checked")) {

        //     $(this).prop("checked", false);
        //     setTreeVisibility($(this).text().replace(/\s+/g, ''), "FAMILY", true);

        // } else {

        //     $(this).prop("checked", true);
        //     setTreeVisibility($(this).text().replace(/\s+/g, ''), "FAMILY", false);

        // }

    });

    $("#generaDropdownMenu").on("click", ".cb", function() {

        if ($(this).prop("checked")) {

            $(this).prop("checked", false);
            setTreeVisibility($(this).text().replace(/\s+/g, ''), "GENUS", true);

        } else {

            $(this).prop("checked", true);
            setTreeVisibility($(this).text().replace(/\s+/g, ''), "GENUS", false);

        }

    });

});