var mongoose = require('mongoose'),
    assert = require('assert');

var Leaderships = require('./models/leadership');

// Connection URL
var url = 'mongodb://localhost:27017/conFusion';
mongoose.connect(url);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error: '));
db.once('open', function() {
    // we are connected
    console.log('Connected correctly to the server');

    // create a new leadership
    Leaderships.create({
        name: 'Peter Pan',
        image: 'images/alberto.png',
        designation: 'Chief Epicurios Officer',
        abbr: 'CEO',
        description: 'Our CEO, Peter,...',
    }, function(err, leadership) {
        if (err) throw err;
        console.log('Leadership created');
        console.log(leadership);

        var id = leadership.id;

        // get all leaderships
        setTimeout(function() {
            Leaderships.findByIdAndUpdate(id, {
                    $set: {
                        description: 'Yeh aadmi kaun hai re baba',
                        abbr: 'Nautanki'
                    }
                }, {
                    new: true
                }
            ).exec(function(err, leadership) {
                if (err) throw err;
                console.log('Updated Leadership!');
                console.log(leadership);

                db.collection('leaderships').drop(function () {
                    db.close();
                });
            });
        }, 3000);
    });
});
