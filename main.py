from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from database import Database



app = Flask(__name__)
app.secret_key = "your_secret_key"

db = Database()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        comma_integers = request.form['comma_integers']
        single_integer = int(request.form['single_integer'])

        comma_integers_list = [int(x.strip()) for x in comma_integers.split(',')]

        # Check if single_integer exists in comma_integers_list
        result = single_integer in comma_integers_list

        # Sort and store comma_integers_list in the database
        sorted_comma_integers = sorted(comma_integers_list)
        db.store_comma_integers(user_id=session.get('user_id'), input_value=','.join(map(str, sorted_comma_integers)))

        success_message = "Data stored successfully."

        return render_template('home.html', result=result, success_message=success_message)

    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_tuple = db.get_user_by_email(email)
        if user_tuple and user_tuple[3] == password:
            session['user_id'] = user_tuple[0]
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        existing_user = db.get_user_by_email(email)
        if existing_user:
            return render_template('register.html', error_message="Email already exists")
        user_id = db.create_user(name, email, password)
        session['user_id'] = user_id
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/api/get_input_values', methods=['GET'])
def api_get_input_values():
    start_datetime = request.args.get('start_datetime')
    end_datetime = request.args.get('end_datetime')
    user_id = request.args.get('user_id')

    input_values_data = db.get_input_values_by_time_range(start_datetime, end_datetime, user_id)

    response_data = {
        "status": "success",
        "user_id": user_id,
        "payload": input_values_data
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
