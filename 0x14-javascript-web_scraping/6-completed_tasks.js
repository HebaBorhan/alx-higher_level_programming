#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const tasksCompleted = {};

  body.forEach(todo => {
    if (todo.completed) {
      tasksCompleted[todo.userId] = (tasksCompleted[todo.userId] || 0) + 1;
    }
  });

  console.log(tasksCompleted);
});
