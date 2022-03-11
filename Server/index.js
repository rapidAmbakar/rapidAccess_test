const express = require('express')
const app = express();
const PORT = 3000;
var cors = require('cors')

app.use(cors())
app.get('/', (req, res) => {
    res.send('Hello World')
})
app.post('/api/images', (req, res) => {
    console.log(req);
    res.json({ 'status': 'TCS' });
});

app.listen(PORT, (err) => {
    console.log("Server Started");
});