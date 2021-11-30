// TODO: need to retrieve puzzle, score, and stage from db (no need answer and flow bcus user can see in javascript)
const puzzle = [
        [1,2,3,4,5,6,7],
        [8,9,10,11,12,13,14],
        [15,16,17,18,19,20,21],
        [22,23,24,25,26,27,28],
        [29,30,31,32,33,34,35],
        [36,37,38,39,40,41,42],
        [43,44,45,46,47,48,49]
    ];
const answer = ["F","F","R","F","L","F"];
const flow = [31,24,17,18,11];
score = 123;
stage = 3;

/**
 * Set the position of the car waypoint based on the grid box position
 */
function setWaypointPosition(grid_ID,waypoint_ID){
    var offset_t = document.getElementById(grid_ID).getBoundingClientRect().top;
    var offset_l = document.getElementById(grid_ID).getBoundingClientRect().left;
    document.getElementById(waypoint_ID).style.top = offset_t+5+"px";
    document.getElementById(waypoint_ID).style.left = offset_l+"px";
}

/**
 * Rotate the car waypoint
 */
function rotateWaypoint(waypoint_ID,degree){
    document.querySelector(waypoint_ID).style.transform = degree;
}

/**
 * Create puzzle grid based on the puzzle retrieved from database
 */
function createPuzzleGrid(puzzle){
    for (var i=0; i < puzzle.length; i++){
        for (var j=0; j < puzzle[i].length; j++){
            var rowname = "row" + (i+1);
            if (flow.includes(puzzle[i][j])){
                if (flow.indexOf(puzzle[i][j]) == 0){
                    document.getElementById(rowname).innerHTML += "<td id='box"+puzzle[i][j]+"' class='customisedgreen border-2 border-gray-500 w-12 h-12'></td>";
                } else {
                    document.getElementById(rowname).innerHTML += "<td id='box"+puzzle[i][j]+"' class='bg-red-200 border-2 border-gray-500 w-12 h-12'></td>";
                }
            }else{
                document.getElementById(rowname).innerHTML += "<td id='box"+puzzle[i][j]+"' class='bg-gray-100 border-2 border-gray-500 w-12 h-12'></td>";
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
        document.getElementById(dropdownID),{
            placement: "bottom-start",
        }
    );
    document.getElementById(dropdownID).classList.toggle("hidden");
    document.getElementById(dropdownID).classList.toggle("block");
}

/**
 * Display the stages in the dropdown button according to the user current stage
 */
function displayStageDropdown(stage){
    document.getElementById("currentStage").innerHTML = stage;
    for (var i=1; i<8;i++){
        if (i<=stage) {
            document.getElementById("stageDropdown").innerHTML += "<a href='#"+i+"' class='text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-gray-700 hover:bg-gray-100'>Stage "+i+"</a>";
        } else {
            document.getElementById("stageDropdown").innerHTML += "<a class='text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-gray-700 bg-gray-200'>Stage "+i+"</a>";
        }
    }
}

/**
 * Load the puzzle grid and starting point of the car waypoint, 
 * set the values for steps required and user current score
 * display the "step" button if game stage is below or equal to 3
 * display the stages in the dropdown button according to the current user game stage
 */               
window.addEventListener('DOMContentLoaded', function () {

    createPuzzleGrid(puzzle);

    setWaypointPosition("box"+flow[0],'waypoint');
    rotateWaypoint("#waypoint","rotate(-90deg)");

    document.getElementById("direction_num").innerHTML = "0/"+answer.length;
    document.getElementById("score").innerHTML = score;

    displayStepButton();
    displayStageDropdown(stage);
})

/**
 * Move the car waypoint according to the signal received from the car
 */    
const sleep=(delay)=> new Promise((resolve)=> setTimeout(resolve,delay));
async function reflect_waypoint(){
    var count=0;
    for (var x=0;x<answer.length;x++){            
        if (answer[x] == "F" || answer[x] == "B") {
            count++;
            setWaypointPosition("box"+flow[count],'waypoint');
            document.getElementById("box"+flow[count]).style.backgroundColor = '#cded9d' ;
        } else if (answer[x] == "L") {
            rotateWaypoint("#waypoint","rotate(270deg)");
        } else if (answer[x] == "R") {
            rotateWaypoint("#waypoint","rotate(0deg)");
        }
        await sleep(2000);
    }
}

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
            if (num > answer.length) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "You only need "+answer.length+" steps to complete this puzzle!",
            });
            $("#option_selected").sortable("cancel");
            $("#option_selected li:last-child").remove();
            } else {
            $("#direction_num").text(num + "/"+answer.length);
            }
        },
    })
    .disableSelection();

    //setInterval(checkQueue, 3000);

    $(".clear").on("click", function (e) {
        $("#option_selected li").remove();
        $("#direction_num").text("0/"+answer.length);
    });

    // TODO: function for processing step button
    $(".step").on("click", function (e) {
        
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

        // TODO: need to check whether the answer is correct before executing waypoint
        reflect_waypoint();

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
        //sendSteps(steps);

    });
});
