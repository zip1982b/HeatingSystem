$(function(){
	$(".thumbnails a").attr('rel', 'gallery').fancybox();

	$("#nav-list li, #scroll_up").click(function(e) {
		e.preventDefault();
		 $('html, body').animate({
				scrollTop: $($(this).children("a").attr("href")).offset().top
		 },1500);
	 });
 });

//отображение какую температуру выбрали
function outputUpdate(vol) {
	document.querySelector('#volume').value = vol;
}

// web socket
$(document).ready(function(){
            namespace1 = '/test1'; // change to an empty string to use the global namespace
            //namespace2 = '/test2'; // change to an empty string to use the global namespace
            // the socket.io documentation recommends sending an explicit package upon connection
            // this is specially important when using the global namespace
            // убрал io.connect оставил io
            // возможно здесь проиходит подключение к серверу !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            var socket1 = io.connect('http://' + document.domain + ':' + location.port + namespace1);
            //var socket2 = io.connect('http://' + document.domain + ':' + location.port + namespace2);



            // event handler for server sent data
            // the data is displayed in the "Received" section of the page
            // здесь мы принимаем все ответы(данные) от сервера*********************************************
            socket1.on('Server response', function(msg) {
               // $('#log').append('<br>Received #' + msg.count + ': ' + msg.data);
                $('#log_test1').text('Received #' + msg.count + ': ' + msg.data);
            });

            //**********************************************************************************************






            // event handler for new connections - обработчик события
            // не отвечает за само соединение, только когда произошло событие connect, тогда отсылаем сообщение

            socket1.on('connect', function() {
                //socket1.emit("server receives data", user);
                //var user = { "name": "Вася", "age": 35, "isAdmin": false, "friends": [0,1,2,3] };
                socket1.emit("server receives data", {data: 'Client is connected! test1'}); //{data: 'Client is connected! test1'}
            });

            // handlers for the different forms in the page
            // these send data to the server in a variety of ways
            $('form#emit').submit(function(event) {
                socket1.emit('server receives data', {data: $('#selectDay').val()});
                console.log({data: $('#selectDay').val()});
                return false;
            });




        });