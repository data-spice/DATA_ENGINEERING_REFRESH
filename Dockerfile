FROM python:3.13.11-slim 
RUN pip install pandas pyarrow


WORKDIR /code
COPY pipeline/pipeline.py .


ENTRYPOINT ["python", "pipeline.py"]
RUN apt update
