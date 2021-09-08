from flask import Blueprint, config
from flask.app import Flask
main = Blueprint('main',__name__)
from .import views,error

