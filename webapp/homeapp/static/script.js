// script.js
// get the canvas element and its context
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
// initialize some variables for drawing
var drawing = false; // whether the mouse is pressed
var prevX = 0; // previous x coordinate
var prevY = 0; // previous y coordinate
var currX = 0; // current x coordinate
var currY = 0; // current y coordinate

// add event listeners for mouse events
canvas.addEventListener('mousedown', function(e) {
    // set drawing to true and update the coordinates
    drawing = true;
    prevX = currX;
    prevY = currY;
    currX = e.clientX - canvas.offsetLeft;
    currY = e.clientY - canvas.offsetTop;
});

canvas.addEventListener('mousemove', function(e) {
    if (drawing) {
        // update the coordinates and draw a line
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        currY = e.clientY - canvas.offsetTop;
        draw();
    }
});

canvas.addEventListener('mouseup', function(e) {
    // set drawing to false
    drawing = false;
});

canvas.addEventListener('mouseout', function(e) {
    // set drawing to false
    drawing = false;
});

function draw() {
    // draw a line from the previous to the current coordinates
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.closePath();
}

// get the save button element
var save = document.getElementById('save');

// add an event listener for click event
save.addEventListener('click', function(e) {
    // get the canvas data as a base64 string
    var data = canvas.toDataURL();
    // send a POST request to the save view with the data as a parameter
    $.post('/save', {data: data}, function(response) {
        // alert the response from the server
        alert(response);
    });
});
