# Redirect latest ABC National news bulletin
This docker container redirects any incoming HTTP request to the URL of the latest
ABC national news bulletin as listed in
[this feed](https://appsupport.abc-prod.net.au/Prod/listen/newsbulletin).

You need to set the following environment variables in the Unraid config for the container:
- `PORT` the port to listen on

To build it on my M1 Mac I had to use the following:
`docker buildx build --platform linux/amd64,linux/arm64 -t shermozle/abc_national_bulletin --push .`