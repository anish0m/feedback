from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Username cannot be enpty!",
                "max_length": "Please enter a shorter username."
            }
            # "review_text": {
            #     # 
            # },
            # "rating": {
            #     # 
            # }
        }
