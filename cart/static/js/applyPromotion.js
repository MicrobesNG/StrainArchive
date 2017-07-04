
$("#applyPromoCode").click(function() {
    $.ajax({
        url: "/cart/applyPromotion/" + promotionCode,
        success: function(data) {
            console.log(data);
        }
    });
});



$(document).ready(function() {

});