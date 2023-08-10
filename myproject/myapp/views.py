from django.shortcuts import render,redirect
from .models import contact1,Post
from .forms import ContactForm
from django.views import generic
# Create your views here.



def About(request):
 return render(request, 'About.html')
     
def index(request):
  return render(request, 'index.html')
def contact(request):
                 
         if request.method=="POST":
          #cont=contact.objects.all()
           form=ContactForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect("sucess")
         form = ContactForm()
         context = {'form': form}
         
         return render(request, 'contact.html')



class post_list(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class post_detail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'







    


      
    


