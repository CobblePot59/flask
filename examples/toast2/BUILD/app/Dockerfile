FROM python:slim-bookworm

WORKDIR /opt/toastr

RUN python3 -m pip install --no-cache-dir flask flask-toastr flask-socketio gunicorn gevent

EXPOSE 5000

CMD ["gunicorn", "-w", "1", "-k", "gevent", "--certfile", "/etc/ssl/certs/www.toastr.int.crt", "--keyfile", "/etc/ssl/private/www.toastr.int.key", "--bind", "0.0.0.0:5000", "wsgi:app"]