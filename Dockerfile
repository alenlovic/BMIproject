FROM python:3.8

ADD kalkulator_zdravlja.py .

RUN pip install requests beautifulsoup4 

CMD [ "python", "./kalkulator_zdravlja.py" ]