from django import forms

class DynamicEmailForm(forms.Form):
    smtp_user = forms.EmailField(
        label="SMTP Email",
        required=True
    )
    smtp_password = forms.CharField(
        label="SMTP Password",
        widget=forms.PasswordInput(attrs={
            'id': 'id_smtp_password'  # Give it an ID for toggling
        }),
        required=True
    )
    
    
    receiver_email = forms.EmailField(
        label="Receiver's Email",
        required=True
    )
    reply_to_email = forms.EmailField(
        label="Reply-To Email",
        required=False
    )
    email_title = forms.CharField(
        label="Email Title",
        max_length=255
    )
    email_message = forms.CharField(
        label="Email Message",
        widget=forms.Textarea
    )
