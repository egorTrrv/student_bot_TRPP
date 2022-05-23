FROM python:3

WORKDIR ./dockerdir

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY mainMenu.py ./dockerdir/mainMenu.py
COPY number_of_groups.db ./dockerdir/number_of_groups.db

COPY./functions ./dockerdir/functions
COPY ./classes ./dockerdir/classes


CMD [ "python", "mainMenu.py" ] 