from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html" # this is an expected name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works !'
        return context

class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs): # This method defines the context that will be set for the template
        context = super().get_context_data(**kwargs)
        loaded_review = self.object # This special "object" property in this class will give us access to the automaticaly loaded review
        request = self.request # This special "request" property in this class will give us access to the request
        favorite_id = request.session.get('favorite_review') # This is the currently stored favorite ID
        context['is_favorite'] = favorite_id == str(loaded_review.id) # This compares if the loaded review ID is the same as the favorite review's ID
        # By default the loaded_review is a int, but we need it to be a string
        return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context

class AddFavoriteView(View):
    def post(self, requests):
        review_id = requests.POST['review_id'] # Getting the review id
        requests.session['favorite_review'] = review_id # Storing the review id in a session
        return HttpResponseRedirect('/reviews/' + review_id) # Redirecting

# OBS: Data stored in a session must contain simple data(strings, numbers, booleans, dictionaries)
# DO NOT STORE OBJECTS ! Like functions or classes