import logging, os

from app import create_app # load my app factory

app = create_app() # triggers app factory


#################
#### LOGGING 
#################
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
root_path = str(os.path.abspath((os.path.dirname(__file__))))
handler = logging.FileHandler(root_path + '/errors.log', mode='a', encoding=None, delay=False)  # errors logged to this file
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)  # attach the handler to the app's logger
app.logger.info('App started.')


# talk to app through CLI? here's where you can pre-load stuff
@app.shell_context_processor
def make_shell_context():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
