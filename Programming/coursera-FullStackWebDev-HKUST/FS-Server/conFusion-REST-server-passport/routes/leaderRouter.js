var express = require('express'),
    bodyParser = require('body-parser');
var mongoose = require('mongoose');

var Leaderships = require('../models/leadership');
var Verify = require('./verify');

var leaderRouter = express.Router();
leaderRouter.use(bodyParser.json());

leaderRouter.route('/')
.get(function(req, res, next) {
    Leaderships.find(req.query, function(err, leadership) {
        if(err) return next(err);
        res.json(leadership);
    });
})
.post(Verify.verifyOrdinaryUser, Verify.verifyAdmin, function(req, res, next) {
    Leaderships.create(req.body, function(err, leadership) {
        if(err) return next(err);
        console.log('Leadership created!');
        var id = leadership._id;

        res.writeHead(200, {'Content-Type':'text/plain'});
        res.end('Added the leadership with id: ' + id);
    });
})
.delete(Verify.verifyOrdinaryUser, Verify.verifyAdmin, function(req, res, next) {
    Leaderships.remove({}, function(err, resp) {
        if(err) return next(err);
        res.json(resp);
    });
});

leaderRouter.route('/:leaderId')
.get(function(req, res, next) {
    Leaderships.findById(req.params.leaderId, function(err, leader) {
        if(err) return next(err);
        res.json(leader);
    });
})
.put(Verify.verifyOrdinaryUser, Verify.verifyAdmin, function(req, res, next) {
    Leaderships.findByIdAndUpdate(req.params.leaderId, {$set: req.body}, {new: true},
        function(err, leader) {
        if(err) return next(err);
        res.json(leader);
    });
})
.delete(Verify.verifyOrdinaryUser, Verify.verifyAdmin, function(req, res, next) {
    Leaderships.findByIdAndRemove(req.params.leaderId, function(err, resp) {
        if(err) return next(err);
        res.json(resp);
    });
});

module.exports = leaderRouter;
