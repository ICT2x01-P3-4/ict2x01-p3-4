const puzzle = [
  [1,2,3,4,5,6,7],
  [8,9,10,11,12,13,14],
  [15,16,17,18,19,20,21],
  [22,23,24,25,26,27,28],
  [29,30,31,32,33,34,35],
  [36,37,38,39,40,41,42],
  [43,44,45,46,47,48,49]
];
// TODO: need to retrieve puzzle, score, and stage from db (no need answer and flow bcus user can see in javascript)
var dbPuzzleName = "Test puzzle name";
var dbPuzzleLevel = 3;
var dbPuzzleStep = 6;
answer = ["F","F","R","F","L","F"];
flow = [31,24,17,18,11];

/**
* Create puzzle grid 
*/
function createPuzzleGrid(puzzle){
    for (var i=0; i < puzzle.length; i++){
        for (var j=0; j < puzzle[i].length; j++){
            var rowname = "row" + (i+1);
            if (flow.includes(puzzle[i][j])){
                if (flow.indexOf(puzzle[i][j]) == 0){
                    document.getElementById(rowname).innerHTML += 
                    "<td id='box"+puzzle[i][j] + 
                    "' class='border-2 border-gray-500 w-12 h-12'>" + 
                    puzzle[i][j] +
                    "</td>";
                } else {
                    document.getElementById(rowname).innerHTML += 
                    "<td id='box"+puzzle[i][j] +
                    "' class='border-2 border-gray-500 w-12 h-12'>" +
                    puzzle[i][j] +
                    "</td>";
                }
            }else{
                document.getElementById(rowname).innerHTML += 
                "<td id='box"+puzzle[i][j] +
                "' class='border-2 border-gray-500 w-12 h-12'>" +
                puzzle[i][j] +
                "</td>";
            }
        }
    }
}

/**
* Display puzzle directions based on the puzzle details retrieved from database
*/
function displayPuzzleDirections(answer){
    for (var i=0; i < answer.length; i++){
        if (answer[i]=="F"){
            document.getElementById("option_selected").innerHTML += 
            "<li class='bg-blue-300 bg-opacity-60 border border-blue-400 p-3 m-3 shadow-lg rounded-lg'>Move Forward</li>";
        } else if (answer[i]=="B"){
            document.getElementById("option_selected").innerHTML += 
            "<li class='bg-blue-400 bg-opacity-60 border border-blue-400 p-3 m-3 shadow-lg rounded-lg'>Move Backward</li>";
        } else if (answer[i]=="L"){
            document.getElementById("option_selected").innerHTML += 
            "<li class='bg-indigo-300 bg-opacity-90 border border-indigo-400 p-3 m-3 shadow-lg rounded-lg'>Turn Left</li>";
        } else {
            document.getElementById("option_selected").innerHTML += 
            "<li class='bg-purple-300 bg-opacity-90 border border-purple-400 p-3 m-3 shadow-lg rounded-lg'>Turn Right</li>";
        }
    }
}

/**
* Display the maximum step for the puzzle direction according to the user input for steps required
*/      
function displayMaxStep(){
    document.getElementById("direction_max_num").innerHTML = document.getElementById("steps_required").value;
}

/**
* Display current puzzle details
*/               
window.addEventListener('DOMContentLoaded', function () {
    createPuzzleGrid(puzzle);
    displayPuzzleDirections(answer);
    document.getElementById("puzzle_name").value = dbPuzzleName;
    document.getElementById("diff_level").value = dbPuzzleLevel;
    document.getElementById("steps_required").value = dbPuzzleStep;
    document.getElementById("puzzle_flow").value = flow.toString(); 
    document.getElementById("direction_num").innerHTML = answer.length;
    displayMaxStep();
})

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
        var maxnum = document.getElementById("steps_required").value;
        if (num <= maxnum) {
            $("#direction_num").text(num);
        } else {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "You only selected "+maxnum+" steps to create the puzzle",
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

    $(".update").on("click", function (e) {
        var puzzleDirections = $("#option_selected").sortable("toArray");
        var puzzleName = document.getElementById("puzzle_name").value;
        var puzzleLevel = document.getElementById("diff_level").value;
        var stepsRequired = document.getElementById("steps_required").value;
        var puzzleFlow = document.getElementById("puzzle_flow").value.split(",");   
                
        // Verify whether all fields are filled in
        if (puzzleDirections.length == 0 || puzzleFlow.length == 0 || puzzleName.length == 0) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Please fill in all the input fields.",
                });
            return;
        }

        // Verify whether the number of puzzle direction boxes is the same as the number of steps required
        if(stepsRequired!=$("#option_selected li").length){
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Please ensure the number of puzzle direction boxes is the same as the number of step required",
                });
            return;
        }

        // Verify whether the puzzle shape is achievable with the puzzle directions defined
        const countOccurrences = (arr, val) => arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
        var numOfSteps = countOccurrences(puzzleDirections, "F");
        if(numOfSteps!=puzzleFlow.length){
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Please ensure the puzzle shape matches the puzzle direction",
                });
            return;
        }

        // TODO: in backend
        // double check whether all fields are null
        // diff level > 0 and < 8
        // steps required > 0 and < 16
        // puzzle flow: all elements is convertable to int (current puzzle flow format ["12","13","14"])
        // number of "F" in puzzleDirections = number of elements in puzzleFlow

        // Format data nicely to be sent to backend
        var steps = [];
        for (var i = 0; i < puzzleDirections.length; i++) {
            var step = {
            step_number: i + 1,
            direction: puzzleDirections[i],
            };
            steps.push(step);
        }

    });
});

// Decrement function for number counter
function decrement(e,dataaction,step){
    btn = e.target.parentNode.parentElement.querySelector(dataaction);
    target = btn.nextElementSibling;
    let value = Number(target.value);
    if (value > step){
        value--;
        target.value = value;
    }   
}

// Increment function for number counter
function increment(e,dataaction,step){
    btn = e.target.parentNode.parentElement.querySelector(dataaction);
    target = btn.nextElementSibling;
    let value = Number(target.value);
    if (value < step){
        value++;
        target.value = value;
    }
}