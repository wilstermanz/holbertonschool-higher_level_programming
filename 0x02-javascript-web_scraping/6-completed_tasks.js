#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, response, content) {
  if (err) {
    console.log(err);
  } else {
    const taskList = JSON.parse(content);
    const tasksByUser = {};
    for (const i in taskList) {
      if (taskList[i].completed === true) {
        if (!tasksByUser[taskList[i].userId]) {
          tasksByUser[taskList[i].userId] = 1;
        } else {
          tasksByUser[taskList[i].userId]++;
        }
      }
    }
    console.log(tasksByUser);
  }
});
