import http.cookies
import os
import sqlite3

import server_internals
from server_internals import server_socket, server_address, server_port
from server_security import is_valid_token, register_user, login_user, get_session_id
from get_total import calculate_total

# All server stats or common variables should go here.
default_server_path = "./"
default_encoding = "utf-8"
default_server_read = 2048
default_headers = []
main_page = "/dashboard_main.html"
login_page = "/login.html"
register_page = "/register.html"
allowed_types = [".html", ""]
blocked_types = [".py", ".db"]
active_redirects = {}
session_params = {}


def find_user_tags(content):
    tags_to_replace = []
    current_tag = ""
    read_tag = False
    for i in range(1, len(content) - 1):
        if read_tag:
            current_tag += content[i]
            if content[i] == ">" and content[i - 1] == ">":
                tags_to_replace.append(current_tag[:-2])
                current_tag = ""
                read_tag = False
        else:
            if content[i] == "<" and content[i - 1] == "<":
                read_tag = True
    return tags_to_replace


def form_response(status_code=200, reason="OK", headers=default_headers, content=""):
    global default_encoding
    send_content = f"HTTP/1.1 {status_code} {reason}\r\n"
    if len(headers) > 0:
        send_content += "\r\n".join(headers) + "\r\n"
    send_content += "\r\n"
    if content:
        send_content += content
    return send_content.encode(default_encoding)


def read_cookies(request):
    request_cookies = {}
    cookie_lines = [http_header for http_header in request.split("\r\n")[:-1] if "Cookie: " in http_header]
    for cookie_line in cookie_lines:
        content = cookie_line[8:].split("; ")
        for cookie in content:
            key, value = cookie.split("=")
            request_cookies[key] = value
    return request_cookies


def replace_user_tags(content, tags_to_replace):
    for tag in tags_to_replace:
        if tag != "":
            if tag.lower() in session_params:
                content = content.replace(f"<<{tag}>>", session_params[tag.lower()])
            else:
                content = content.replace(f"<<{tag}>>", "")
    return content


def fetch_transactions():
    conn = sqlite3.connect('payment_table.db')
    cursor = conn.cursor()
    cursor.execute("SELECT sender, reciever, amount, date FROM payments")
    transactions = cursor.fetchall()
    conn.close()
    return transactions


def generate_transaction_html(transactions):
    rows = []
    for txn in transactions:
        row = f"<tr><td>{txn[0]}</td><td>{txn[1]}</td><td>Rs.{txn[2]:.2f}</td><td>{txn[3]}</td></tr>"
        rows.append(row)
    return "\n".join(rows)


def send_response(connection, resource, headers=default_headers):
    global allowed_types, blocked_types
    any_allowed = False
    any_blocked = False
    for allowed in allowed_types:
        if allowed in resource:
            any_allowed = True
    for blocked in blocked_types:
        if blocked in resource:
            any_blocked = True
    if any_allowed and not any_blocked:
        if resource in ["/" + name for name in os.listdir(default_server_path)]:
            if resource == main_page:
                resource_file = open(default_server_path + resource, 'r')
                response_content = resource_file.read()
                resource_file.close()
                tags_to_replace = find_user_tags(response_content)
                response_content=response_content.replace("<<username>>", values['username'])
                response_content=response_content.replace("<<totalamount>>", str(calculate_total()))
                tags_to_replace = find_user_tags(response_content)
                # Fetch transactions and generate HTML rows
                transactions = fetch_transactions()
                transaction_html = generate_transaction_html(transactions)
                response_content = response_content.replace("<<transaction_table>>", transaction_html)
                response_content = replace_user_tags(response_content, tags_to_replace)
                connection.send(form_response(content=response_content, headers=headers))
            else:
                resource_file = open(default_server_path + resource, 'r')
                response_content = resource_file.read()
                resource_file.close()
                tags_to_replace = find_user_tags(response_content)
                response_content = replace_user_tags(response_content, tags_to_replace)
                connection.send(form_response(content=response_content, headers=headers))
        else:
            connection.send(form_response(404, "Not found"))
    else:
        connection.send(form_response(403, "Unauthorized"))


def set_cookies(cookies):
    return str(http.cookies.SimpleCookie(cookies))


while 1:
    connection, client_address = server_socket.accept()
    request = connection.recv(default_server_read).decode(default_encoding)
    if request == "":
        continue
    main_request = request.split("\r\n")[0]
    resource = main_request.split(" ")[1]
    request_headers = request.split("\r\n")[:-1]
    request_content = request.split("\r\n")[-1]

    if "GET /favicon.ico" in main_request:
        favicon = open("favicon.ico", "rb")
        favimg = favicon.read()
        favicon.close()
        connection.send(favimg)
        connection.close()
        continue
    else:
        print(client_address[0], ":", client_address[1], "->", main_request, "[ ", end="")

    # All session stats or session variables should go here.
    session_params = {"sessionid": "", "username": ""}
    session_params.update(read_cookies(request))
    client_can_login = is_valid_token(session_params['sessionid'], session_params['username'])
    print("Authorized ]" if client_can_login else "Unauthorized ]")
    if client_can_login:
        # Authorized users can access any resource.
        if "GET" in main_request:
            if resource == "/":
                resource = main_page

            send_response(connection, resource)

        elif "POST" in main_request:
            # Forms will be handled here.
            pass

    else:
        if "GET" in main_request:
            # Unauthorized users can be served the login page as landing and the register page.

            if resource == "/register.html":
                resource = register_page

            elif resource == "/login.html":
                resource = login_page

            elif resource == "/":
                resource = login_page

            else:
                active_redirects[client_address[0]] = resource.replace("\"", "")
                print(f"WILL REDIRECT ON AUTH : {client_address[0]} -> {active_redirects[client_address[0]]}")
                resource = login_page

            send_response(connection, resource)

        elif "POST" in main_request:
            fields = request_content.split("&")
            values = dict([i.split("=") for i in fields])
            username = values["username"]
            password_hash = get_session_id("", values["password"])
            if "register" in values:
                successful_registration = register_user(username, password_hash)
                if successful_registration:
                    # Pass back login page with <<STATUS>> "Registered successfully"
                    session_params.update({"status": "Registered successfully"})
                    resource = login_page
                    send_response(connection, resource)

                else:
                    # Pass back registration page with <<STATUS>> "User already registered. Use the same account or create a new one."
                    session_params.update({"status": "User already registered. Use the same account or create a new one."})
                    resource = register_page
                    send_response(connection, resource)

            elif "login" in values:
                successful_login, session_id = login_user(username, password_hash)
                if successful_login:
                    # Return to redirect, or main page with headers set with cookies.
                    cookie_headers = set_cookies({'sessionid': session_id, 'username': username})
                    if client_address[0] in active_redirects:
                        print(f"AUTH REDIRECT : {client_address[0]} -> {active_redirects[client_address[0]]}")
                        resource = active_redirects[client_address[0]]

                    else:
                        resource = main_page

                    send_response(connection, resource, default_headers + [cookie_headers])

                else:
                    # Pass back login page with <<STATUS>> "Login failed. Try again with the right credentials."
                    session_params.update({"status": "Login failed. Try again with the right credentials."})
                    resource = login_page
                    send_response(connection, resource)

    connection.close()
