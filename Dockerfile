FROM python:3.6.14-alpine

WORKDIR /app

ENV FLASK_APP=customsepomex
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY python_dependencies.txt python_dependencies.txt

RUN pip install -r python_dependencies.txt
EXPOSE 5000

COPY . .

CMD ["flask", "run"]
