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

