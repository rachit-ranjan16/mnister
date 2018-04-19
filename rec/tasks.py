from celery import shared_task, current_task
import time
from numpy import random
from scipy.fftpack import fft
from .views import state_dict

# TODO Decide whether this is needed
# @shared_task
# def fft_random(n):
#     for i in range(n):
#         x = random.normal(0, 0.1, 2000)
#         y = fft(x)
#         if (i % 30 == 0):
#             process_percent = int(100 * float(i) / float(n))
#             current_task.update_state(state='PROGRESS',
#                                       meta={'process_percent': process_percent})
#     return random.random()


@shared_task
def init_learning(dl):
    print("Going to sleep for 10s")
    time.sleep(10);
    print("I'm back up")