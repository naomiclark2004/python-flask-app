from flask import Flask, render_template, request
from  random import sample
app = Flask("__name__")

@app.route("/")
@app.route("/madlib/", methods=["GET", "POST"])
def madlib():
    if request.method == "POST":
        arr = request.form.values()
        input = []
        for value in arr:
            input.append(value)

        text = f"But {input[0]}! What light through yonder {input[1]} breaks? It is the East, and Juliet is the {input[2]}! Arise, fair sun, and {input[3]} the envious moon, Who is already sick and {input[4]} with grief, That thou her {input[5]} art far more fair than she. Be not her {input[5]}, since she is envious. Her vestal livery is but sick and green, And none but fools do {input[6]} it. Cast it off. It is my lady; O, it is my {input[7]}! O that she knew she were! She {input[8]}, yet she says nothing. What of that? Her {input[9]} discourses; I will answer it. I am too {input[10]}; `tis not to me she {input[8]}. Two of the fairest stars in all the {input[11]}, Having some business, do entreat her {input[9]} To {input[12]} in their {input[13]} till they return. What if her {input[9]} were there, they in her head? The {input[14]} of her cheek would shame those stars, As daylight doth a lamp; her {input[9]} in {input[11]} Would, through the airy {input[15]}, stream so bright That {input[16]} would sing and think it were not night. See how she leans her cheek upon her {input[17]}! O that I were a glove upon that {input[17]}, That I might touch that cheek!"
        return render_template('index.html', result=text)
    return render_template("index.html")

@app.route("/scramble/", methods=["GET", "POST"])
def scramble():
    if request.method == "POST":
        new_word = " "
        input = request.form.get('words')
        words = input.split()
        punct = (".", ";", "!", "?", ",") 
        for word in words:
            if len(word) > 3:
                word1 = word[1:-1] 
                word1 = sample(word1, len(word1)) 
                word1.insert(0, word[0]) 
                word1.append(word[-1]) 
                new_word = new_word + ''.join(word1) + " " 
            else: 
                new_word = new_word + word + " "
         
        return render_template("scramble.html", scrambled = new_word, words = input)
    return render_template("scramble.html")


@app.route("/about/", methods=["GET", "POST"])
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)