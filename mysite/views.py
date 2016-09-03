from django.apps import apps
from django.views import generic


#class applist(generic.ListView):
    # Got the list of your app here

    #then display it in the html

class applist(generic.ListView):
    template_name = 'polls/applist.html'
    print('aaaaa')
    print(apps.all_models)
    def get_queryset(self):
        """Return the last five published questions."""
        return apps.get_models()[:5]
