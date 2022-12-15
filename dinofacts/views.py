from datetime import datetime
from django.shortcuts import render

# Create your views here.
def show_dino(request, temp_name):
        data = {
        "dinosaurs": [
            "Tyrannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops",
        ],
        "now": datetime.now(),
    }
        return render(request, temp_name + ".html",data)
