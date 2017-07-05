




$(document).ready(function() {
    $("#applyPromoCode").click(function() {
        $.ajax({
            url: "/cart/applyPromotion/" + $("#promoCodeInput").val(),
            success: function(data) {
                console.log(data);
            }
        });
    });
});