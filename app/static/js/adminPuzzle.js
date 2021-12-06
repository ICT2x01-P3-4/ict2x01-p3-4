$(document).ready(function () {
  // Delete Puzzle
  $(".delPuzzle").on("click", function (e) {
    // put the code here to send array to backend
    Swal.fire({
      title: "Are you sure you want to delete this Puzzle?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, delete it!",
    }).then((result) => {
      if (result.isConfirmed) {
        deletePuzzle($(this).data("pid"));
      }
    });
  });
});

/**
 * Ajax call to delete a puzzle
 **/
function deletePuzzle(_id) {
  $.ajax({
    url: `/api/puzzle/delete/${_id}`,
    type: "DELETE",
    success: function (data, textStatus, jqXHR) {
      Swal.fire({
        title: "Puzzle Deleted",
        text: "Puzzle has been deleted",
        icon: "success",
        confirmButtonText: "OK",
      }).then(function () {
        location.reload();
      });
    },
  });
}
