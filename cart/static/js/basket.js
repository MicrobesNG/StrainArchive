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
        console.log(i);
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
                // break;
            }
        });

        if (!located) {

            var html = generateBasketEntryRow(
                currentSessionStrain["name"],
                currentSessionStrain["amount"],
                currentSessionStrain["cost"]
            );

            $("#basketContentTable").append(html)

        }

    }

    setBasketCostText(data["total_cost"]);

}


function addToBasket(strainPK) {
    $.ajax({
        url: "/cart/addToBasket/" + strainPK,
        success: function(data) {
            updateBasket(data);
        }
    });
}

function removeFromBasket(strainPK) {
    $.ajax({
        url: "/cart/removeFromBasket/" + strainPK,
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

    // initially hide the remove column
    $(".removeItemCell").hide();

    $(".addToBasket").click(function() {
        addToBasket($(this).closest(".strainRow").attr("id"));
    });
    
});