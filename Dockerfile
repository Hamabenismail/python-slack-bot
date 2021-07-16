FROM python:3

ADD lambda_function.py /

RUN pip install slackclient
RUN pip install python-dotenv
RUN pip install schedule

CMD [ "python", "./lambda_function.py" ]