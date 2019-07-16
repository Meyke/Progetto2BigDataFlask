FROM python:3.6-slim-stretch

RUN mkdir -p /usr/share/man/man1

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    git \
    wget \
    curl \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

WORKDIR ./root

RUN wget https://www-us.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz && \
    tar -xvzf spark-2.4.3-bin-hadoop2.7.tgz

COPY . ./spark-2.4.3-bin-hadoop2.7/data      
RUN cd spark-2.4.3-bin-hadoop2.7 && \
    mv data/elasticsearch-spark-20_2.11-7.2.0.jar jars
