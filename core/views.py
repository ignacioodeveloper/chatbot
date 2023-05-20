from django.shortcuts import redirect, render
import openai
from django.http import HttpResponse
import datetime
# Create your views here.
openai.api_key = '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'

# def home(request):
#     return render(request, "core/home.html",{'reply': reply})

def obtener_hora_y_fecha():
    ahora = datetime.datetime.now()
    hora_fecha_actual = ahora.strftime("%Y-%m-%d %H:%M:%S")
    return hora_fecha_actual


def home(request):
    hora_fecha_actual = obtener_hora_y_fecha()
    
    chat_history = request.session.get('chat_history',[])

    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_message,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )

        reply = response.choices[0].text.strip()
        chat_history.append({'user_message': user_message, 'reply': reply})
        request.session['chat_history'] = chat_history

        return render(request, 'core/home.html',{'chat_history': chat_history,'user_message': user_message,'hora_fecha_actual': hora_fecha_actual, 'reply': reply})

    return render(request, 'core/home.html',{'chat_history': chat_history ,'hora_fecha_actual': hora_fecha_actual} )






def home1(request):
    hora_fecha_actual = obtener_hora_y_fecha()

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
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )

        reply = response.choices[0].text.strip()

        # Agregar la respuesta del chatbot a la lista de mensajes
        chat_history.append(('A.I: ', reply))

        # Guardar la lista de mensajes actualizada en la sesión
        request.session['chat_history'] = chat_history

        return render(request, 'core/home.html', {'chat_history': chat_history, 'hora_fecha_actual': hora_fecha_actual})

    return render(request, 'core/home.html')