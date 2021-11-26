var is_completed = true;

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

  setInterval(checkQueue, 3000);

  $(".clear").on("click", function (e) {
    $("#option_selected li").remove();
    $("#direction_num").text("0/15");
  });

  $(".execute").on("click", function (e) {
    var idsInOrder = $("#option_selected").sortable("toArray");
    if (idsInOrder.length == 0) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Please select at least one step.",
      });
      return;
    }

    // Format data nicely to be sent to backend
    var steps = [];
    for (var i = 0; i < idsInOrder.length; i++) {
      var step = {
        step_number: i + 1,
        direction: idsInOrder[i],
      };
      steps.push(step);
    }

    sendSteps(steps);
  });
});

/**
 * Send steps to backend
 *
 * @param {Array} steps
 */
function sendSteps(steps) {
  $.ajax({
    type: "POST",
    url: "/api/freestyle/execute",
    contentType: "application/json",
    data: JSON.stringify({ steps }),
    success: function (data, textStatus, jqXHR) {
      Swal.fire({
        icon: "success",
        title: "Yay, the car is moving now!",
        text: "Checkout the car movement physically!",
      });

      $("#option_selected li").remove();
      $("#direction_num").text("0/15");
      is_completed = false;
    },
    error: function (jqXHR, textStatus, errorThrown) {
      Swal.fire({
        icon: "warning",
        title: "The Car is still executing!",
        text: "Please wait for the car to finish executing.",
      });
    },
  });
}

/**
 * Check if queue is empty
 */
function checkQueue() {
  $.ajax({
    type: "GET",
    url: "/api/freestyle/check-queue",
    success: function (data, textStatus, jqXHR) {
      if (data.is_empty && !is_completed) {
        Swal.fire({
          icon: "success",
          title: "Yay, execution completed!",
          text: "The car have finished executing!",
        });

        is_completed = true;
      }
    },
  });
}
