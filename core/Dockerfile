FROM python:3.6-onbuild
COPY . /app
WORKDIR /app
EXPOSE 8000
ENV PYTHON_UNBUFFERED=1
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt
CMD ["/app/run.sh"]
