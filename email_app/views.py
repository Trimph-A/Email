from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from .forms import DynamicEmailForm

@csrf_exempt
def send_dynamic_email_view(request):
    if request.method == 'POST':
        form = DynamicEmailForm(request.POST)
        if form.is_valid():
            # 1. Gather user-provided SMTP credentials
            smtp_user = form.cleaned_data['smtp_user']
            smtp_password = form.cleaned_data['smtp_password']
            
            # 2. Gather email fields
            
            receiver = form.cleaned_data['receiver_email']
            reply_to = form.cleaned_data['reply_to_email']
            subject = form.cleaned_data['email_title']
            message = form.cleaned_data['email_message']

            # 3. Create a custom email connection using user-provided creds
            connection = get_connection(
                backend='django.core.mail.backends.smtp.EmailBackend',
                host=settings.EMAIL_HOST,          # e.g., smtp.gmail.com
                port=settings.EMAIL_PORT,          # e.g., 587
                username=smtp_user,
                password=smtp_password,
                use_tls=settings.EMAIL_USE_TLS,    # or use_ssl if needed
                fail_silently=False
            )

            # 4. Construct the EmailMessage and attach the custom connection
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=smtp_user,
                to=[receiver],
                reply_to=[reply_to] if reply_to else None,
                connection=connection
            )

            # 5. Send the email
            email.send()

            return render(request, 'email_app/email_sent.html', {
                'receiver': receiver,
                'subject': subject
            })
    else:
        form = DynamicEmailForm()

    return render(request, 'email_app/send_email_form.html', {'form': form})
