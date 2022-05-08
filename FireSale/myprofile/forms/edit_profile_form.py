# from django.forms import ModelForm, widgets
# from django import forms
#
# from myprofile.models import Users
#
#
# class edit_profile_form(ModelForm):
#     image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = Users
#         exclude = ['id', 'user', 'rating']
#         widgets = {
#             'bio': widgets.TextInput(attrs={'class': 'form-control'})
#         }