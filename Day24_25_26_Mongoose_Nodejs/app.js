// jshint esversion:6

// This is 'use fruitsDB' code if we want to use mongodb with our application

const mongoose = require('mongoose');

// It will look for database fruitDB and if it doesn't exist, it will create it for us
mongoose.connect("mongodb://localhost:27017/fruitDB", { useNewUrlParser: true, useUnifiedTopology: true });

// Adding data using mongoose (Creating a Schema for mongoose model)
const fruitSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Please check your data entry, no name specified!"]
    },
    rating: {
        type: Number,
        min: 1,
        max: 10
    },
    review: String
});

// Specify singular word for your collection (it will plurarise automatically)
const Fruit = mongoose.model("Fruit", fruitSchema);

// Creating a document 'fruit' from a model 'Fruit'
const fruit = new Fruit({
    rating: 10,
    review: "Peaches are so yummy !!"
});

// Save the fruit document into a 'Fruit' collection inside our 'FruitDB'
// fruit.save()

// Schema Person
const personSchema = new mongoose.Schema({
    name: String,
    age: Number,
    favouriteFruit: fruitSchema

    // It tells mongoose that we are embedding a fruit document inside property called fruitSchema
});

const Person = mongoose.model("Person", personSchema);

const grape = new Fruit({
    name: "Grapes",
    score: 6,
    review: "Grapes are decent."
});

grape.save(); // Save pineapple into our fruits collection

const person = new Person({
    name: "Sam",
    age: 50,
    // favouriteFruit: mango
});

// Adding a relationship 'favouriteFruit' to person
Person.updateOne({ name: "Sam" }, { favouriteFruit: grape }, function(err) {
    if (err) {
        console.log(err);
    } else {
        console.log("Successfully updated the document");
    }
});

// person.save();

/*
// Inserting Data into database using Mangoose
const kiwi = new Fruit({
    name: "Kiwi",
    score: 10,
    review: "The best fruit!"
});

const orange = new Fruit({
    name: "Orange",
    score: 4,
    review: "Too sour for me"
});

const banana = new Fruit({
    name: "Banana",
    score: 3,
    review: "Weird Texture"
});
*/

// Insert an array of documents into our model

// Fruit.insertMany([kiwi, orange, banana], function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log("Successfully saved all the fruits to fruitsDB");
//     }
// });


// find() function accepts a callback
Fruit.find(function(err, fruits) {
    // If there are errors, log the errors else log the fruits
    if (err) {
        console.log(err);
    } else {
        mongoose.connection.close()
            // console.log(fruits);
            // for (let index = 0; index < fruits.length; index++) {
            //     console.log(fruits[index]['name']);
            // }

        // tap into array, it loops through each individual fruit out of the array
        fruits.forEach(function(fruit) {
            console.log(fruit.name);
        });
    }
});

// Update data in Mongoose
// Fruit.updateOne({ _id: "5f0eeef0c59e78594d559f22" }, { name: "Peach" }, function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log("Successfully updated the document");
//     }
// });

// Deleting a document using Mongoose (with callback function)
// Fruit.deleteOne({ name: "Peach" }, function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log("Successfully deleted the document");
//     }
// })

// Deleting the contents of people collections using Person model (with condition and callback)
// Person.deleteMany({ name: "John" }, function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log("Successfully the rows in people collections");
//     }
// });