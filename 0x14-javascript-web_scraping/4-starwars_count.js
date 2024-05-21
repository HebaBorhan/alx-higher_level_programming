#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const actorId = '/people/18';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const content = JSON.parse(body);
    // Loop through each film and check if Wedge Antilles is present
    let count = 0;
    content.results.forEach((film) => {
      film.characters.forEach(character => {
        if (character.includes(actorId)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
