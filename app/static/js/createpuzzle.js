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

/**
 * Count the number of occurrence of an element in an array
 */
 function countOccurrencesInArray(array,element){
    const countOccurrences = (arr, val) =>
      arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
    var result = countOccurrences(array,element);
    return result;
}

$(document).ready(function () {
    // Display direction options available for drag and drop 
    $("#option")
        .sortable({
        connectWith: ".connectedSortable",
        remove: function (event, ui) {
            ui.item.clone().appendTo("#option_selected");
            $(this).sortable("cancel");
        },
        })
        .disableSelection();

    // Display direction options selected by user 
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

    // Clear all the directions user selected
    $(".clear").on("click", function (e) {
        $("#option_selected li").remove();
        $("#direction_num").text("0");
    });

    // To process after user clicking the "Create" button
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
        var numOfSteps = countOccurrencesInArray(puzzleDirections, "F");
        if (numOfSteps + 1 != puzzleFlow.length) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Please ensure the puzzle shape is achievable with the directions defined",
        });
        return;
        }

        // validate whether the puzzle shape input is in correct format (element should be integer, > 0 and < 50)
        if(!convertAndValidateArray(puzzleFlow)){
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Please ensure the input format for puzzle shape is correct",
            });
            return;
        }

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
 * Converts items in array into int and validate whether all items in the array is > 0 and < 50
 * @param {Array} arr
 */
 function convertAndValidateArray(arr) {
    const validatedArray = new Array(arr.length).fill(0);
    for (var i = 0; i < arr.length; i++) {
        num = parseInt(arr[i]);
        if (num!=null && num>0 && num<50) {
            validatedArray[i]=num;
        }        
    }
    var invalidInput = countOccurrencesInArray(validatedArray, 0);
    if (invalidInput != 0){
        return false;
    } else {
        arr = validatedArray;
        return true;
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
    error: function (jqXHR) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: jqXHR.responseJSON.message,
      });
    },
  });
}
