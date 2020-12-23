const express = require("express");
const app = express();

app.set("view engine", "ejs");

app.get("/", function(req, res) {
    res.render("index")
});

app.get("/about", function(req, res) {
    res.render("about")
});

app.get("/support", function(req, res) {
    res.render("support")
});

app.get("/faq", function(req, res) {
    res.render("faq")
});

app.get("/", function(req, res) {
    res.render("support")
});

app.get("*", function(req, res) {
    res.render("404")
});

app.listen(process.env.PORT, process.env.IP, function() {
    console.log("Server up!")
});
