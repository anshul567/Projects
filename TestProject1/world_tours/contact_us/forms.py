from django import forms # type: ignore

class Contactform(forms.Form):
    name= forms.CharField(label="Your Name", max_length=100)
    email= forms.EmailField(label="Email")
    message=forms.CharField(label="Message for us",widget=forms.Textarea)

    def send_email(self):
        print(f"Sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")