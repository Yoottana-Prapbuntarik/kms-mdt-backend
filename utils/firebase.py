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
# /img-category
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
def uploadToClound(file):
  storage = firebase.storage()
  storage.child("img-category/" + file.name).put("media/" + file.name)
  delete = default_storage.delete(file.name)
  img_url = storage.child("img-category/" + file.name).get_url(None)