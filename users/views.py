from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from app.models import Question
from .models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

class ProfileView(ListView):
    template_name = 'profile.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        user = self.request.user
        print(user)
        return Question.objects.get(user=user.id)          