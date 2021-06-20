from django.shortcuts import render, HttpResponseRedirect
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.10')
led = LED(17, pin_factory=factory)

# Create your views here.
def index(request):
    return render(request, 'ledapp/ledbutton.html', {})

def ledon(request):
    led.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def ledoff(request):
    led.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
