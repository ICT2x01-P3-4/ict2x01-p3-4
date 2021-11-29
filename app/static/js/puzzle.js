// TODO: need to retrieve puzzle, score, and stage from db (no need answer and flow bcus user can see in javascript)
const puzzle = [
  [1, 2, 3, 4, 5, 6, 7],
  [8, 9, 10, 11, 12, 13, 14],
  [15, 16, 17, 18, 19, 20, 21],
  [22, 23, 24, 25, 26, 27, 28],
  [29, 30, 31, 32, 33, 34, 35],
  [36, 37, 38, 39, 40, 41, 42],
  [43, 44, 45, 46, 47, 48, 49],
];

const answer = data.puzzle_answer;
const flow = data.puzzle_flow;
var remainingBoxes = flow.slice(1);
var remainingSteps = answer.slice(0);

score = data.score;
stage = data.stage;

var is_completed = true;
var interval = null;
var prevBox = {};

$(document).ready(function () {
  console.log(getTotalStages());
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
        if (num > answer.length) {
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text:
              "You only need " +
              answer.length +
              " steps to complete this puzzle!",
          });
          $("#option_selected").sortable("cancel");
          $("#option_selected li:last-child").remove();
        } else {
          $("#direction_num").text(num + "/" + answer.length);
        }
      },
    })
    .disableSelection();

  //setInterval(checkQueue, 3000);

  $(".clear").on("click", function (e) {
    clearSteps();
  });

  // TODO: function for processing step button
  $(".step").on("click", function (e) {});

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

    // TODO: need to check whether the answer is correct before executing waypoint
    // reflect_waypoint();

    // Format data nicely to be sent to backend
    var steps = [];
    for (var i = 0; i < idsInOrder.length; i++) {
      var step = {
        step_number: i + 1,
        direction: idsInOrder[i],
      };
      steps.push(step);
    }

    // TODO: modify ur send step
    solvePuzzle(idsInOrder);
  });

  //   setInterval(checkQueue, 3000);
});

function clearSteps() {
  $("#option_selected li").remove();
  $("#direction_num").text("0/" + answer.length);
}
/**
 * Check the game stage and display the "step" button if the stage is 1, 2 or 3
 */
function displayStepButton() {
  if (stage <= 3) {
    document.getElementById("puzzlebutton").innerHTML +=
      "<button type='button' class='step flex m-3 pl-10 bg-yellow-400 bg-opacity-50 hover:bg-yellow-300 py-4 px-8 shadow-lg rounded-lg'>Step</button>";
  }
}

/**
 * Set the position of the car waypoint based on the grid box position
 */
function setWaypointPosition(grid_ID, waypoint_ID) {
  var offset_t = document.getElementById(grid_ID).getBoundingClientRect().top;
  var offset_l = document.getElementById(grid_ID).getBoundingClientRect().left;
  document.getElementById(waypoint_ID).style.top = offset_t + 5 + "px";
  document.getElementById(waypoint_ID).style.left = offset_l + "px";
}

/**
 * Rotate the car waypoint
 */
function rotateWaypoint(waypoint_ID, degree) {
  document.querySelector(waypoint_ID).style.transform = degree;
}

/**
 * Create puzzle grid based on the puzzle retrieved from database
 */
function createPuzzleGrid(puzzle) {
  for (var i = 0; i < puzzle.length; i++) {
    for (var j = 0; j < puzzle[i].length; j++) {
      var rowname = "row" + (i + 1);
      if (flow.includes(puzzle[i][j])) {
        if (flow.indexOf(puzzle[i][j]) == 0) {
          document.getElementById(rowname).innerHTML +=
            "<td id='box" +
            puzzle[i][j] +
            "' class='customisedgreen border-2 border-gray-500 w-12 h-12'></td>";
        } else {
          document.getElementById(rowname).innerHTML +=
            "<td id='box" +
            puzzle[i][j] +
            "' class='bg-red-200 border-2 border-gray-500 w-12 h-12'></td>";
        }
      } else {
        document.getElementById(rowname).innerHTML +=
          "<td id='box" +
          puzzle[i][j] +
          "' class='bg-gray-100 border-2 border-gray-500 w-12 h-12'></td>";
      }
    }
  }
}

/**
 * Open the stage dropdown button
 */
function openDropdown(event, dropdownID) {
  let element = event.target;
  while (element.nodeName !== "BUTTON") {
    element = element.parentNode;
  }
  var popper = Popper.createPopper(
    element,
    document.getElementById(dropdownID),
    {
      placement: "bottom-start",
    }
  );
  document.getElementById(dropdownID).classList.toggle("hidden");
  document.getElementById(dropdownID).classList.toggle("block");
}

