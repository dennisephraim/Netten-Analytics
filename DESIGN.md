# Design Overview

This document provides a design overview of the Financial analysis web application.

## Architecture

The application follows a client-server architecture with Flask serving as the backend server and providing RESTful APIs. The frontend is built using HTML, CSS, and JavaScript, with Chart.js for dynamic chart rendering.

## Components

### Flask Application

- **Server:** The main Flask application is structured in the `app` directory.
- **Routes:** The application has three main routes:
  - `/`: Home page with a form for entering data and a dynamic chart.
  - `/get_data`: Custom API endpoint to fetch user input from server and query database for company via user input.
  - `/analysis`: Separate page displaying a dynamic chart.
- **Database:** SQLite is used as the database to store data of companies.

### Frontend

- **HTML:** The `templates` directory contains HTML templates for the home page (`homepage.html`) and the anlysis page (`analysis.html`).
- **CSS:** The application uses minimal styling for a clean and responsive design.
- **JavaScript:** The `static/js` directory contains the `script.js` file responsible for handling interactions, including fetching data, updating the chart, and drawing the chart to the analysis page.

## Data Flow

1. User enters data in the input feild on the analysis page.
2. The user input is sent to the server using a POST request.
3. The server queries the SQLite database to return data containing the symbol given by the user. If symbol is not already in database, the server queries an api and stores the company information in the database.
4. The server responds with data, and the chart on the analysis page is dynamically updated using script.js.
5. Clicking the "Get Data" button draws charts on the analysis page.

## Database Model

The application gets data of company from an api called 'alphavantage'.
The data is stored in two tables: description and compnay_data.

This would work for companies that have information for the past five years

Below are structures for the two tables
TABLE description
    'company_symbol' = TEXT PRIMARY KEY NOT NULL
    'description' = TEXT
    'company_name' TEXT NOT NULL

TABLE company_data
    'id' = INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
    'company_symbol' = TEXT NOT NULL
    'feature' = TEXT NOT NULL
    'v2018' = INTEGER
    'v2019' = INTEGER
    'v2020' = INTEGER
    'v2021' = INTEGER
    'v2022' = INTEGER
