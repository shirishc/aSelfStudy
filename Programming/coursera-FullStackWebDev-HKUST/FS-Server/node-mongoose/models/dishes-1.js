// grab the things we need
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// create a Schema
var dishSchema = new Schema({
        name: {
            type: String,
            required: true,
            unique: true
        },
        description: {
            type: String,
            required: true
        },
    },
    {
        timestamps: true
    }
);

// the schema is useless so far
// we need to create a model for using it
var Dishes = mongoose.model('Dish', dishSchema);

// make this available to our Node applications
module.exports = Dishes;
