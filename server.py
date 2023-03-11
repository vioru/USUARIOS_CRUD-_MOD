from flask_app import app

from flask import Flask, render_template, request, redirect

from flask_app.models.users import User

from flask_app.controllers import users_controllers

if __name__=="__main__":
    app.run(debug = True)