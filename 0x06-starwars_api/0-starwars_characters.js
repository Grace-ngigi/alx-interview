#!/usr/bin/node
// prints all caracters of certain star war movie

const request = require('request');
const movie_id = process.argv[2];

const params = {
url :`https://swapi-api.alx-tools.com/api/films/${movie_id}`,
method: 'GET'
};

request(params, (error, response, body) => {
  if (!error) {
    const caracters_list = JSON.parse(body).characters;
    printCaracter(caracters_list);
  }
});

function printCaracter(characters) {
   for (let idx = 0; idx < characters.length; idx++) {
      request(characters[idx], function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
