// grab the things we need
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// create a Schema
var favouritesSchema = new Schema({
		postedBy: {
			type: mongoose.Schema.Types.ObjectId,
			ref: 'User'
		},
		dishes: [{type: mongoose.Schema.Types.ObjectId, 
				require: true, 
				ref: 'Dish'}]
	},
	{ timestamps: true }
);

// the schema is useless so far
// we need to create a model for using it
var Favourites = mongoose.model('Favourites', favouritesSchema);

// make this available to our Node applications
module.exports = Favourites;
