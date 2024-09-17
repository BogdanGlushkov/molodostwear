FROM python:3.12.0-slim

COPY req.txt req.txt
RUN pip install -r req.txt

COPY . .

CMD [ "python", "run.py" ]