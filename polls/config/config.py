from django.shortcuts import render
import pyrebase
 
config={
    apiKey: "AIzaSyBc10ugt9naJF8inUrXolzyIqYwRetmXjg",
    authDomain: "eng-ver-2.firebaseapp.com",
    databaseURL: "https://eng-ver-2-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "eng-ver-2",
    storageBucket: "eng-ver-2.appspot.com",
    messagingSenderId: "11804727838",
    appId: "1:11804727838:web:e6dfa01e1a7a2d2bdaec0f"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
