from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def cadd():
	ll = []
	for i in range(1000):
		ll.append(i**i)
	return ll
