# ��������
FROM python:3.8-slim-buster

# ����ά����
MAINTAINER user peng3577041@qq.com

WORKDIR /ELE_AndroidTest

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update -y && apt-get install


RUN apt-get install android-tools-adb -y
RUN apt-get install default-jre -y
RUN apt-get install default-jdk -y
RUN apt-get install net-tools -y

# ����Ҫʹ�õ��ļ����ƹ�ȥ������Ƕ���ļ����ͷ�һ���ļ���
COPY aseert_pic ./aseert_pic
COPY logs ./logs
COPY module ./module
COPY reports ./reports
COPY result ./result
COPY screenshots ./screenshots
COPY testsuites_new ./testsuites_new
COPY tools ./tools
COPY config.py ./config.py
COPY conftest.py ./conftest.py
COPY driver.py ./driver.py
COPY run.py ./run.py

# ����������6080�˿�
EXPOSE 6080

# ��������������ִ�е�������Ҳ��ɱ� docker run �ṩ�Ĳ������ǡ�
ENTRYPOINT ["python", "-m"]
CMD ["run.py"]


