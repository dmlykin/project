FROM python:3.7

SHELL ["/bin/bash", "-c"]
RUN /bin/sed -i 's/archive\.ubuntu\.com/mirror\.yandex\.ru/g' /etc/apt/sources.list && apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        pkg-config \
        software-properties-common \
        libgl1-mesa-glx \
        git \
        cmake \
        curl \
        wget \
        unzip \
        vim \
        sudo \
        openssh-server \
        supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /root/conda
ENV PATH "/root/conda/bin:$PATH"
# ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
ADD environment.yml /tmp/environment.yml
RUN conda update -n base -c defaults conda && \
    conda env create -f environment.yml && \
    conda init bash && \
    conda clean -a
RUN echo "conda activate project" >> ~/.bashrc


ARG UID
ENV NOTVISIBLE "in users profile"

RUN useradd -d /home/developer -ms /bin/bash -u $UID -G sudo developer
RUN echo developer:developer | chpasswd
RUN chmod 775 /root

RUN echo "export PATH=$PATH" >> /home/developer/.bashrc
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> /home/developer/.bashrc
RUN echo "export VISIBLE=now" >> /home/developer/.bashrc
RUN echo "export NOTVISIBLE=$NOTVISIBLE" >> /home/developer/.bashrc
RUN cat /root/.bashrc >> /home/developer/.bashrc

RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "echo \"PasswordAuthentication no\" >> /etc/ssh/sshd_config" >> /root/ssh_disable_password.sh && \
    echo "service ssh restart" >> /root/ssh_disable_password.sh && \
    chmod +x /root/ssh_disable_password.sh

USER developer
RUN mkdir /home/developer/.jupyter
RUN mkdir /home/developer/project
WORKDIR /home/developer/project

USER root
ADD supervisord /etc/supervisor/conf.d/
RUN exec /bin/bash && conda activate project
CMD ["supervisord", "-n"]
