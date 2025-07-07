from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<h1>Hi</h1>
<h2>상품목록</h2>
<div>
    <ul>
        <li>아메리카노</li>
        <li>카푸치노</li>
    </ul>
</div>
"""


if __name__ == '__main__':
    app.run(debug=True, port = 5050)