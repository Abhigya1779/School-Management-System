from django import forms

from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'address', "course","document"]
    
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name',
                                            "class": "form-control"}),
        

            "email" : forms.EmailInput(attrs={'placeholder': 'Enter your email',
                                        "class": "form-control"}),
    

            "age" : forms.NumberInput(attrs={'placeholder': 'Enter your age',
                                         "class": "form-control"}), 
    

            "address" : forms.TextInput(attrs={'placeholder': 'Enter your address',
                                       "class": "form-control"}),

            "course" : forms.Select(attrs={'placeholder': 'Enter your course',
                                           "class": "form-control"}),

            "document" : forms.ClearableFileInput(attrs={'placeholder': 'Enter your course',
                                                       "class": "form-control"})
    
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age <16:
            raise forms.ValidationError("Age must be at least 16.")
        elif age > 40:
            raise forms.ValidationError("Age must be at most 40.")
        
        return age

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        address = cleaned_data.get('address')

        if age and age <18 and address =="Kathmandu":
            raise forms.ValidationError("Students under 18 cannot have kathmandu as their address")

        return cleaned_data
    