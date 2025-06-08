from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def hello_world():
    #Removed the return statement here
    return render_template('index.html') #Renders the index.html template

if __name__ == '__main__':
    app.run(debug=True)

