speedtest --accept-license --accept-gdpr --format=json > results.json
echo "Results written to results.json"
cat results.json

# TODO - send results to server, access token available und $TOKEN