import logging
import time

from flask import Flask, render_template, request, redirect

from appLogs.logger import getLogger

log = getLogger()
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['CORS_HEADERS'] = 'Content-Type'

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/generate')
def generate_log():
    t1 = time.time()
    id = request.args.get("id")

    if id == "login":
        time.sleep(0.2)
        t2 = "%.4f" % (time.time() - t1)
        log.error("Forbidden!!!", extra={'statusCode': 403, 'rst': t2, 'url': '/api/v1/login'})
    elif id == "signup":
        time.sleep(0.4)
        t2 = "%.4f" % (time.time() - t1)
        log.error("Internal server error!!!", extra={'statusCode': 500, 'rst': t2, 'url': '/api/v1/signup' })
    elif id == "dashboard":
        time.sleep(5)
        t2 = "%.4f" % (time.time() - t1)
        log.warn("Response time is greater than 3 sec!!!", extra={'statusCode': 200, 'rst': t2, 'url': '/api/v1/dashboard'})

    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
