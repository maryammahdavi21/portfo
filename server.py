from flask import Flask, render_template, url_for, request, send_from_directory, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

# ***** so much dynamic than bellow!
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode ='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

import csv

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')
# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/practices.html")
# def practice():
#     return render_template('practices.html')


# @app.route("/lawyers.html")
# def lawyers():
#     return render_template('lawyers.html')

# @app.route('/news.html')
# def news():
#     return render_template('news.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/post.html')
# def post():
#     return render_template('post.html')

# @app.route('/singlepost.html')
# def single_post():
#     return render_template('singlepost.html')