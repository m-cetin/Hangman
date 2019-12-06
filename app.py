from flask import Flask,render_template,redirect,request

import functions
  
app = Flask(__name__) 

secret_word = None
word_set = None
to_display = None
tries = None
blanks = None
  
@app.route('/') 
def hello_world(): 
    return render_template('home.html')


@app.route('/game')
def game():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	
	secret_word = functions.get_random_word()
	word_set = "abcdefghijklmnopqrstuvwxyz"
	blanks = 0
	to_display = []
	for i,char in enumerate(secret_word):
		if char==" ":
			to_display.append(" ")
			blanks+=1
		else:
			to_display.append("_")

	tries = 0
	return render_template('game.html',to_display=to_display,word_set=word_set,tries="/static/img/hangman%d.png"%tries)


@app.route('/add_char',methods=["POST"])
def add_char():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	

	letter = request.form["letter"]
	
	chance_lost = True
	for i,char in enumerate(secret_word):
		if char==letter:
			chance_lost = False
			to_display[i] = letter
			blanks-=1

	word_set = word_set.replace(letter,'')

	if chance_lost==True:
		tries += 1
		if tries==6:
			return redirect('/game_lost')

	if blanks==0:
		return redirect('/game_won')

	return render_template('game.html',to_display=to_display,word_set=word_set,tries="/static/img/hangman%d.png"%tries)


if __name__ == '__main__': 
    app.run() 