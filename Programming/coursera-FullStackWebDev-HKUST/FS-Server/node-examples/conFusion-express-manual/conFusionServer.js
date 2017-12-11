var express = require('express'),
    morgan = require('morgan');
var dishRouter = require('./dishRouter');
var promoRouter = require('./promoRouter');
var leaderRouter = require('./leaderRouter');

var hostname = 'localhost';
var port = 4000;

var app = express();
// Morgan is used for logging messages in the server side
app.use(morgan('dev'));

app.use('/dishes', dishRouter);
app.use('/promotions', promoRouter);
app.use('/leadership', leaderRouter);

app.use(express.static(__dirname + '/public'));

app.listen(port, hostname, function() {
    console.log(`Server running at http://${hostname}:${port}/`);
});
