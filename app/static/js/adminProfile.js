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
      Swal.fire(
        `
            Old Password: ${result.value.oldpassword}
            New Password: ${result.value.newpassword}
        `.trim()
      );
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
      Swal.fire(
        `
            New User: ${result.value.newuser} created!
        `.trim()
      );
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
      Swal.fire(
        `
            Username is updated to: ${result.value.editnewuser}!
        `.trim()
      );
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
        Swal.fire("Deleted!", "User has been deleted.", "success");
      }
    });
  });
});
