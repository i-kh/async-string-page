/**
 * Created by ikharitonova on 14.09.17.
 */

const STOP = "Stop it!";
const GO = "Ok. Go again.";



function createWebSocket(){
    try{
        var sock = new WebSocket('ws://' + window.location.host + '/ws');
    }
    catch(err){
        var sock = new WebSocket('wss://' + window.location.host + '/ws');
    }
    sock.onmessage = function(event) {
        showString(event.data);
    };
    return sock;
}

function showString(randomString) {
    var stringElem = $('#random_string');
    stringElem.empty();
    stringElem.append($('<p>').html(randomString));
}

function refreshButtonHandler(socket, timerId){
    var btn = $('#stop_btn');
    btn.off('click');
    btn.on('click', {'socket': socket, 'timerId': timerId}, sendStopMessage);
}

function sendStopMessage(event){
    switch(event.originalEvent.srcElement.innerText) {
        case STOP: {
            sendMessage(event.data.socket,'stop');
            clearTimeout(event.data.timerId);
            event.originalEvent.srcElement.innerText = GO;
            break;
        }
        case GO: {
            var sock = createWebSocket();
            var timerId = startMessageSending(sock);
            event.originalEvent.srcElement.innerText = STOP;
            refreshButtonHandler(sock, timerId);
            break;
        }
    }
}

function sendMessage(socket, message) {
    socket.send(message);
}


function startMessageSending(socket){
   return setInterval(function() {
       sendMessage(socket, 'refresh')
   }, 1000);
}

function init(){
    var sock = createWebSocket();
    var timerId = startMessageSending(sock);
    refreshButtonHandler(sock, timerId);
}

init();
