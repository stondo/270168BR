FROM python:3.11.2

# working directory
WORKDIR /270168BR

# copy requirement file to working directory
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY guru.py .
COPY test_guru.py .

ENTRYPOINT ["python", "-m", "unittest", "test_guru.py"]
