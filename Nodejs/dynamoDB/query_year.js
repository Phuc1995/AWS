var AWS = require("aws-sdk");

AWS.config.update({
  region: "us-east-2",
});

var docClient = new AWS.DynamoDB.DocumentClient();

var date = "2"
var user = "USER2"

console.log("Querying : ");

var params = {
    TableName : "DATE",
    KeyConditionExpression: "#USER1 = :user and #DATE1 = :date",
    ExpressionAttributeNames: {
        "#USER1":"USER1",
        "#DATE1":"DATE1"
    },
    ExpressionAttributeValues: {
        ":user": user,
        ":date": date,
    }
};

docClient.query(params, function(err, data) {
    if (err) {
        console.error("Unable to query. Error:", JSON.stringify(err, null, 2));
    } else {
        console.log("Query succeeded.");
        data.Items.forEach(function(item) {
            console.log(" -", item.USER1 + ": " + item.DATE1);
        });
    }
});