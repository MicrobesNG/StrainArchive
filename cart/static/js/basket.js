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
    var text = generateBasketCostText(amount.toFixed(2));
    $(BASKET_COST_TEXT_SELECTOR).html(text);
}


function updateRowInBasket(row, newAmount, newCost, newPK) {
    
    row.find(".itemAmountCell").html(newAmount);
    row.find(".itemCostCell").html(newCost);

}

function generateBasketEntryRow(newName, newAmount, newCost, newPK) {

    var row = '<tr class="itemRow" id="item_' + newPK + '">';
    row += '<td class="removeItemCell"><button type="button" class="btn btn-xs btn-danger removeFromBasket">&times;</button></td>';
    row += '<td class="itemNameCell">' + newName + '</td>';
    row += '<td class="itemAmountCell">' + newAmount + '</td>';
    row += '<td class="itemCostCell">' + newCost + '</td>';
    row += '<tr>';

    return row;
}


function itemInSession(itemPK, sessionItems) {

    for (var i = 0; i < sessionItems.length; i++) {

        if (sessionItems[i]["pk"] == itemPK) {
            return true;
        }
    }

    return false;

}


function updateBasket(data) {

    // if no items in session basket, remove everything
    if (data["items"].length == 0) {
        $(".itemRow").each(function() {
            $(this).remove();
        });

    }

    // loop over all items in session basket
    for (var i = 0; i < data["items"].length; i++) {
        
        var currentSessionStrain = data["items"][i];
        
        // loop over all items on page basket   
        var locatedOnPage = false;
        $(".itemRow").each(function() {

            // grab properties
            var basketName = $(this).find(".itemNameCell").html();
            var basketAmount = $(this).find(".itemAmountCell").html();
            var basketCost = $(this).find(".itemCostCell").html();
            var basketPK = parseInt($(this).attr("id").replace("item_", ""));

            // if the page item is not present in session basket remove from page
            if (!itemInSession(basketPK, data["items"])) {
                $(this).remove();
            } else {
            
                // if found in session basket, update the item row on page
                if (basketPK == currentSessionStrain["pk"]) {
                    
                    locatedOnPage = true;

                    updateRowInBasket(
                        $(this),
                        currentSessionStrain["amount"],
                        currentSessionStrain["cost"]
                    );
                    
                }
            }
        });

        // if after looping over each row on page it has not been found
        if (!locatedOnPage) {

            // add a new row to the page basket
            var html = generateBasketEntryRow(
                currentSessionStrain["name"],
                currentSessionStrain["amount"],
                currentSessionStrain["cost"],
                currentSessionStrain["pk"]
            );

            $("#basketContentTable").append(html)
            $(".removeItemCell").hide();

        }

    }
    
    // update cost on page basket
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
            console.log(data);
            updateBasket(data);
        }
    });
}


$(document).ready(function() {

    // initially hide the remove cell column
    $(".removeItemCell").hide();

    // toggle remove column on edit button click
    $("#basketEditButton").click(function() {
        
        if ($(this).hasClass("btn-warning")) {
            
            $(this).removeClass("btn-warning");
            $(this).addClass("btn-primary");

            $(".removeItemCell").hide();
            $(".addToBasket").show();

        } else {

            $(this).removeClass("btn-primary");
            $(this).addClass("btn-warning");

            $(".removeItemCell").show();
            $(".addToBasket").hide();
        }
        
    });

    $(".addToBasket").click(function() {
        addToBasket($(this).closest(".strainRow").attr("id"));
    });

    $("#basketContainer").on("click", ".removeFromBasket", function() {
        removeFromBasket(parseInt($(this).closest(".itemRow").attr("id").replace("item_", "")));
    });
    
});