from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from . forms import ProfileForm
from . models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# def store_file(file):
#     with open("temp/222222.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             'form': form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES['user_image'])
#             #This acceses "user_image" on the incoming files and we store that file as a value in the image field of my UserProfile
#             # "user_image" is the identifier because our form is now rendered with our "form" class and now that class uses "user_image" as a fieldname for the FileField
#             #store_file(request.FILES["image"]) #".FILES"a special property offered by Django which gives us access to uploaded files
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#         else:
#             return render(request, "profiles/create_profile.html", {
#                 'form': submitted_form
#             })