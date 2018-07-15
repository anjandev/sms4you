# sms4you

Easy gateway to send and receive SMS via email. _(To be extended to work with other protocols like XMPP or Matrix)_


## Idea

Connect a [suitable GSM modem or phone](https://wammu.eu/phones/) containing the SIM card into a computer (e.g. a Raspberry Pi) at a fixed place. Give `sms4you` access (imap and smtp) to one dedicated email address. It will use this connection to receive emails to be sent out as SMS and to send out emails with received SMS messages. The phone number will be managed over the email's subject and only emails are accepted coming from a certain email address.


## Concretely - what for?

There can be many reasons, why you want to use `sms4you`. Here are some examples:

* You live in the internetz, and you just need a gateway to this old thing "SMS", which some people really still seem to use.
* You travel and use local SIM cards, but still want to be able to receive SMS confirmation codes for banks and services to your usual number.
* You don't want to carry a (registered) SIM card for [good reasons](https://www.theguardian.com/technology/2016/apr/19/ss7-hack-us-congressman-calls-texts-location-snooping) and stil be able to send and receive SMS.

### Docker Compose

sms4you is available simple dockerized setup. It is easiest to set up with [docker compose](https://docs.docker.com/compose/).

* `wget https://raw.githubusercontent.com/xamanu/sms4you/master/docker/docker-compose.yml`
* Adjust the environment variables in the downloaded file with your settings.
* `docker-compose run sms4you`
