const express = require('express')
// from flask import Flask 랑 유사하다고 보면 된다.

//app = Flask(__name__)
const app = express()

// @app.route('/')
// def index():
//     return 'hello world from flask'

app.get('/',(reg, res) =>{
    res.send('hello, world from node.js')
})


// app.run()
// 3000 => port 번호이다.
app.listen(3000, ()=>{
    console.log('서버가 준비되었음')
})

// python app.py
// node app.js