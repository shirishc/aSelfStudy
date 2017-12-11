var mongoose = require('mongoose'),
    assert = require('assert');

var Promotions = require('./models/promotions');

// Connection URL
var url = 'mongodb://localhost:27017/conFusion';
mongoose.connect(url);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error: '));
db.once('open', function() {
    // we are connected
    console.log('Connected correctly to the server');

    // create a new promotion
    Promotions.create({
        name: 'Weekend Grand Buffet',
        image: 'images/buffet.png',
        // label: 'New',
        price: '19.99',
        description: 'Sabko phokat mein khana',
    }, function(err, promotion) {
        if (err) throw err;
        console.log('Promotion created');
        console.log(promotion);

        var id = promotion.id;

        // get all promotions
        setTimeout(function() {
            Promotions.findByIdAndUpdate(id, {
                    $set: {
                        description: 'Khana nahin milega',
                        label: 'Naya'
                    }
                }, {
                    new: true
                }
            ).exec(function(err, promotion) {
                if (err) throw err;
                console.log('Updated Promotion!');
                console.log(promotion);

                db.collection('promotions').drop(function () {
                    db.close();
                });
            });
        }, 3000);
    });
});
