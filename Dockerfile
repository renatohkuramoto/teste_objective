FROM python:3.11

WORKDIR /test_objective

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python","manage.py"]
CMD ["startup"]