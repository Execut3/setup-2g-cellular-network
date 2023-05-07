# Setup 2g Cellular Network
In this repository I will try to explain all requirement that are needed to setup a 2G Cellular network.

## Requirements

- USRP B210 USB Software Defined Radio (SDR)
- sysmoISIM-SJA2 ISIM Card 
- SmartCard Reader
- Linux (Ubuntu on virtualbox)
- Xiaomi redme note (UE Client)

## Configuration

To setup this lab we need to do the following steps:

- Setup osmocom as a 2g Network
- Install b210 drivers and attach to be used in 2g network
- Program simcard to be configured on same MCC, MNC of 2g network
- Configure Simcard in HLR to be registerd on network

### Setup Osmocom

Change directory to `osmocom` folder and run following commands:
```bash
docker build --network host -t osmocom-2g .
```
And then
```bash
docker-compose up -d
```

This will setup a 2g network and connect to b210 SDR on MCC=901 and MNC=71
