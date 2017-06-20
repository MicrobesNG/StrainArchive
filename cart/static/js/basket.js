var BASKET_COST_TEXT_SELECTOR = "#basketTotalCost";

function calculateBasketTotalCost() {
    var total = 0;
    $(".itemCostCell:not(.basketHeaderCell)").each(function() {
        total = total + parseFloat($(this).html()); 
    });
    return total;
}

function generateBasketCostText(amount) {
    return "£" + amount.toString();
}

function setBasketCostText(amount) {
    // var amount = calculateBasketTotalCost();
    var text = generateBasketCostText(amount.toFixed(2));
    $(BASKET_COST_TEXT_SELECTOR).html(text);
}


function updateRowInBasket(row, newAmount, newCost) {
    
    row.find(".itemAmountCell").html(newAmount);
    row.find(".itemCostCell").html(newCost);

}

function generateBasketEntryRow(newName, newAmount, newCost) {

    var row = '<tr class="itemRow">';
    row += '<td class="removeItemCell"><button type="button" class="btn btn-xs btn-danger removeFromBasket">&times;</button></td>';
    row += '<td class="itemNameCell">' + newName + '</td>';
    row += '<td class="itemAmountCell">' + newAmount + '</td>';
    row += '<td class="itemCostCell">' + newCost + '</td>';
    row += '<tr>';

    return row;
}


function updateBasket(data) {
    
    for (var i = 0; i < data["items"].length; i++) {
        
        var currentSessionStrain = data["items"][i];
        
        var located = false;
        $(".itemRow").each(function() {

            var basketName = $(this).find(".itemNameCell").html();
            var basketAmount = $(this).find(".itemAmountCell").html();
            var basketCost = $(this).find(".itemCostCell").html();

            if (basketName == currentSessionStrain["name"]) {
                located = true;

                updateRowInBasket(
                    $(this),
                    currentSessionStrain["amount"],
                    currentSessionStrain["cost"]
                );

                break;
            }
        });

        if (!located) {

            var html = generateBasketEntryRow(
                currentSessionStrain["name"],
                currentSessionStrain["amount"],
                currentSessionStrain["cost"]
            );

        }

    }

    setBasketCostText(data["total_cost"]);

}


function addToBasket(strainPK) {
    $.ajax({
        url: "/add_to_basket/" + strainPK,
        success: function(data) {
            updateBasket(data);
        }
    });
}


$(document).ready(function() {

    // toggle remove column on edit button click
    $("#basketEditButton").click(function() {
        $(".removeItemCell").toggle();
    });



    // $(".removeFromBasket").click(function() {

    //     var amount = parseInt($(this).parent().parent().find(".itemAmountCell").html());

    //     var costPerAmount = (parseFloat($(this).parent().parent().find(".itemCostCell").html()) / amount).toFixed(2);

    //     amount--;

    //     if (amount == 0) {
    //         $(this).parent().parent().remove();
    //     } else {
    //         $(this).parent().parent().find(".itemAmountCell").html(amount);
    //         $(this).parent().parent().find(".itemCostCell").html(amount * costPerAmount);
    //     }
        
    //     setBasketCostText();

    // });

    // initially hide the remove column
    $(".removeItemCell").hide();

    // calculate inital basket cost
    setBasketCostText();

});