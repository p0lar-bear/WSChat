<!DOCTYPE html>
<html>
<head>
  <title>WebSocket Chat</title>
  {% for css in css_incl %}
  <link href="/css/{{ css }}.css" type="text/css" rel="stylesheet">
  {% end %}
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  {% for js in js_incl %}
  <script src="/js/{{ js }}.js" type="text/javascript"></script>
  {% end %}
</head>
<body>
  <input type="text" id="bufIn"> <button id="btnSend">Send</button>
  <div id="bufOut"></div>
</body>
</html>
