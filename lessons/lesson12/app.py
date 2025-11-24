from flask import (Flask, 
                   url_for, 
                   redirect, 
                   request)


my_app = Flask(__name__)


@my_app.route("/")
def show_users_home():
    return "List of users"


@my_app.route("/user/<name>")
def show_user(name):
    if name == "admin":
        return redirect(url_for("show_users_home"))
    return f"Single user details for {name}"

@my_app.route("/user/<name>/<int:repeat>", methods=["GET", "POST"])
def show_users(name, repeat):
    if request.method == "POST":
        return f"POST request received for {name*repeat}"
    else:
        return f"Single user details for {name*repeat}"


    


if __name__ == "__main__":
    with my_app.test_request_context():
        print(url_for("show_users_home"))
        print(url_for("show_user", name="John"))
        print(url_for("show_users", name="John", repeat=3))


    my_app.run(debug=True)
    print("Stop server ...")
    # my_app.run(host="0.0.0.0", port=80)