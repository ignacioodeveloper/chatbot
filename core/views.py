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