FROM python:slim-buster

WORKDIR /opt/secure-ws

RUN python3 -m pip install --no-cache-dir gunicorn flask flask-socketio gevent-websocket

EXPOSE 5000

CMD ["gunicorn", "--workers=1", "--bind=0.0.0.0:5000", "--certfile=/etc/ssl/certs/secure-ws.cobblepot59.int.crt", "--keyfile=/etc/ssl/private/secure-ws.cobblepot59.int.key", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "wsgi:app"]
