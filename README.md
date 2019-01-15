# Google Play Publisher

An image to upload an Android App Bundle (`.aab`) to Google play.

## How-to

```sh
docker run --rm \
	-v /path/to/the/bundle.aab:/bundle.aab \
	-v /path/to/the/mapping.txt:/mapping.txt \
	-v /path/to/the/client_secrets.json:/client_secrets.json \
	-v /path/to/the/androidpublisher.dat:/androidpublisher.dat \
	21buttons/google-play-publisher package_name
```

The documentation about how to generate the `client_secrets.json` and `androidpublisher.dat`
is here: https://github.com/googlesamples/android-play-publisher-api/tree/master/v3/python
