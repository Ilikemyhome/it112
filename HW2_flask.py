from flask import Flask, render_template, request, jsonify, redirect, url_for
from HW5 import Dream_Cars, tables




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
tables.init_app(app)


# HW6 converting data to JSON format


@app.route("/api/cars", methods=["GET"])
def get_data():
    data = Dream_Cars.query.all()
    data_list = [item.to_dict() for item in data]
    return jsonify(data_list)


@app.route("/api/cars", methods=["POST"])
def add_car():
    try:
        data = request.get_json()

        if not all(key in data for key in ("make", "model", "year", "color")):
            return jsonify({"error": "Missing data"}), 400
        
        new_car = Dream_Cars(
            make=data["make"],
            model=data["model"],
            year=data["year"],
            color=data["color"]
        )

        tables.session.add(new_car)
        tables.session.commit()
        return jsonify({"message": "Car added successfully!"}), 201
    
    except Exception as e:
        return jsonify({"error":"Failed to add car"}), 500


@app.route("/cars")
def cars():
    
    return render_template("cars.html", cars = Dream_Cars.query.all())

@app.route("/cars/<int:car_id>")
def car_details(car_id):
    car = Dream_Cars.query.get(car_id)
    return render_template("car_details.html", car=car)

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