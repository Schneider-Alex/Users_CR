# from flask import Flask, render_template,request, redirect, session
# # import the class from friend.py
from flask_app import app
from flask_app.controllers import users

# from user import User

# app = Flask(__name__)
# app.secret_key = 'keep it secret, keep it safe'
# @app.route('/')
# def index():
#     users = User.get_all()
#     return render_template("index.html", all_users = users)

# @app.route('/newuserpage')
# def newuserpage():
#     return render_template("indexcreate.html")

# @app.route('/create_user', methods=["POST"])
# def create_friend():
#     session['createedit'] = 'create'
    # # First we make a data dictionary from our request.form coming from our template.
    # # The keys in data need to line up exactly with the variables in our query string.
    # data = {
    #     "fname": request.form["fname"],
    #     "lname" : request.form["lname"],
    #     "email" : request.form["email"]
    # }
    # # We pass the data dictionary into the save method from the Friend class.
    # User.save(data)
    # # Don't forget to redirect after saving to the database.
    # return redirect('/')

# @app.route('/users/<int:userid>')
# def showuser(userid):
#     data = {
#         "id" : userid
#     }
#     showuser=User.pull_one_user(data)
#     return render_template("indexshow.html", showuser=showuser)

# @app.route('/users/update/<int:userid>',methods=['POST'])
# def update(userid):
#     data = {
#         "id" : userid,
#         "first_name": request.form["fnameedit"],
#         "last_name" : request.form["lnameedit"],
#         "email" : request.form["emailedit"]
#     }
#     User.edituser(data)
#     return redirect ('/')


# @app.route('/users/<int:userid>/edit')
# def edit(userid):
#     data ={ 
#     "id": userid
#     }
#     return render_template("indexedit.html",user=User.pull_one_user(data)[0])

# @app.route('/users/<int:userid>/delete')
# def deleteuser(userid):
#     data={
#         "id": userid
#     }
#     User.clear_user_data(data)
#     return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)

