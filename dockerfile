
# use lighweight python image
FROM python:3.8-slim

#set working directory
WORKDIR /app

#copy requirements file and install dependencies
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

#copy all code
COPY . .


#expose port 8000 because 5000 was in use
EXPOSE 8000

# #run app
CMD ["python", "app.py"]