/**
 * Display the stages in the dropdown button according to the user current stage
 */
function displayStageDropdown(stage) {
  document.getElementById("currentStage").innerHTML = stage;
  for (var i = 1; i < 8; i++) {
    if (i <= stage) {
      document.getElementById("stageDropdown").innerHTML +=
        "<a href='#" +
        i +
        "' class='text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-gray-700 hover:bg-gray-100'>Stage " +
        i +
        "</a>";
    } else {
      document.getElementById("stageDropdown").innerHTML +=
        "<a class='text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-gray-700 bg-gray-200'>Stage " +
        i +
        "</a>";
    }
  }
}

/**
 * Load the puzzle grid and starting point of the car waypoint,
 * set the values for steps required and user current score
 * display the "step" button if game stage is below or equal to 3
 * display the stages in the dropdown button according to the current user game stage
 */
window.addEventListener("DOMContentLoaded", function () {
  createPuzzleGrid(puzzle);

  setWaypointPosition("box" + flow[0], "waypoint");
  rotateWaypoint("#waypoint", "rotate(-90deg)");

  document.getElementById("direction_num").innerHTML = "0/" + answer.length;
  document.getElementById("score").innerHTML = score;

  displayStepButton();
  displayStageDropdown(stage);
});

/**
 * Move the car waypoint according to the signal received from the car
 */
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));
async function reflect_waypoint(box) {
  var boxNum = box.num;
  var direction = box.direction;

  //   var count = 0;
  //   for (var x = 0; x < answer.length; x++) {
  if (direction == "F" || direction == "B") {
    // count++;
    setWaypointPosition("box" + boxNum, "waypoint");
    document.getElementById("box" + boxNum).style.backgroundColor = "#cded9d";
  } else if (direction == "L") {
    rotateWaypoint("#waypoint", "rotate(270deg)");
  } else if (direction == "R") {
    rotateWaypoint("#waypoint", "rotate(0deg)");
  }
  // await sleep(2000);
  //   }
}

/**
 * Checks if answer that user provided is same as
 * the answer that is stored in the database.
 *
 * @param {Array} directions
 * @returns true if answer is correct, false otherwise
 */
function checkAnswer(directions) {
  for (var i = 0; i < directions.length; i++) {
    if (directions[i] != answer[i]) {
      return false;
    }
  }
  return true;
}

/**
 * Ajax call to check if the answer is correct.
 */
function solvePuzzle(steps) {
  $.ajax({
    type: "POST",
    contentType: "application/json",
    url: `/api/puzzle/solve/${data.puzzle_id}`,
    data: JSON.stringify({ steps }),
    success: function (data, textStatus, jqXHR) {
      Swal.fire({
        icon: "success",
        title: "Your answer is correct!",
        text: "Sending commands to the car...Checkout the car movement physically!",
      });

      clearSteps();
      is_completed = false;
      interval = setInterval(checkQueue, 3000);
    },
    error: function (jqXHR) {
      Swal.fire({
        icon: jqXHR.responseJSON.icon,
        title: "Oops...",
        text: jqXHR.responseJSON.message,
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
    url: "/api/puzzle/check-queue",
    success: async function (data, textStatus, jqXHR) {
      var queue = data.queue ?? [];
      var box = getBox(queue);
      console.log(box);
      if (box) {
        reflect_waypoint(box);
      }
      if (data.is_empty && !is_completed) {
        is_completed = true;
        clearInterval(interval);

        await Swal.fire({
          icon: "success",
          title: "Yay, execution completed!",
          text: "The car have finished executing!",
        });

        updateScore();
      }
    },
  });
}

function updateScore() {
  $.ajax({
    type: "POST",
    url: "/api/puzzle/update-score",
    success: async function (data, textStatus, jqXHR) {
      if (stage <= (await getTotalStages())) location.href = "/puzzle";
      else {
        await Swal.fire({
          icon: "success",
          title: "Congratulations!",
          text: "You have completed all the stages!",
        });
        location.href = "/home";
      }
    },
  });
}

async function getTotalStages() {
  var data = $.ajax({
    type: "GET",
    url: "/api/puzzle/total",
  });

  return data?.total;
}

/**
 * Retrieve the box number and direction
 * to be reflected on the car waypoint.
 *
 * @param {Array} queue from database.
 * @returns box object
 */
function getBox(queue) {
  if (queue.length === remainingSteps.length) return null;

  var box = {};

  box.direction = remainingSteps[0];
  box.num = remainingBoxes[0];

  if (box.direction == "F" || box.direction == "B") {
    remainingBoxes.shift();
  } else {
    box.num = prevBox.num;
  }

  remainingSteps.shift();

  if (box) prevBox = box;
  return box;
}
