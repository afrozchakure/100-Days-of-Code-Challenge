// jshint esversion:6

// This is 'use fruitsDB' code if we want to use mongodb with our application

const MongoClient = require('mongodb').MongoClient; // MongoDB Driver to connect to our datbase
const assert = require('assert'); // assert is used to validate our data entry to mongodb database

// Connection URL
const url = 'mongodb://localhost:27017'; // Port is always similar

// Database Name
const dbName = 'fruitsDB';

// Create a new MongoClient (it'll connect with MongoDb database)
const client = new MongoClient(url, { useUnifiedTopology: true });

// Use connect method to connect to the Server
client.connect(function(err) {
    assert.equal(null, err);
    console.log("Connected successfully to server"); // If connection is successful

    const db = client.db(dbName);

    // Only once its done inserting our documents, do we close the connection to our database
    /*    insertDocuments(db, function() {
            client.close();
        });
    */

    // It'll find the records in our database
    findDocuments(db, function() {
        client.close();
    });
});

// To insert new Documents
const insertDocuments = function(db, callback) {
    // Get the documents collection
    const collection = db.collection('fruits');
    // Insert some documents (We create an array of fruits to insert then into collection 'fruits')
    collection.insertMany([{
            name: 'Apple',
            score: 8,
            review: 'Great fruit'
        },
        {
            name: 'Orange',
            score: 6,
            review: "Kinda sour"
        },
        {
            name: 'Banana',
            score: 9,
            review: 'Great stuff!'
        }
    ], function(err, result) { // Used for validation (Non-fatal assertion failure - simply alerts that assertion has failed)
        assert.equal(err, null); // Make sure there no errors when we inserted into the documents
        assert.equal(3, result.result.n); // Make sure we have 3 results inserted into our collection
        assert.equal(3, result.ops.length);
        console.log("Inserted 3 documents into the collection"); // Successfull
        callback(result);
    });
}


// Read the documents in our node.js app
const findDocuments = function(db, callback) {
    // Get the documents collection
    const collection = db.collection('fruits');
    // Find some documents
    collection.find({}).toArray(function(err, fruits) { // Its gonna "find all" and save it to an "array"
        assert.equal(err, null);
        console.log("Found the following records");
        console.log(fruits) // Log fruits into the console
        callback(fruits);
    });
}