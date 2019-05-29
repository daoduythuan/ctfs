var net = require('net');

flag='fake_flag';

var server = net.createServer(function(socket) {
	socket.on('data', (data) => { 
		//m = data.toString().replace(/[\n\r]*$/, '');
		ok = true;
		arr = data.toString().split(' ');
		console.log(arr);
		console.log("arr get http header");
		//arr get http header
		console.log(Number);
		arr = arr.map(Number);

		console.log(arr);
		if (arr.length != 5) 
			console.log("if arr.length != 5");
			console.log(arr.length);
			console.log(arr);
			ok = false;
		console.log("ok: ",ok);
		/* make http heard = 5*/
		//[ 'GET',
  //'HTTP/1.1\r\nHost:',
  //'127.0.0.1:23333\r\nUser-Agent:',
  //'Mozilla/5.0',
  //'(Macintosh;',
  //'Intel',
  //'Mac',
  //'OS',
  //'X',
  //'10.13;',
  //'rv:51.0)',
  //'Gecko/20100101',
  //'Firefox/51.0\r\nAccept:',
  //'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:',
  //'en-US,en;q=0.5\r\nAccept-Encoding:',
  //'gzip,',
  //'deflate\r\nConnection:',
  //'keep-alive\r\nUpgrade-Insecure-Requests:',
  //'1\r\nCache-Control:',
  //'max-age=0\r\n\r\n' ]


		arr1 = arr.slice(0);
		console.log("arr1=arr.slice(0)");
		console.log(arr1);
		arr1.sort();
		console.log(arr1);
		for (var i=0; i<4; i++)
			if (arr1[i+1] == arr1[i] || arr[i] < 0 || arr1[i+1] > 127) //a[1] = a[0], a[0] < 1,
				ok = false;
				console.log("for i, i < 4");
				console.log("ok: ",ok);
		arr2 = []
		for (var i=0; i<4; i++)
			arr2.push(arr1[i] + arr1[i+1]);
		val = 0;
		for (var i=0; i<4; i++)
			val = val * 0x100 + arr2[i];
		if (val != 0x23332333)
			ok = false;
		if (ok)
			socket.write(flag+'\n');
		else
			socket.write('nope\n');
	});
	//socket.write('Echo server\r\n');
	//socket.pipe(socket);
});

HOST = '0.0.0.0'
PORT = 23333

server.listen(PORT, HOST);
