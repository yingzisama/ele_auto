# 基础镜像
FROM python:3.8-slim-buster

# 镜像维护者
MAINTAINER user peng3577041@qq.com

WORKDIR /ELE_AndroidTest

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update -y && apt-get install


RUN apt-get install android-tools-adb -y
RUN apt-get install default-jre -y
RUN apt-get install default-jdk -y
RUN apt-get install net-tools -y

# 把需要使用的文件复制过去，如果是多个文件，就放一个文件夹
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

# 开放容器的6080端口
EXPOSE 6080

# 配置容器启动后执行的命令，并且不可被 docker run 提供的参数覆盖。
ENTRYPOINT ["python", "-m"]
CMD ["run.py"]


