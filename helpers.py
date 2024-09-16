import requests

api_key_alpha = 'GOP2ERI734J12562'
url_alpha = 'https://www.alphavantage.co/query'

# Information to get from API
statements = ['OVERVIEW', 'INCOME_STATEMENT']

# function to call API
def call_api(company_symbol):
    data = []

    # Request different information and store in data
    for function in statements:
        parameters_alpha = {
            'function': function,
            'symbol': company_symbol,
            'apikey': api_key_alpha,
        }

        r = requests.get(url=url_alpha, params=parameters_alpha)
        raw_data = r.json()
        # store the data returned in a list called data
        data.append(raw_data)

    # Return the data containing two elements gotten from API
    return data


# Function to insesrt data into netten database
def insert_company(db, data):
    # Get specific information from the response gotten from API
    company_symbol = data[0]['Symbol']
    company_name = data[0]['Name']
    description = data[0]['Description']
    info = data[1]['annualReports']

    # Insert description into table description in database
    db.execute(
        "INSERT INTO description (company_symbol, description, company_name) VALUES (?, ?, ?)",
        company_symbol,
        description,
        company_name
    )

    # Insert into company_data the netincome of the company for past five years
    db.execute(
        "INSERT INTO company_data (company_symbol, feature, v2018, v2019, v2020, v2021, v2022) VALUES (?, ?, ?, ?, ?, ?, ?)",
        company_symbol,
        'netincome',
        int(info[4]['netIncome']),
        int(info[3]['netIncome']),
        int(info[2]['netIncome']),
        int(info[1]['netIncome']),
        int(info[0]['netIncome'])
    )

    # Insert into company_data the revenue of the company for past five years
    db.execute(
        "INSERT INTO company_data (company_symbol, feature, v2018, v2019, v2020, v2021, v2022) VALUES (?, ?, ?, ?, ?, ?, ?)",
        company_symbol,
        'revenue',
        int(info[4]["totalRevenue"]),
        int(info[3]["totalRevenue"]),
        int(info[2]["totalRevenue"]),
        int(info[1]["totalRevenue"]),
        int(info[0]["totalRevenue"])
    )
