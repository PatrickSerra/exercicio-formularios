from django import forms

BOOK_CHOICHES = (
    ('1', 'Deep Learning with Keras'),
    ('2', 'Web Development with Django'),
    ('3', 'Brave New World'),
    ('4', 'The Great Gatsby'),
)

BOOK_CHOICHES_OPT = (
    (
        'Non-Fiction', (
             ('1', 'Deep Learning with Keras'),
             ('2', 'Web Development with Django'),  
        ),
    ),
    
    (
        'Fiction', (
            ('3', 'Brave New World'),
            ('4', 'The Great Gatsby'),
         )
    )
)

RADIO_CHOICES = (
    ('Value One', 'Value One'),
    ('Value Two', 'Value Two'),
    ('Value Three', 'Value Three')
)
    

class ExampleForm(forms.Form):
    text_input = forms.CharField(max_length=3) # input de texto
    password_input = forms.CharField(widget=forms.PasswordInput, min_length=8) # input de senha
    checkbox_on = forms.BooleanField(required=False) #checkbox
    
    # Campos Select
 
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICHES) #Select
    #Select com grupo de opções
    favorite_book_with_choices = forms.ChoiceField(choices=BOOK_CHOICHES_OPT) 
     #Select com grupo de opções e múltipla escolha
    books_you_own = forms.MultipleChoiceField(choices=BOOK_CHOICHES_OPT, required=False)
    
    #Botões de Radio
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    
    #Inputs de números
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField(max_digits=5, decimal_places=3)
    
    #Input de email
    email_input = forms.EmailField(required=False)
    
    #Input de data
    date_input = forms.DateInput(attrs={'type': 'date'})
    
    #Input escondido
    
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial='Hidden')
    
    