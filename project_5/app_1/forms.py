from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    birthday = forms.DateField()
    appointment = forms.DateTimeField()
    check = forms.BooleanField()
    options_size = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=options_size)
    options_pizza = [('P','Peperoni'),('C',"Chicken"),('B',"Beef")]
    pizza = forms.MultipleChoiceField(choices=options_pizza)
