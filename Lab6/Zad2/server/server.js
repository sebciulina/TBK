const express = require('express');
const app = express();

app.get('/test', (req, res) => {
    res.send({test: 'test'});
});

app.listen(9000, '0.0.0.0', () => {
    console.log('Application listening at 0.0.0.0:9000');
})