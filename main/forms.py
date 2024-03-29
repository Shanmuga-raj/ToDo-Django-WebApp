from django import forms

class TodoForms(forms.Form):
    text = forms.CharField(max_length=50,
            widget=forms.TextInput(
                attrs={'class' : 'form-control',
                        'placeholder' : 'Example: Go To GYM, CODE',
						'aria-label' : 'Todo',
                        'aria-describedby' : 'add-btn',
                }
            ))