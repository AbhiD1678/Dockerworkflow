#1. Python
#2. app.py , demo.py, requirements.txt
#3. install packages
#4. streamlit run app.py

FROM python:3

WORKDIR /usr/src/app              

COPY requirements.txt ./           
RUN pip install --no-cache-dir -r requirements.txt  

COPY . .                          

CMD [ "streamlit", "run", "app.py" ] 