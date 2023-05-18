from django.shortcuts import redirect, render
import openai

# Create your views here.
openai.api_key = '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'

# def home(request):
#     return render(request, "core/home.html",{'reply': reply})


def home(request):
    if request.method == 'POST':
        user_message = request.POST['user_message']
        # Enviar solicitud a la API de OpenAI
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_message,
            max_tokens=50
        )
        
        reply = response.choices[0].text.strip()

        return render(request, "core/home.html",{'reply': reply, 'user_message': user_message})

    return render(request, 'core/home.html')