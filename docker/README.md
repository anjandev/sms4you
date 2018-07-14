# sms4you

A simple dockerized setup to send and receive SMS via email. It relies on the [gammu](https://wammu.eu/gammu/) library to connect to a [GSM modem or phone](https://wammu.eu/phones/) with the SIM card. When receiving an SMS it sends out an email to a designated address. 

Most easily just run it with [docker compose](https://docs.docker.com/compose/). Make sure to edit the variables in the [docker-compose.yml](./docker-compose.yml) before.

`docker-compose run sms4you`

Or use a pure (long) docker command:

`docker run -t -i --device=/dev/ttyUSB0 sms4you bash`

