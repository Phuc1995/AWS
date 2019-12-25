var AWS = require("aws-sdk");
let awsConfig = {
    "region": "us-east-2"   
};
AWS.config.update(awsConfig);

let docClient = new AWS.DynamoDB.DocumentClient();

let save = function () {

    var input = {
        "Author": "Test", 
        "Title": "Test",
        "Category": "Test",
        "Formats": { "Test": "J4SUKVGU", "Test": "D7YF4FCX" }
    };
    var params = {
        TableName: "Books",
        Item:  input
    };
    docClient.put(params, function (err, data) {

        if (err) {
            console.log("users::save::error - " + JSON.stringify(err, null, 2));                      
        } else {
            console.log("users::save::success" );                      
        }
    });
}

save();
        