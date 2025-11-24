from flask import (Flask, 
                   url_for, 
                   redirect, 
                   request,
                   render_template)


from modals import generate_random_user


USERS = generate_random_user(10)



my_app = Flask(__name__)


@my_app.route("/")
def show_users_home():

    return render_template("users_list.html", users=USERS)


@my_app.route("/create_user", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")
        new_user = {"name": name, "email": email, "age": age}
        if any(user.email == email for user in USERS):
            data = {
                "error": "Email already exists!",
                "data": new_user
            }
            return render_template("create_user.html", error_data=data)
        USERS.append(new_user)
        return redirect(url_for("show_users_home"))
    return render_template("create_user.html")

@my_app.route('/users/<user_email>')
def view_user_details(user_email):
    # Пошук користувача за email
    user = None
    for user in USERS:
        if user.email == user_email:
            user = user
            break
    
    if user is None:
        # Якщо користувача не знайдено, повертаємо помилку 404
        return render_template('user_details.html', user=None), 404
    
    # Якщо користувача знайдено, передаємо його дані в темплейт
    return render_template('user_details.html', user=user)



@my_app.route('/users/<user_email>/delete', methods=['POST'])
def delete_user(user_email):
    for user in USERS:
        if user.email == user_email:
            USERS.remove(user)
            break
    return redirect(url_for('show_users_home'))
    


if __name__ == "__main__":
    # with my_app.test_request_context():
    #     print(url_for("show_users_home"))
    #     print(url_for("show_user", name="John"))
    #     print(url_for("show_users", name="John", repeat=3))


    my_app.run(debug=True)
    print("Stop server ...")
    # my_app.run(host="0.0.0.0", port=80)