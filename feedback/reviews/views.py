from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == "POST":
        enered_username = request.POST['username'] #Extracting the data enetered in the form
        # Validating the data :
        if enered_username == "" and len(enered_username) >= 100:
            return render(request, "reviews/review.html", {
                "has_error": True
            })
        print(enered_username)
        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html", {
        "has_error": False
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")
