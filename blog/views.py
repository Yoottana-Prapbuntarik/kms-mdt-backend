from django.shortcuts import render, redirect
from .models import BlogCategory
from django.shortcuts import render
from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase

config = {
    "apiKey": "AIzaSyA5WKXEARihj0QcbtV12AYMFqMUe7hux4M",
    "authDomain": "kms-media.firebaseapp.com",
    "projectId": "kms-media",
    "storageBucket": "kms-media.appspot.com",
    "messagingSenderId": "3397243878",
    "appId": "1:3397243878:web:1e2367dd9527a60ccbbc27",
    "measurementId": "G-9P1DZPRLK5",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def uploadFileCategory(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_save = default_storage.save(file.name, file)
        storage.child("img-category/" + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        img_url = storage.child("img-category/" + file.name).get_url(None)
        ct = {
        'content': img_url
        }
        return render(request, "check.html", ct)
    