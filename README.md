# Google Play Publisher

An image to upload an Android App Bundle (`.aab`) to Google play.

## How-to

```sh
docker run --rm \
	-v /path/to/the/bundle.aab:/bundle.aab \
	-v /path/to/the/mapping.txt:/mapping.txt \
	-v /Users/brais/projects/21buttons/key.p12:/key.p12 \
	-e "PACKAGE_NAME=com.android21buttons" \
	-e "SERVICE_ACCOUNT_EMAIL=your.service@account.email" \
	21buttons/google-play-publisher
```

The documentation about how to get the `key.p12` is here:
https://github.com/googlesamples/android-play-publisher-api/tree/master/v3/python
