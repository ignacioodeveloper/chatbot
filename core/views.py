from django.contrib.sessions.backends.db import SessionStore

from django.shortcuts import redirect, render
import openai
from django.http import HttpResponse
import datetime
from .models import ChatEntry

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

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
        if 'nuevo_chat' in request.POST:
            request.session.flush()
            request.session = SessionStore()

            return redirect('home')

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


        chat_id = 1
        chat_entry = ChatEntry(user_message=user_message, reply=reply)
        chat_entry.save()

        chat_history.append({'user_message': user_message, 'reply': reply})
        request.session['chat_history'] = chat_history

        #mensajes websocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
                        f'chat_{chat_id}',
            {
                'type': 'chat_message',
                'message': f'A.I.: {reply}'  # Envía solo la respuesta de la IA
            }

        )

        return render(request, 'core/home.html',{'chat_history': chat_history,'user_message': user_message,'hora_fecha_actual': hora_fecha_actual, 'reply': reply})

    return render(request, 'core/home.html',{'chat_history': chat_history ,'hora_fecha_actual': hora_fecha_actual} )




