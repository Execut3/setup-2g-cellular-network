Create Docker image:
```bash
docker build --network host -t osmocom-2g .
```


Now run it with following command:
```bash
docker run -it -d -v /dev/bus/usb:/dev/bus/usb -v /usr/local/share/uhd/images/:/usr/share/uhd/ -v $PWD/configs:/app/configs --privileged --network host --name osmocom-2g osmocom-2g 
```
