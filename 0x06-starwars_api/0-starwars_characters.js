#!/usr/bin/node
// prints all caracters of certain star war movie

const request = require('request');
const movieId = process.argv[2];

const params = {
  url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  method: 'GET'
};

request(params, async (error, response, body) => {
  if (!error) {
    const caractersList = JSON.parse(body).characters;
    for (const caractersUrl of caractersList) {
      const caracter = await printCaracter(caractersUrl);
      console.log(caracter.name);
    }
  }
});

function printCaracter (caractersUrl) {
  return new Promise((resolve, reject) => {
    request(caractersUrl, function (error, response, body) {
      if (error || response.statusCode !== 200) {
        console.error('Error fetching character details:', error);
        reject(error || response.statusCode);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData);
      }
    });
  });
}
