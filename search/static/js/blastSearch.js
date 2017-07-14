

$(document).ready(function() {

    $(".searchRadioButton").click(function() {
        $(".searchRadioButton").prop("checked", false);
        $(this).prop("checked", true);
    });

});