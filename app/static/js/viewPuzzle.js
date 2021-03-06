const puzzle = [
  [1, 2, 3, 4, 5, 6, 7],
  [8, 9, 10, 11, 12, 13, 14],
  [15, 16, 17, 18, 19, 20, 21],
  [22, 23, 24, 25, 26, 27, 28],
  [29, 30, 31, 32, 33, 34, 35],
  [36, 37, 38, 39, 40, 41, 42],
  [43, 44, 45, 46, 47, 48, 49],
];
const puzzleName = data.name;
const answer = data.puzzle_steps;
const flow = data.puzzle_flow;
const level = data.difficulty;
const step = data.puzzle_steps.length;

/**
 * Convert string array to int array
 * @param {*} puzzle 
 */
function convertStringToInt(arr){
    for (var i = 0; i < arr.length; i++) {
        arr[i] = parseInt(arr[i]);      
    }
}
/**
 * Display puzzle grid based on the puzzle details retrieved from database
 */
function displayPuzzleGrid(puzzle) {
  for (var i = 0; i < puzzle.length; i++) {
    for (var j = 0; j < puzzle[i].length; j++) {
      var rowname = "row" + (i + 1);
      if (flow.includes(puzzle[i][j])) {
        if (puzzle[i][j] == flow[0]) {
          document.getElementById(rowname).innerHTML +=
            "<td id='box" +
            puzzle[i][j] +
            "' class='customisedgreen border-2 border-gray-500 w-12 h-12'>" +
            puzzle[i][j] +
            "</td>";
        } else {
          document.getElementById(rowname).innerHTML +=
            "<td id='box" +
            puzzle[i][j] +
            "' class='bg-red-200 border-2 border-gray-500 w-12 h-12'>" +
            puzzle[i][j] +
            "</td>";
        }
      } else {
        document.getElementById(rowname).innerHTML +=
          "<td id='box" +
          puzzle[i][j] +
          "' class='bg-gray-100 border-2 border-gray-500 w-12 h-12'>" +
          puzzle[i][j] +
          "</td>";
      }
    }
  }
}

/**
 * Display puzzle directions based on the puzzle details retrieved from database
 */
function displayPuzzleDirections(answer) {
  for (var i = 0; i < answer.length; i++) {
    if (answer[i] == "F") {
      document.getElementById("puzzleDirections").innerHTML +=
        "<li class='bg-blue-300 bg-opacity-60 border border-blue-400 p-3 m-3 shadow-lg rounded-lg'>Move Forward</li>";
    } else if (answer[i] == "B") {
      document.getElementById("puzzleDirections").innerHTML +=
        "<li class='bg-blue-400 bg-opacity-60 border border-blue-400 p-3 m-3 shadow-lg rounded-lg'>Move Backward</li>";
    } else if (answer[i] == "L") {
      document.getElementById("puzzleDirections").innerHTML +=
        "<li class='bg-indigo-300 bg-opacity-90 border border-indigo-400 p-3 m-3 shadow-lg rounded-lg'>Turn Left</li>";
    } else {
      document.getElementById("puzzleDirections").innerHTML +=
        "<li class='bg-purple-300 bg-opacity-90 border border-purple-400 p-3 m-3 shadow-lg rounded-lg'>Turn Right</li>";
    }
  }
}

/**
 * Display puzzle details based on the puzzle details retrieved from database
 */
function displayPuzzleDetails() {
  document.getElementById("puzzleName").innerHTML = puzzleName;
  document.getElementById("puzzleLevel").innerHTML = level;
  document.getElementById("puzzleSteps").innerHTML = step;
  document.getElementById("shapeSteps").innerHTML = flow.toString();
}

/**
 * Display puzzle details in the view puzzle page
 */

window.addEventListener("load", function () {
    convertStringToInt(flow);
    displayPuzzleGrid(puzzle);
    displayPuzzleDirections(answer);
    displayPuzzleDetails();
});
