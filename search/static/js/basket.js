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

function setBasketCostText() {
    var amount = calculateBasketTotalCost();
    var text = generateBasketCostText(amount.toFixed(2));
    $(BASKET_COST_TEXT_SELECTOR).html(text);
}


$(document).ready(function() {

    // toggle remove column on edit button click
    $("#basketEditButton").click(function() {
        $(".removeItemCell").toggle();
    });

    $(".removeFromBasket").click(function() {

        var amount = parseInt($(this).parent().parent().find(".itemAmountCell").html());

        var costPerAmount = (parseFloat($(this).parent().parent().find(".itemCostCell").html()) / amount).toFixed(2);

        amount--;

        if (amount == 0) {
            $(this).parent().parent().remove();
        } else {
            $(this).parent().parent().find(".itemAmountCell").html(amount);
            $(this).parent().parent().find(".itemCostCell").html(amount * costPerAmount);
        }
        
        setBasketCostText();

    });

    // initially hide the remove column
    $(".removeItemCell").hide();

    // calculate inital basket cost
    setBasketCostText();

});