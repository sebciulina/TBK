let http = require('http');
let options = {
    host: 'server',
    port: 9000,
    path: '/test'
};

http.get(options, function(res) {
    console.log("Got response: " + res.statusCode);
  
    res.on("data", function(chunk) {
      console.log("BODY: " + chunk);
    });
  }).on('error', function(e) {
    console.log("Got error: " + e.message);
  });