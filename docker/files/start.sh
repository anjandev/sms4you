#!/usr/bin/env bash

if [ -z "${$NAME}" ]; then
    echo "Failure starting xmpp server: The environment variable NAME must be set."
elif [ -z "${MATRIX_SERVER_URL}" ]; then
    echo "Failure starting xmpp server: The environment variable MATRIX_SERVER_URL must be set."
elif [ -z "${MATRIX_TURN_KEY}" ]; then
    echo "Failure starting xmpp server: The environment variable MATRIX_TURN_KEY must be set."
else

    DEFAULT_HS_URL="https://$MATRIX_SERVER_URL"
    DEFAULT_IS_URL="https://vector.im"
    INTEGRATIONS_UI_URL="https://scalar.vector.im/"
    INTEGRATIONS_REST_URL="https://scalar.vector.im/api"

    sed -i "s#{{DEFAULT_HS_URL}}#${DEFAULT_HS_URL}#" /riot-web/webapp/config.json
    sed -i "s#{{DEFAULT_IS_URL}}#${DEFAULT_IS_URL}#" /riot-web/webapp/config.json
    sed -i "s#{{BRAND}}#${NAME}#" /riot-web/webapp/config.json
    sed -i "s#{{INTEGRATIONS_UI_URL}}#${INTEGRATIONS_UI_URL}#" /riot-web/webapp/config.json
    sed -i "s#{{INTEGRATIONS_REST_URL}}#${INTEGRATIONS_REST_URL}#" /riot-web/webapp/config.json

    exec http-server -p 8080 -A 0.0.0.0 -c 3500
fi