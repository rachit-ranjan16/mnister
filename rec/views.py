import json
from django.http import HttpResponse
from django.views import View
from enum import Enum
from .learn import DeepLearn
from .tasks import init_learning
# Create your views here.


class State(Enum):
    # TODO Decide if this has to be moved to utils package
    READY = 1
    IN_PROGRESS = 2
    COMPLETED = 3


state_dict = {
    State.READY: 'READY',
    State.IN_PROGRESS: 'Training in Progress',
    State.COMPLETED: 'Training Completed'
}


class MnistStatusView(View):

    def __init__(self):
        self.state = State.READY
        self.dL = DeepLearn()

    def get(self, request):
        # TODO Add implementation for returning accuracy of the trained Deep Learning Model
        tokens = request.path.split('/')
        if len(tokens) > 3:
            return HttpResponse(state=404)
        response = HttpResponse(json.dumps({'state': state_dict[self.state]}), content_type="application/json")
        response.status_code = 200
        return response

    def post(self, request):
        tokens = request.path.split('/')
        if len(tokens) > 3:
            return HttpResponse(state=400)
        if tokens[2] == 'train':
            # POST /rec/train Initiate Training if State is READY or COMPLETED
            if self.state == State.READY:
                # Initiate Training
                # TODO Add Async Processing using Celery
                init_learning(self.dL)
                return HttpResponse(state=201)



