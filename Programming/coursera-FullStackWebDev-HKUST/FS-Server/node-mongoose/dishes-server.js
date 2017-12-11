var mongoose = require('mongoose'),
    assert = require('assert');

var Dishes = require('./models/dishes');

// Connection URL
var url = 'mongodb://localhost:27017/conFusion';
mongoose.connect(url);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error: '));
db.once('open', function() {
    // we are connected
    console.log('Connected correctly to the server');

    // create a new dish
    Dishes.create({
        name: 'Uthapizza',
        image: 'images/uthapizza.png',
        category: 'mains',
        label: 'Hot',
        price: '4.99',
        description: 'Test',
        comments: [
            {
                rating: 3,
                comment: 'This is insane',
                author: 'Matt Daemon'
            },
            {
                rating: 5,
                comment: 'Imagine all the eatables, living in conFusion',
                author: 'John Lemon'
            }
        ]
    }, function(err, dish) {
        if (err) throw err;
        console.log('Dish created');
        console.log(dish);

        var id = dish.id;

        // get all dishes
        setTimeout(function() {
            Dishes.findByIdAndUpdate(id, {
                    $set: {
                        description: 'Updated Test',
                        label: 'Garam'
                    }
                }, {
                    new: true
                }
            ).exec(function(err, dish) {
                if (err) throw err;
                console.log('Updated Dish!');
                console.log(dish);

                dish.comments.push({
                    rating: 5,
                    comment: 'I\'m getting a sinking feeling!',
                    author: 'Leonardo di Carpaccio'
                });
                dish.save(function(err, dish) {
                    console.log('Updated Comments!');
                    console.log(dish);

                    db.collection('dishes').drop(function () {
                        db.close();
                    });
                });
            });
        }, 3000);
    });
});
