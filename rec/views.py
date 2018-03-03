from django.shortcuts import render
from django.http import HttpResponse
from enum import Enum
# Create your views here.


class STATUS(Enum):
    # TODO Decide if this has to be moved to utils package
    READY = 'READY'
    IN_PROGRESS = 'Training in Progress'
    COMPLETED = 'Training Completed'


def init(request):
    # TODO Add implementation for Async POST Call
    pass


def status(request):
    return HttpResponse(status=200)
    # return render(request, , status=204)


def accuracy(request):
    # TODO Add implementation for returning accuracy of the trained Deep Learning Model
    # TODO Finalize url pattern
    pass


def prediction(request):
    # TODO Add implementation for returning prediction of a given image after running it through the trained model
    # TODO Finalize url pattern
    pass
