/* global $ WebSocket */

$(function () {
  function recieveMessage(e) {
    $('#bufOut').append('<p>' + e.data + '</p>');
  }

  var ws = new WebSocket('ws://' + window.location.host + '/socket');
  ws.onmessage = recieveMessage;

  $('#btnSend').click(function () {
    ws.send($('#bufIn').val());
    $('#bufIn').val('');
  });
});