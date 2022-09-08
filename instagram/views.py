from rest_framework import generics
from django.views.generic import CreateView
from .models import InstaUser
from .serializer import InstaUserSerializer
from .forms import InstaUSerForm

# Create your views here.
class InstaUserLoginAPIView(generics.CreateAPIView):
    queryset = InstaUser
    serializer_class = InstaUserSerializer


class InstaUserLoginView(CreateView):
    form_class = InstaUSerForm
    template_name = 'home.html'

