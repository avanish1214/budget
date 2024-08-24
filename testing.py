import sqlite3

# Connect to your SQLite database
sql_con = sqlite3.connect('payment_table.db')
cur = sql_con.cursor()

# Query to fetch data
cur.execute("SELECT sender, reciever, amount, date FROM payments")
rows = cur.fetchall()

# Calculate total spent
total_spent = sum(row[2] for row in rows)

# Generate the table rows dynamically
table_rows = ""
for row in rows:
    table_rows += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>${row[2]:.2f}</td>
            <td>{row[3]}</td>
        </tr>
    """

# Assuming you have a query for upcoming payments




# HTML template
html_template = """
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Budget Management Dashboard</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f7f6;
            margin: 0;
            padding: 0;
        }

        .container {
            display: flex;
            flex-direction: row;
            margin: 20px;
        }

        .content {
            flex: 3;
            margin-right: 20px;
        }

        .sidebar {
            flex: 1;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .header {
            margin-bottom: 30px;
        }

        h1 {
            color: #333;
            font-size: 28px;
            margin-bottom: 10px;
        }

        .total-spent {
            font-size: 20px;
            color: #3498db;
            margin-bottom: 30px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }

        .upcoming-payments {
            margin-top: 20px;
        }

        .payment {
            margin-bottom: 15px;
            padding: 10px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .payment h4 {
            margin: 0 0 5px 0;
            font-size: 16px;
            color: #333;
        }

        .payment p {
            margin: 0;
            color: #777;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="content">
            <div class="header">
                <h1>Hi, {username} </h1>
                <div class="total-spent">
                    Total Amount Spent This Month: $<span id="total-amount">{total_spent:.2f}</span>
                </div>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Sender</th>
                        <th>Receiver</th>
                        <th>Amount Paid</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody id="transaction-table">
                    {table_rows}
                </tbody>
            </table>
        </div>

        <div class="sidebar">
            <h3>Upcoming Payments</h3>
            <div class="upcoming-payments" id="upcoming-payments">
                
            </div>
        </div>
    </div>
</body>

</html>
"""

# Fill the template with dynamic data
html_content = html_template.format(
    username="avanish",
    total_spent=total_spent,
    table_rows=table_rows,
    #upcoming_payments=upcoming_payments
)

# Write the HTML content to a file
with open("transaction_table.html", "w") as html_file:
    html_file.write(html_content)

# Close the database connection
sql_con.close()
