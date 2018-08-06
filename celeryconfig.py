from kombu import Queue
from kombu import Exchange

result_serializer = 'json'


broker_url = "amqp://jiuge:jiuge_thunlp@118.190.162.99:5672/jiugehost"
result_backend = "amqp://guest:@localhost:5672"

task_queues = (
    Queue('JJ',  exchange=Exchange('priority', type='direct'), routing_key='JJ'),
    Queue('JJ1',  exchange=Exchange('priority', type='direct'), routing_key='JJ'),
    Queue('JJJ',  exchange=Exchange('priority', type='direct'), routing_key='JJJ'),
    Queue('CT',  exchange=Exchange('priority', type='direct'), routing_key='CT'),
    Queue('SC',  exchange=Exchange('priority', type='direct'), routing_key='SC'),
    Queue('Tencent',  exchange=Exchange('priority', type='direct'), routing_key='Tencent'),
)

task_routes = ([
    ('tasks.main_JJ', {'queue': 'JJ'}),
    ('tasks.main_JJ1', {'queue': 'JJ1'}),
    ('tasks.main_JJJ', {'queue': 'JJJ'}),
    ('tasks.main_CT', {'queue': 'CT'}),
    ('tasks.main_SC', {'queue': 'SC'}),
    ('tasks.main_Tencent', {'queue': 'Tencent'}),
],)
