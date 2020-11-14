var express = require("express");
var app = express();

app.set("view engine", "ejs");

app.get("/", function(req, res) {
    res.render("index")
})

app.get("/about", function(req, res) {
    res.render("about")
})

app.get("/company", function(req, res) {
    res.render("company")
})

app.get("/why", function(req, res) {
    res.render("why")
})

app.get("/about", function(req, res) {
    res.render("about")
})

app.get("/hire", function(req, res) {
    res.render("hire")
})

app.get("*" , function(req, res){
    res.send("ERROR, CANNOT FIND PAGE")
})


app.listen(process.env.PORT, process.env.IP, function() {
    console.log("Server Up!")
})

// Index.js is done!