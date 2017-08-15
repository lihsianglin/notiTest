from django.shortcuts import render, redirect
from django.http import HttpResponse
from notifications.signals import notify
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	template = "index.html"
	response = ""
	args = {}
	return render(request, template, args)

def getNotifications(request):
	user = request.user
	notis = user.notifications.all()
	user.notifications.mark_all_as_read()
	response = ""

	if notis.count():
		response += "<ul>"
		for noti in notis:
			response += "<li>{0}<br>{1}<br>{2}</li>".format(noti.verb, noti.description, noti.timestamp)
		response += "</ul>"
	else:
		 response = "目前沒有訊息"

	return HttpResponse(response)


def sendmsg(request):
	user = request.user
	recipient = request.GET['recipient']
	msg = request.GET['msg']

	recipient = User.objects.get(username=recipient)

	args = {}
	args['recipient'] = recipient
	args['verb'] = '{0}給你一則訊息'.format(user)
	args['description'] = msg

	notify.send(user, **args)

	return redirect("/")

def get_noti_unread_count(request):
	user = request.user
	unread_count = user.notifications.unread().count()

	return HttpResponse(unread_count)