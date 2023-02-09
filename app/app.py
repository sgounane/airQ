from flask import Flask, render_template
app=Flask(__name__)
@app.route("/chaari")
def home():
    name="Chaari"
    return "<h1>bonjour "+name+"</h1><h2>titre2</h2><p>un texte .........</p>"

app.run(debug=True)