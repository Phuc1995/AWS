'use strict';
var AWS = require("aws-sdk");
AWS.config.update({
    region: "us-east-2",
  });
var docClient = new AWS.DynamoDB.DocumentClient();

const Hapi = require('@hapi/hapi');

const init = async () => {

    const server = Hapi.server({
        port: 3000,
        host: 'localhost'
    });

    server.route({
        method: 'GET',
        path: '/{user}/{date}',
        handler: (request, h) => {
            var params = {
                TableName : "DATE",
                KeyConditionExpression: "USER1 = :user and DATE1 = :date",
                ExpressionAttributeValues: {
                    ":user":  request.params.user,
                    ":date": request.params.date,
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
            
        }
        
    });

    
    server.route({
        method: 'GET',
        path: '/test',
        handler: (request, h) => {
            const user = {
                firstName: 'John',
                lastName: 'Doe',
                userName: 'JohnDoe',
                id: 123
            }
    
            return "aaaaa";
        }
    });
    
    await server.start();
    console.log('Server running on %s', server.info.uri);
};

process.on('unhandledRejection', (err) => {

    console.log(err);
    process.exit(1);
});

init();