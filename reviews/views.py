from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Review
from .forms import ReviewForm

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Your response was noted."

        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review


class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST['review.id']
        fav_review = Review.objects.get(pk=review_id)
        request.session["favourite_review"] = fav_review
        return HttpResponseRedirect("/reviews/" + review_id)
