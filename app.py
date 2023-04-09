from flask import Flask, Response, request, session, render_template, redirect, make_response
import requests
import random
from datetime import timedelta

app = Flask(__name__,static_folder="static")

# Session Handling
app.secret_key = "_#SampleAppCapstone$%" 
app.session_cookie_name = "Sample_session"
app.permanent_session_lifetime = timedelta(minutes=30)

def import_word():
    with open("static/words.txt","r",encoding="utf-8") as file:
        content=file.read()
    dict_array=content.splitlines()
    return dict_array

@app.route("/logout", methods=["GET"])
def clear():
    session.clear()
    return redirect("/")

@app.route("/resetscore")
def resetcookie():
    resp=make_response(redirect("/logout"))
    resp.set_cookie("score_cookie","0")
    return resp

@app.route("/reset-highscore")
def resethighscore():
    resp=make_response(redirect("/"))
    resp.set_cookie("highscore_cookie","0")
    return resp

@app.route("/", methods=["GET"]) # map the URL "/" for a function below
def begin():
    # read dict 
    try:
        if session.get("word", None) == None:
            dict_array=import_word()
            session["word"] = dict_array[random.randint(0, len(dict_array) - 1)]
            session["history"] = list()

    except requests.exceptions.RequestException: # just handle exceptions regarding HTTP
        return Response("Something went wrong to retrieve data", mimetype='text/plain')

    lenWord=str(len(session["word"]))Fail
    print("------------------------------\nWord is :",session["word"])
    # print(lenWord,"letters (begin1)")
    score=request.cookies.get("score_cookie")
    highscore=request.cookies.get("highscore_cookie")

    if score==None and highscore==None:
        score="0"
        highscore="0" 
    elif score==None:
        score="0"
    elif highscore==None:
        highscore="0"

    resp=make_response(render_template("wordle.html", current="", word=session["word"], history=session["history"], lenWord=lenWord,warn="",wordleft="6",score=score,highscore=highscore))
    resp.set_cookie("score_cookie",score)
    resp.set_cookie("highscore_cookie",highscore)
    return resp

@app.route("/", methods=["POST"]) # map the URL "/" for a function below
def ontheway():
    wordleftIn=6
    query = request.form["query"].lower()
    score=request.cookies.get("score_cookie")
    highscore=request.cookies.get("highscore_cookie")
    score=int(score)
    highscore=int(highscore)

    try:
        dict_array=import_word()
        word = session["word"]
        history = session["history"]
        lenWord = len(word)

        if len(query)>lenWord:
            query=query[:lenWord]
        elif len(query)<lenWord:
            warn=f"Your guess word is shorter than {lenWord} letters, try again."
            print("len",len(history),history)
            wordleftIn=6-len(history)
            return render_template("wordle.html", current=query, word=word, history=history, lenWord=lenWord, warn=warn, wordleft=wordleftIn, score=score, highscore=highscore)
        
        if query not in dict_array:
            warn="Your guess word is not in Dictionary !! Try again."
            wordleftIn=6-len(history)
            return render_template("wordle.html", current=query, word=word, history=history, lenWord=lenWord, warn=warn, wordleft=wordleftIn, score=score, highscore=highscore)
        history.append(query)
        historyLen=len(history)
        session["history"] = history
        wordleftIn-=historyLen
        if wordleftIn<=0 and query!=word:
            resp=make_response(render_template("wordle.html", current=query, word=word, history=history, lenWord=lenWord, warn="Game over, try again!", wordleft=f"{wordleftIn} -- Answer is {word} --", score=0, highscore=highscore, reset=1))
            resp.set_cookie("score_cookie","0")
            return resp

        if query == word:
            score+=1
            if score>highscore:
                highscore=score
            resp=make_response(render_template("wordle.html", current=query, word=word, history=history, lenWord=lenWord, warn="",wordleft=wordleftIn,score=score,highscore=highscore))
            # score=request.cookies.get("score_cookie")
            resp.set_cookie("score_cookie",str(score))
            resp.set_cookie("highscore_cookie",str(highscore))
            session.clear()
            return resp
        else:
            return render_template("wordle.html", current=query, word=word, history=history, lenWord=lenWord, warn="", wordleft=wordleftIn, score=score, highscore=highscore)
    except Exception as e: # pylint: disable=broad-except
        print(e)
        return Response("Something went wrong to retrieve data: " + str(e), mimetype='text/plain')


if __name__=="__main__":
    app.run()