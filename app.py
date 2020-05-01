from flask import Flask, render_template

app=Flask("__name__")

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/chatbot")
def chatbot():
    return '<iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/64e2e662-a9b4-4a69-96da-53b0ac877e1f"></iframe>'

if __name__=="__main__":
    app.run(debug=True)
