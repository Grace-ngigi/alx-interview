#!/usr/bin/node
// prints all caracters of certain star war movie

const request = require('request');
const movieId = process.argv[2];

const params = {
  url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  method: 'GET'
};

request(params, (error, response, body) => {
  if (!error) {
    const caractersList = JSON.parse(body).characters;
    printCaracter(caractersList);
  }
});

function printCaracter (characters) {
  for (let idx = 0; idx < characters.length; idx++) {
    request(characters[idx], function (error, response, body) {
      if (!error) {
        console.log(JSON.parse(body).name);
      }
    });
  }
}
