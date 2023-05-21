from django.contrib.sessions.backends.db import SessionStore

from django.shortcuts import redirect, render
import openai
from django.http import HttpResponse
import datetime
from .models import ChatEntry

# Create your views here.
openai.api_key = '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'

# def home(request):
#     return render(request, "core/home.html",{'reply': reply})

def obtener_hora_y_fecha():
    ahora = datetime.datetime.now()
    hora_fecha_actual = ahora.strftime("%Y-%m-%d %H:%M:%S")
    return hora_fecha_actual


    hora_fecha_actual = obtener_hora_y_fecha()

    chat_history = request.session.get('chat_history', [])
    chat_session_id = request.session.get('chat_session')

    if request.method == 'POST':
        if 'nuevo_chat' in request.POST:
            request.session.flush()
            request.session = SessionStore()

            # Crear una nueva instancia de ChatSession
            chat_session = ChatSession.objects.create(timestamp=hora_fecha_actual)
            chat_session_id = chat_session.id
            request.session['chat_session'] = chat_session_id

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

        # Guardar el mensaje en ChatEntry asociado a la ChatSession actual
        chat_session = ChatSession.objects.get(id=chat_session_id)
        chat_entry = ChatEntry(chat_session=chat_session, user_message=user_message, reply=reply,
                               timestamp=hora_fecha_actual)
        chat_entry.save()

        chat_history.append({'user_message': user_message, 'reply': reply, 'timestamp': hora_fecha_actual})
        request.session['chat_history'] = chat_history

        return render(request, 'core/home.html', {'chat_history': chat_history, 'user_message': user_message,
                                                   'hora_fecha_actual': hora_fecha_actual, 'reply': reply})

    return render(request, 'core/home.html', {'chat_history': chat_history, 'hora_fecha_actual': hora_fecha_actual})

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



        chat_entry = ChatEntry(user_message=user_message, reply=reply)
        chat_entry.save()

        chat_history.append({'user_message': user_message, 'reply': reply})
        request.session['chat_history'] = chat_history

        return render(request, 'core/home.html',{'chat_history': chat_history,'user_message': user_message,'hora_fecha_actual': hora_fecha_actual, 'reply': reply})

    return render(request, 'core/home.html',{'chat_history': chat_history ,'hora_fecha_actual': hora_fecha_actual} )




