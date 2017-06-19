
function calculateBasketTotalCost() {
    
    var total = 0;

    $(".itemCostCell:not(.basketHeaderCell)").each(function() {
        
        total = total + parseFloat($(this).html());
        
    });
    
    return total;

}


$(document).ready(function() {

    console.log(calculateBasketTotalCost());


});