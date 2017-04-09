var autobahn = require('./node_modules/autobahn');
var fs = require('fs')
var logger = fs.createWriteStream('poloData.txt', {
  flags: 'a'
})

// Autobahn Material

var poloUri = "wss://api.poloniex.com";

var connection = new autobahn.Connection({
  url: poloUri,
  realm: "realm1"
});


connection.onopen = function (session) {
  function trollboxEvent (args, kwargs) {
    logger.write(args.toString(" ") + "\n");
    
  }

  session.subscribe('trollbox', trollboxEvent);
}  

  connection.onclose = function () {
    console.log("Closed connection");
  }

connection.open();

