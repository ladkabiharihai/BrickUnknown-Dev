from django import forms
from  projects.models import project


class CreateprojectForm(forms.ModelForm):

    class Meta:
        model = project
        fields = ['ProjectName','category1','category2','category3','category4','category5','link','github','linedin','desc','image']
