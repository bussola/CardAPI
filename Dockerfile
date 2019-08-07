FROM python:3.6-onbuild
EXPOSE 8000
ENV PYTHON_UNBUFFERED=1
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
