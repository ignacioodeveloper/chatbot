from django.shortcuts import redirect, render
import openai
from django.http import HttpResponse
# Create your views here.
openai.api_key = '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'

# def home(request):
#     return render(request, "core/home.html",{'reply': reply})


def home(request):
    if request.method == 'POST':
        user_message = request.POST['user_message']

        # Obtener la lista de mensajes existente (si existe)
        chat_history = request.session.get('chat_history', [])

        # Agregar el mensaje del usuario a la lista de mensajes
        chat_history.append(('user', user_message))

        # Concatenar todos los mensajes en un solo prompt
        prompt = '\n'.join(f'{role}: {message}' for role, message in chat_history)

        # Enviar solicitud a la API de OpenAI
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=50
        )

        reply = response.choices[0].text.strip()

        # Agregar la respuesta del chatbot a la lista de mensajes
        chat_history.append(('A.I.', reply))

        # Guardar la lista de mensajes actualizada en la sesión
        request.session['chat_history'] = chat_history

        return render(request, 'core/home.html', {'chat_history': chat_history})

    return render(request, 'core/home.html')