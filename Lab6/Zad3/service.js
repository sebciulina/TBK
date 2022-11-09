const express = require('express')
const app = express()
const port = 3000

app.get('/cars', (req, res) => {
  res.send('cars')
})

app.post('/addCar', (req, res) => {
  res.send('Add car')
})

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})