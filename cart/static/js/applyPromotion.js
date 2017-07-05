

$(document).ready(function() {
    
    $("#clearPromocode").hide();
    
    $("#confirmCode").click(function() {
        
        $("#promoCodeInput").prop("disabled", true);
        $("#clearPromocode").show();
        $("#checkPromocode").hide();
        $("#promoDetailsModal").modal("hide");

    });

    $("#clearPromocode").click(function() {
        $.ajax({
            url: "/cart/cancelPromotion/" + $("#promoCodeInput").val(),
            success: function(data) {
                $("#promoCodeInput").prop("disabled", false);
                $("#clearPromocode").hide();
                $("#checkPromocode").show();
                $("#finalCost").text("£" + data["basket"]["total_cost"]);
            }
        });
    });

    $("#cancelPromotionApplication").click(function() {
        $.ajax({
            url: "/cart/cancelPromotion/" + $("#promoCodeInput").val(),
            success: function(data) {
                $("#promoDetailsModal").hide();
                $("#finalCost").text("£" + data["basket"]["total_cost"]);
            }
        });
    });


    $("#checkPromocode").click(function() {
        $.ajax({
            url: "/cart/checkPromotion/" + $("#promoCodeInput").val(),
            success: function(data) {

                switch (data["status"]) {
                    case "NOT_FOUND":
                        var message = "The promo code is not valid.";
                        $("#promotionStatusTitle").text("INVALID PROMOTION CODE");
                        $("#promoModalMessage").text(message);
                        $("#promoStatusModal").modal("show");
                        break;
                    case "EXPIRED":
                        var message = "The promotion has expired.";
                        $("#promotionStatusTitle").text("PROMOTION EXPIRED");
                        $("#promoModalMessage").text(message);
                        $("#promoStatusModal").modal("show");
                        break;
                    case "NOT_YET_RUNNING":
                        var message = "The promotion has not started yet.";
                        $("#promotionStatusTitle").text("PROMOTION NO RUNNING");
                        $("#promoModalMessage").text(message);
                        $("#promoStatusModal").modal("show");
                        break;
                    case "USEAGE_LIMIT":
                        var message = "This code has already reached its usage limit.";
                        $("#promotionStatusTitle").text("CODE USAGE LIMIT HIT");
                        $("#promoModalMessage").text(message);
                        $("#promoStatusModal").modal("show");
                        break;
                    case "INACTIVE":
                        var message = "This code is not active.";
                        $("#promotionStatusTitle").text("INACTIVE CODE");
                        $("#promoModalMessage").text(message);
                        $("#promoStatusModal").modal("show");
                        break;
                    case "SUCCESS":
                        var message = "This will reduce your total basket cost from £" + data["basket"]["total_cost"];
                            message += " to £" + data["basket"]["promotion"]["promotion_total_cost"];
                        $("#promoName").text(data["promo_name"]);
                        $("#promoDescription").text(data["promo_description"]);
                        $("#promoApplicationSummary").text(message);
                        $("#finalCost").text("£" + data["basket"]["promotion"]["promotion_total_cost"]);
                        $("#promoDetailsModal").modal("show");
                        break;
                    default:
                        break;
                }
            }
        });
    });
});