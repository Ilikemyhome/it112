from flask import Flask, render_template, request

app = Flask(__name__)


from flask import redirect, url_for

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        first_name = request.form.get("name")
        last_name = request.form.get("last_name")
        color = request.form.get("color")
        number = request.form.get("number")
        if first_name and last_name:
            
            return redirect(url_for('fortune', first_name=first_name, last_name=last_name, color=color, number=number))
    return render_template("home.html")

@app.route("/fortune", methods=["GET"])
def fortune():
    
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    color = request.args.get("color")
    number = request.args.get("number")

    fortunes = {
        
        "red": {
            "1": "A dream you have will come true.",
            "2": "Its better to be alone sometimes.",
            "3": "If you feel you are right, stand firmly by your convictions.",
            "4": "It may be difficult, but it will be worth it in the end.",
            "5": "You will be successful in your work.",

        },
        "yellow": {
            "1" : "Your future is as bright as a disco ball—get ready to dance through unexpected joy!",
            "2" : "Beware of flying tacos today; they may bring both hunger and surprise opportunities.",
            "3" : "Respect your elders. You could inherit a large sum of money.",
            "4" : "Your hard work will be rewarded.",
            "5" : "Open your mind and heat to good things",
        },
        "blue": {
            "1" : "Wealth awaits you very soon",
            "2" : "Move quickly. Now is the time to make progress.",
            "3" : "Lead by example, Not by words alone.",
            "4" : "Learn from your mistakes. Try not to make them again",
            "5" : "Its okay to say no sometimes.",
        },
        "green": {
            "1" : "Just have fun.",
            "2" : "Stop procrastinating. Make a decision already.",
            "3" : "Dont worry about the past. It is gone.",
            "4" : "Dont worry about what others think of you.",
            "5" : "Time to take a break.",
        }
    }
    return render_template("fortune.html", name=first_name, last_name=last_name,
                            color=color, number=number, fortune=fortunes[color][number])

@app.route("/about")
def about():
    return render_template("about.html")




if __name__ == "__main__":
    app.run(debug=True)