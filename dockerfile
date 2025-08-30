# # use lighweight python image
# FROM python:3.8-slim

# #set working directory
# WORKDIR /app


# #copy requirements file and install dependencies
# COPY requirements.txt requirements.txt
# RUN pip install -r requir#used port 8000 because 5000 was in usedements.txt

# #copy all code
# COPY requirements.txt requirements.txt

# #run ap
# CMD ["python", "app.py"]

# #expose port 8000 because 5000 was in use
# EXPOSE 8000

FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
