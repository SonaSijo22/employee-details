from django import forms
from empapp.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields ="__all__"
        widgets={#style chayyan vendi
            "name":forms.TextInput(attrs={"class":"form-control"}),#form control kodukkan kaaranam title ennu kofuthitttu athinte adiyil ezhuthan paattunna rethiyilchayyan vendi ahnu
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "post":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"})
            
        }

# errors
# ---------
# matching query doesn't exist
# template deoen't exist
# context must be dictionary rather than set

