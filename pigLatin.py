import flask
app = flask.Flask(__name__) 


@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

@app.route("/pigLatin", methods = ['GET', 'POST'])
def formPage():
    html = "<html> <body> <h1> Pig Latin Creator </h1>" + HTMLForm()
    if flask.request.method == 'GET':
        html += "<p> Enter a name </p>"

    if flask.request.method == "POST":
        sentenceToMakePigLatin = flask.request.form["pigLatinInput"]
        html +="<p> Original: " + sentenceToMakePigLatin + "</p>"
        html +="<p> Check it out: " + pigLatin(sentenceToMakePigLatin) + "</p>"
    html += "</body> </html>"
    return html

def HTMLForm():
    form = """
        <form action="pigLatin" method = "post"> Add your name:
            <br>
            <input type="text" name="pigLatinInput"  size = "50"> 
            <br>
            <input type="submit" value="Submit">
        </form> """

    return form 
        

def pigLatin(original):
    first = original[:1]
    new = original[1:]
    
    if len(original) > 0:
        return new + first + "ay"
    else:
        return "please enter a name" 

if __name__ == "__main__":
    app.run()
