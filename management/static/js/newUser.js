


$(document).ready(function() {
    
    $(".permissionOption").click(function() {
        
        $("#newPermissionsDropdown").text($(this).text());
        $("#newPermissionsDropdown").val($(this).attr("id"));

    });


    $("#openNewUserModal").click(function() {

        $("#newUserModal").modal("show");

    });


    $("#newUserForm").submit(function() {

        $("#id_username").val($("#createNewUsername").val());
        $("#id_first_name").val($("#createNewFirstName").val());
        $("#id_last_name").val($("#createNewLastName").val());
        $("#id_user_type").val($("#newPermissionsDropdown").val());
        $("#id_email").val($("#createNewEmail").val());

    });

});