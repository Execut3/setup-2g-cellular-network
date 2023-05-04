FROM debian:11
RUN apt-get update && apt-get install wget -y
RUN OSMOCOM_REPO="https://downloads.osmocom.org/packages/osmocom:/latest/Debian_11" && \
	wget $OSMOCOM_REPO/Release.key && \
	mv Release.key /usr/share/keyrings/osmocom-latest.asc && \
	echo "deb [signed-by=/usr/share/keyrings/osmocom-latest.asc] $OSMOCOM_REPO/ ./" > /etc/apt/sources.list.d/osmocom-latest.list && \
	apt-get update
RUN apt install osmo-bsc osmo-msc osmo-bts-trx osmo-ggsn osmo-sgsn osmo-hlr osmo-mgw osmo-trx-uhd iputils-ping net-tools -y
RUN apt-get install libuhd-dev uhd-host -y
RUN apt-get install iputils-ping net-tools nano telnet tmux -y
RUN apt-get install osmo-stp -y

COPY . /app 
WORKDIR /app

ENV UHD_IMAGES_DIR=/usr/share/uhd/
