var AWS = require("aws-sdk");
let awsConfig = {
    "region": "us-east-2",
};
AWS.config.update(awsConfig);

let docClient = new AWS.DynamoDB.DocumentClient();

let modify = function () {

    var params = {
        TableName: "Books",
        Key: {
            "Author": "John Grisham",
            "Title": "The Rainmaker"
        },
        UpdateExpression: "set updated_by = :Author, is_deleted = :Value",
        ExpressionAttributeValues: {
            ":Author": "Phuc",
            ":Value": "New Update"
        },
        ReturnValues: "UPDATED_NEW"

    };
    docClient.update(params, function (err, data) {

        if (err) {
            console.log("users::update::error - " + JSON.stringify(err, null, 2));
        } else {
            console.log("users::update::success "+JSON.stringify(data) );
        }
    });
}

modify();
        