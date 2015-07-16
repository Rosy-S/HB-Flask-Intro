from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
           <h1> <a href="/hello"> Hi this is the home page! </a> </h1>
        </body>
    </html>
    """

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/grt", method="GET">
                <label>What's your name? <input type="text" name="person"></label>
                <input type="submit"> <br>

            Compliment: 
                <select name="compliment">
                <option value="awesome">Awesome</option>
                <option value="terrific">Terrific</option>
                <option value="fantastic">Fantastic</option> 
                <option value="neato">Neato</option>
                <option value="fantabulous">Fantabulous</option>
                <option value="wowza">Wowza</option>
                <option value="oh-so-not-meh">Oh-so-not-meh</option>
                <option value="brilliant">Brilliant</option>
                <option value="ducky">Ducky</option>
                </select>
            </form>

        </body>
    </html>

    """

@app.route('/grt', methods=["POST"])
def greet_person():
    player = request.form.get("person")
    compliment_value = request.form.get("compliment")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky']


    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s , I think you're %s!
        </body>
    </html>""" % (player, compliment_value)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=False)
