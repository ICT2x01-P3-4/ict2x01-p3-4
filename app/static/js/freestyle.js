$(document).ready(function () {
  $("#option")
    .sortable({
      connectWith: ".connectedSortable",
      remove: function (event, ui) {
        ui.item.clone().appendTo("#option_selected");
        $(this).sortable("cancel");
      },
    })
    .disableSelection();

  $("#option_selected")
    .sortable({
      receive: function (event, ui) {
        var num = $("#option_selected li").length;
        if (num > 15) {
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "The maximum step you can input is 15.",
          });
          $("#option_selected").sortable("cancel");
          $("#option_selected li:last-child").remove();
        } else {
          $("#direction_num").text(num + "/15");
        }
      },
    })
    .disableSelection();

  $(".clear").on("click", function (e) {
    $("#option_selected li").remove();
    $("#direction_num").text("0/15");
  });

  $(".execute").on("click", function (e) {
    var idsInOrder = $("#option_selected").sortable("toArray");
    console.log(idsInOrder);
    // put the code here to send array to backend
    Swal.fire({
      icon: "success",
      title: "Yay, the car is moving now!",
      text: "Checkout the car movement physically!",
    });
    $("#option_selected li").remove();
    $("#direction_num").text("0/15");
  });
});
