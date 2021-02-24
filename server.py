from flask import Flask, render_template, url_for, request,redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
# @app.route()
def my_home():
    # def hello_world(username=None, post_id=None):
    # print(url_for('static', filename='favicon.ico'))
    return render_template('index.html')
    # return render_template('./index.html')
    # return 'Hello, Jehovah Jireh!'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
    # return 'Hello, Jehovah Jireh!'

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
    # with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return 'form submitted hooorayyyy'
    # return render_template('login.html', error=error)
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # print(data)
            return redirect('/thankyou.html')
            #return 'form_submitted'
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'
        # data = request.form['message']

# @app.route('/works.html')
# def work():
#     return render_template('./works.html')
# return 'Hello, Jehovah Jireh!'


# @app.route('/contact.html')
# def work():
#     return render_template('./contact.html')
# return 'Hello, Jehovah Jireh!'
# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs!'

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my dog!'
