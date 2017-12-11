var express = require('express');
var userRouter = express.Router();
var passport = require('passport');
var User = require('../models/user');
var Verify = require('./verify');

/* GET users listing. */
userRouter.get('/', Verify.verifyOrdinaryUser, Verify.verifyAdmin, function(req, res, next) {
    User.find({}, function(err, user) {
        if(err) {
            return res.status(403).json({err: 'You are not authorised to perform this operation'});
        }
        res.json(user);
    });
})

userRouter.post('/register', function(req, res) {
    User.register(new User({username: req.body.username}), req.body.password,
        function(err, user) {
            if(err) {
                return res.status(500).json({err:err});
            }
            if(req.body.firstname) {
                user.firstname = req.body.firstname;
            }
            if(req.body.lastname) {
                user.lastname = req.body.lastname;
            }
            user.save(function(err, user) {
                passport.authenticate('local')(req, res, function() {
                    return res.status(200).json({status: 'Registration Successful'});
                });
            });
        }
    );
});

userRouter.post('/login', function(req, res, next) {
    passport.authenticate('local', function(err, user, info) {
        if(err) return next(err);
        if(!user) return res.status(401).json({err:info});

        req.logIn(user, function(err) {
            // console.log(err);
            if (err) return res.status(500).json({err: 'Could not log in user'});

            // var token = Verify.getToken(user); - No need to send the full user but just some required fields
            var token = Verify.getToken({"username":user.username, "_id":user._id,
                                        "admin":user.admin});
            res.status(200).json({
                status: 'Login successful',
                success: true,
                token: token
            });
        });
    })(req, res, next);
});

userRouter.get('/logout', function(req, res) {
    req.logout();
    res.status(200).json({status:'Bye!'});
});

// userRouter.get('/facebook', function(req, res, next) {
//     console.log("Here -2");            
//     passport.authenticate('facebook', function(err, user, info) {
//         console.log("Here -1");
//         if(err) return next(err);
//     })(req, res, next);
// });

userRouter.get('/facebook', passport.authenticate('facebook'), function(req, res){});

userRouter.get('/facebook/callback', function(req, res, next) {
    passport.authenticate('facebook', function(err, user, info) {
        if(err) return next(err);
        if(!user) return res.status(401).json({err:info});
        req.logIn(user, function(err) {
            // console.log(err);
            if (err) return res.status(500).json({err: 'Could not log in user'});

            // var token = Verify.getToken(user); - No need to send the full user but just some required fields
            var token = Verify.getToken(user);
            res.status(200).json({
                status: 'Login successful',
                success: true,
                token: token
            });
        });
    })(req, res, next);   
});

module.exports = userRouter;
