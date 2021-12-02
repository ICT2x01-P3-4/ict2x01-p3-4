$(document).ready(function () {
  //change admin password
  $(".changepass").on("click", function (e) {
    //code
    Swal.fire({
      title: "Change Password for Admin",
      html: `
        <input type="password" id="oldpassword" class="swal2-input" placeholder="Old Password">
        <input type="password" id="newpassword" class="swal2-input" placeholder="New Password">
        <input type="password" id="cfmnewpassword" class="swal2-input" placeholder="Confirm New Password">`,
      confirmButtonText: "Change Password",
      focusConfirm: false,
      showCancelButton: true,

      preConfirm: () => {
        const oldpassword = Swal.getPopup().querySelector("#oldpassword").value;
        const newpassword = Swal.getPopup().querySelector("#newpassword").value;
        const cfmnewpassword =
          Swal.getPopup().querySelector("#cfmnewpassword").value;

        if (
          !oldpassword ||
          newpassword != cfmnewpassword ||
          !newpassword ||
          !cfmnewpassword
        ) {
          Swal.showValidationMessage(`Try Again`);
        }
        return { oldpassword: oldpassword, newpassword: newpassword };
      },
    }).then((result) => {
      changePassword(result.value.oldpassword, result.value.newpassword);
    });
  });

  //create user
  $(".createuser").on("click", function (e) {
    //code
    Swal.fire({
      title: "Create new user username",
      html: `
        <input type="text" id="newuser" class="swal2-input" placeholder="New User Name">`,
      confirmButtonText: "Create",
      focusConfirm: false,
      showCancelButton: true,

      preConfirm: () => {
        const newuser = Swal.getPopup().querySelector("#newuser").value;

        if (!newuser) {
          Swal.showValidationMessage(`Please input a user name`);
        }
        return { newuser: newuser };
      },
    }).then((result) => {
      createUser(result.value.newuser);
    });
  });

  //edit user
  $(".edituser").on("click", function (e) {
    //code
    Swal.fire({
      title: "Enter new username for user",
      html: `
        <input type="text" id="editnewuser" class="swal2-input" placeholder="New User Name">`,
      confirmButtonText: "Save",
      focusConfirm: false,
      showCancelButton: true,

      preConfirm: () => {
        const editnewuser = Swal.getPopup().querySelector("#editnewuser").value;

        if (!editnewuser) {
          Swal.showValidationMessage(`Please input a user name`);
        }
        return { editnewuser: editnewuser };
      },
    }).then((result) => {
      const oldName = $(this).data("name");
      const newName = result.value.editnewuser;
      updateUser(oldName, newName);
    });
  });

  // Delete user
  $(".deleteuser").on("click", function (e) {
    // put the code here to send array to backend
    Swal.fire({
      title: "Are you sure you want to delete this user?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, delete it!",
    }).then((result) => {
      if (result.isConfirmed) {
        deleteUser($(this).data("name"));
      }
    });
  });
});

/**
 * Ajax call to change admin password
 *
 * @param {string} oldPassword
 * @param {string} newPassword
 */
function changePassword(oldPassword, newPassword) {
  $.ajax({
    url: "/api/admin/change-password",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      old_password: oldPassword,
      new_password: newPassword,
    }),
    success: function (data, textStatus, jqXHR) {
      Swal.fire({
        title: "Password Changed",
        text: "Your password has been changed",
        icon: "success",
        confirmButtonText: "OK",
      });
    },
    error: function (jqXHR, textStatus, errorThrown) {
      Swal.fire({
        title: "Password Change Failed",
        text: "Your password has not been changed",
        icon: "error",
        confirmButtonText: "OK",
      });
    },
  });
}

/**
 * Ajax call to create a new user
 */
function createUser(name) {
  $.ajax({
    url: "/api/admin/create-user",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      name: name,
    }),
    success: function (data, textStatus, jqXHR) {
      Swal.fire({
        title: "User Created",
        text: "User has been created",
        icon: "success",
        confirmButtonText: "OK",
      }).then(function () {
        location.reload();
      });
    },
    error: function (jqXHR, textStatus, errorThrown) {
      Swal.fire({
        title: "User Creation Failed",
        text: "User has not been created",
        icon: "error",
        confirmButtonText: "OK",
      });
    },
  });
}

/**
 * Ajax call to update user name
 * @param {string} name
 */
function updateUser(oldName, newName) {
  $.ajax({
    url: `/api/admin/update-user/${oldName}`,
    type: "PUT",
    contentType: "application/json",
    data: JSON.stringify({
      newName: newName,
    }),
    success: function (data, textStatus, jqXHR) {
      Swal.fire({
        title: "User Updated",
        text: "User has been updated",
        icon: "success",
        confirmButtonText: "OK",
      }).then(function () {
        location.reload();
      });
    },
    error: function (jqXHR, textStatus, errorThrown) {
      Swal.fire({
        title: "User Update Failed",
        text: "User has not been updated",
        icon: "error",
        confirmButtonText: "OK",
      });
    },
  });
}

/**
 * Ajax call to delete a user
 */
function deleteUser(name) {
  $.ajax({
    url: `/api/admin/delete-user/${name}`,
    type: "DELETE",
    success: function (data, textStatus, jqXHR) {
      Swal.fire({
        title: "User Deleted",
        text: "User has been deleted",
        icon: "success",
        confirmButtonText: "OK",
      }).then(function () {
        location.reload();
      });
    },
  });
}
