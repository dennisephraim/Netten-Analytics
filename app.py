from cs50 import SQL
from flask import Flask, render_template, request, jsonify
from flask_session import Session

from helpers import call_api, insert_company

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///netten.db")

# Show homepage when user visits webpage
@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/get_data", methods=["GET", "POST"])
def get_data():
    """Get stock quote."""
    # If user visits via post
    if request.method == "POST":
        # Get symbol from user input
        quote = request.get_json()

        # Get symbol from database
        description = db.execute(
            "SELECT * FROM description WHERE company_symbol = ?", quote
        )

        # Get data from api if symbol is None
        if not description:
                # Get data from api
                company_data = call_api(quote)

                # Insert data into database
                insert_company(db, company_data)
                # Reset description using company gotten from api request
                description = db.execute(
                    "SELECT * FROM description WHERE company_symbol = ?", quote
                )

        # Get revenue row from database
        revenue = db.execute(
            "SELECT * FROM company_data WHERE company_symbol = ? and feature = ?", quote, "revenue"
        )

        # Get income row from database
        netincome = db.execute(
            "SELECT * FROM company_data WHERE company_symbol = ? and feature = ?", quote, "netincome"
        )
        # Above queries return a list with one element
        # Assign to the first element in list
        revenue = revenue[0]
        netincome = netincome[0]
        description = description[0]

        # Data to be passed to the script.js via fetch
        data_points = [{"x": (netincome['v2018'], netincome['v2019'], netincome['v2020'], netincome['v2021'], netincome['v2022']),
                        "y": (2018, 2019, 2020, 2021, 2022)},
                        {"x": (revenue['v2018'], revenue['v2019'], revenue['v2020'], revenue['v2021'], revenue['v2022']),
                        "y": (2018, 2019, 2020, 2021, 2022)},
                        {"description": description['description']}]

        # Return jsonified format of data_points
        return jsonify(data_points)

    # Render analysis if request via get
    return render_template("analysis.html")

# Show analysis page
@app.route("/analysis", methods=["GET", "POST"])
def display():
    return render_template("analysis.html")
