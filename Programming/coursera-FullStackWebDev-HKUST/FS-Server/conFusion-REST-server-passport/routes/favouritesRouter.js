var express = require('express'),
    bodyParser = require('body-parser');
var mongoose = require('mongoose');

var Favourites = require('../models/favourites');
var Verify = require('./verify');

var favouritesRouter = express.Router();
favouritesRouter.use(bodyParser.json());

favouritesRouter.route('/')
.get(Verify.verifyOrdinaryUser, function(req, res, next) {
    Favourites.find({postedBy: req.decoded._id}).populate('postedBy').populate('dishes')
        .exec(function(err, fav) {
            if(err) return next(err);
            res.json(fav);
    });
})
.post(Verify.verifyOrdinaryUser, function(req, res, next) {
    
    Favourites.find({postedBy: req.decoded._id}, function(err, fav) {
        if(err) return next(err);
        if(!fav.length) {
            Favourites.create({"postedBy": req.decoded._id, 
                                "dishes":[req.body._id]}, function(err, fav) {
                if(err) return next(err);
                console.log('Favourite created!');
                res.json(fav);
            });
        } else {
            console.log("Dish array - " + fav[0].dishes);
            console.log("New fav - " + req.body._id);
            var idx = fav[0].dishes.indexOf(req.body._id);
            if (idx == -1) {
                fav[0].dishes.push(req.body._id);
                fav[0].save(function(err, resp) {
                    if(err) return next(err);
                    console.log('Added given favourite dish!');
                    res.json(resp);
                });
            } else {
                var err = new Error('Dish already there in favourites');
                err.status = 403;
                return next(err);
            }
        }
    });
})
.delete(Verify.verifyOrdinaryUser, function(req, res, next) {
    Favourites.remove({postedBy: req.decoded._id}, function(err, resp) {
        if(err) return next(err);
        res.json(resp);
    });
});

favouritesRouter.route('/:dishId')
.delete(Verify.verifyOrdinaryUser, function(req, res, next) {
    Favourites.find({postedBy: req.decoded._id}, function(err, fav) {
        if(err) return next(err);
        var idx = fav[0].dishes.indexOf(req.params.dishId);
        if (idx == -1) {
            var err = new Error('Dish not there in favourites');
            err.status = 403;
            return next(err);
        }
        fav[0].dishes.splice(idx, 1);
        fav[0].save(function(err, resp) {
            if(err) return next(err);
            console.log('Removed given favourite dish!');
            res.json(resp);
        });
    });
});

module.exports = favouritesRouter;
