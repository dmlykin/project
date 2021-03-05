FROM python:3.7

RUN apt-get update && apt-get install -y --no-install-recommends \
        sudo \
        vim \
        openssh-server \
        libmysqlclient-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /tmp/requirements.txt
RUN pip --no-cache-dir install -r /tmp/requirements.txt

EXPOSE 22
EXPOSE 8888

ARG UID
ENV NOTVISIBLE "in users profile"

RUN useradd -d /home/developer -ms /bin/bash -u $UID -G sudo developer
RUN echo developer:developer | chpasswd
RUN chmod 775 /root

RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "export PATH=$PATH" >> /etc/profile
RUN echo "export PYENV_SHELL=$PYENV_SHELL" >> /etc/profile
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> /etc/profile
RUN echo "export TENSORRT_INC_DIR=$TENSORRT_INC_DIR" >> /etc/profile
RUN echo "export TENSORRT_LIB_DIR=$TENSORRT_LIB_DIR" >> /etc/profile
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "export NOTVISIBLE=$NOTVISIBLE" >> /etc/profile

RUN echo "echo \"PasswordAuthentication no\" >> /etc/ssh/sshd_config" >> /root/ssh_disable_password.sh && \
    echo "service ssh restart" >> /root/ssh_disable_password.sh && \
    chmod +x /root/ssh_disable_password.sh

USER developer
RUN mkdir /home/developer/.jupyter
RUN mkdir /home/developer/sor-project

WORKDIR /home/developer/project
