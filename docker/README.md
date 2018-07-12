# sms4you

A simple dockerized setup to send and receive SMS via email. It relies on the [gammu](https://wammu.eu/gammu/) library to connect to a [GSM modem or phone](https://wammu.eu/phones/) with the SIM card. When receiving an SMS it sends out an email to a designated address. 


`docker run -t -i --device=/dev/ttyUSB0 sms4you bash`
