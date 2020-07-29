var express = require("express");
var theapp = express();
theapp.use(express.static('public'))

theapp.get("/url", (req, res, next) => {
 res.json(["this","is","my","test","server"]);
});


theapp.listen(3002, () => {
     console.log("Server running on port 3002");
});

