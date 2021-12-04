const puzzle = [
  [1, 2, 3, 4, 5, 6, 7],
  [8, 9, 10, 11, 12, 13, 14],
  [15, 16, 17, 18, 19, 20, 21],
  [22, 23, 24, 25, 26, 27, 28],
  [29, 30, 31, 32, 33, 34, 35],
  [36, 37, 38, 39, 40, 41, 42],
  [43, 44, 45, 46, 47, 48, 49],
];

/**
 * Create puzzle grid
 */
function createPuzzleGrid(puzzle) {
  for (var i = 0; i < puzzle.length; i++) {
    for (var j = 0; j < puzzle[i].length; j++) {
      var rowname = "row" + (i + 1);
      if (puzzle.includes(puzzle[i][j])) {
        if (puzzle.indexOf(puzzle[i][j]) == 0) {
          document.getElementById(rowname).innerHTML +=
            "<td id='box" +
            puzzle[i][j] +
            "' class='border-2 border-gray-500 w-12 h-12'>" +
            puzzle[i][j] +
            "</td>";
        } else {
          document.getElementById(rowname).innerHTML +=
            "<td id='box" +
            puzzle[i][j] +
            "' class='border-2 border-gray-500 w-12 h-12'>" +
            puzzle[i][j] +
            "</td>";
        }
      } else {
        document.getElementById(rowname).innerHTML +=
          "<td id='box" +
          puzzle[i][j] +
          "' class='border-2 border-gray-500 w-12 h-12'>" +
          puzzle[i][j] +
          "</td>";
      }
    }
  }
}

/**
 * Create the puzzle grid when DOM is loaded
 */
window.addEventListener("DOMContentLoaded", function () {
  createPuzzleGrid(puzzle);
});

var is_completed = true;

/**
 * Display the maximum step for the puzzle direction according to the user input for steps required
 */
function displayMaxStep() {
  document.getElementById("direction_max_num").innerHTML =
    document.getElementById("steps_required").value;
}

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
        var maxnum = document.getElementById("steps_required").value;
        if (num <= maxnum) {
          $("#direction_num").text(num);
        } else {
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "You only selected " + maxnum + " steps to create the puzzle",
          });
          $("#option_selected").sortable("cancel");
          $("#option_selected li:last-child").remove();
        }
      },
    })
    .disableSelection();

  $(".clear").on("click", function (e) {
    $("#option_selected li").remove();
    $("#direction_num").text("0");
  });

  $(".create").on("click", function (e) {
    var puzzleDirections = $("#option_selected").sortable("toArray");
    var puzzleName = document.getElementById("puzzle_name").value;
    var puzzleLevel = document.getElementById("diff_level").value;
    var stepsRequired = document.getElementById("steps_required").value;
    var puzzleFlow = document.getElementById("puzzle_flow").value.split(",");

    // Verify whether all fields are filled in
    if (
      puzzleDirections.length == 0 ||
      puzzleFlow.length == 0 ||
      puzzleName.length == 0
    ) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Please fill in all the input fields.",
      });
      return;
    }

    // Verify whether the number of puzzle direction boxes is the same as the number of steps required
    if (stepsRequired != $("#option_selected li").length) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Please ensure the number of puzzle direction boxes is the same as the number of step required",
      });
      return;
    }

    // Verify whether the puzzle shape is achievable with the puzzle directions defined
    const countOccurrences = (arr, val) =>
      arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
    var numOfSteps = countOccurrences(puzzleDirections, "F");
    if (numOfSteps + 1 != puzzleFlow.length) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Please ensure the puzzle shape matches the puzzle direction",
      });
      return;
    }

    // double check whether all fields are null
    // diff level > 0 and < 8
    // steps required > 0 and < 16
    // puzzle flow: all elements is convertable to int (current puzzle flow format ["12","13","14"])
    // number of "F" in puzzleDirections = number of elements in puzzleFlow
    convertArray(puzzleFlow);

    // Format data nicely to pass to backend
    var data = {
      name: puzzleName,
      difficulty: parseInt(puzzleLevel),
      puzzle_steps: puzzleDirections,
      puzzle_flow: puzzleFlow,
    };
    createPuzzle(data);
  });
});

// Decrement function for number counter
function decrement(e, dataaction, step) {
  btn = e.target.parentNode.parentElement.querySelector(dataaction);
  target = btn.nextElementSibling;
  let value = Number(target.value);
  if (value > step) {
    value--;
    target.value = value;
  }
}

// Increment function for number counter
function increment(e, dataaction, step) {
  btn = e.target.parentNode.parentElement.querySelector(dataaction);
  target = btn.nextElementSibling;
  let value = Number(target.value);
  if (value < step) {
    value++;
    target.value = value;
  }
}

/**
 * Converts items in array into int
 * @param {Array} arr
 */
function convertArray(arr) {
  for (var i = 0; i < arr.length; i++) {
    arr[i] = parseInt(arr[i]);
  }
}

/**
 * Ajax call to server to create a new puzzle
 */
function createPuzzle(data) {
  $.ajax({
    type: "POST",
    url: "/api/puzzle/create",
    contentType: "application/json",
    data: JSON.stringify(data),
    success: async function (data) {
      await Swal.fire({
        icon: "success",
        title: "Success",
        text: "Puzzle created successfully",
      });
      location.href = "/admin/puzzle";
    },
    error: function (data) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Something went wrong!",
      });
    },
  });
}
