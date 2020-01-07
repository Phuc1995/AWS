'use strict';
var AWS = require("aws-sdk");
AWS.config.update({
    region: "us-east-2",
});

console.log(parseFloat(1578367802.019376))
var docClient = new AWS.DynamoDB.DocumentClient();
const Hapi = require('@hapi/hapi');
const init = async () => {
    const server = Hapi.server({
        port: 3000,
        host: 'localhost'
    });

    server.route({
        method: 'GET',
        path: '/api/oneday/{postId}/{id}',
        handler: (request, h) => {

            var params = {
                TableName: "Comment",
                KeyConditionExpression: "postId = :postId and id = :id",
                ExpressionAttributeValues: {
                    ":postId": parseInt(request.params.postId),
                    ":id": parseFloat(request.params.id),
                }
            };
            const promise = new Promise((resolve, reject) => {
                docClient.query(params, function (err, data) {
                    if (!err) {
                        console.log(typeof(result))
                        console.log("Query succeeded.");
                        data.Items.forEach(function (item) {
                            var result = item.postId + " " + item.id + " " + item.email;
                            resolve(result)
                        });
                    } else {
                        console.error("Unable to query. Error:", JSON.stringify(err, null, 2));
                    }
                });
            });
            return promise
        }
    });

    server.route({
        method: 'GET',
        path: '/api/postId/{postId}',
        handler: (request, h) => {

            var params = {
                TableName: "Comment",
                KeyConditionExpression: "postId = :postId",
                ExpressionAttributeValues: {
                    ":postId": parseInt(request.params.postId),
                }
            };
            const promise = new Promise((resolve, reject) => {
                docClient.query(params, function (err, data) {
                    if (!err) {
                        var result = [] 
                        console.log("Query succeeded.");
                        data.Items.forEach(function (item) {
                            result.push(item.postId + " " + item.id + " " + item.email)
                        });
                        resolve(result)
                    } else {
                        console.error("Unable to query. Error:", JSON.stringify(err, null, 2));
                    }
                });
            });
            return promise
        }
    });

    server.route({
        method: 'GET',
        path: '/api/query/{postId}/{id1}/{id2}',
        handler: (request, h) => {

            var params = {
                TableName: "Comment",
                KeyConditionExpression: "postId = :postId and id between :id1 and :id2",
                ExpressionAttributeValues: {
                    ":postId": parseInt(request.params.postId),
                    ":id1": parseFloat(request.params.id1),
                    ":id2": parseFloat(request.params.id2),
                },
                ScanIndexForward : false
            };
            const promise = new Promise((resolve, reject) => {
                docClient.query(params, function (err, data) {
                    if (!err) {
                        var result = [] 
                        console.log("Query succeeded.");
                        data.Items.forEach(function (item) {
                            result.push(item.postId + " " + item.id + " " + item.email)
                            console.log(item.postId + " " + item.id + " " + item.email)
                        });
                        resolve(result)
                    } else {
                        console.error("Unable to query. Error:", JSON.stringify(err, null, 2));
                    }
                });
            });
            return promise
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