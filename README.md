# Pihole Adblocking Control Flask App

This is a Flask app that allows you to enable or disable adblocking on a Pihole server through a simple web interface. The app is Dockerised for easy installation and use.

## Requirements

To use this Flask app, you will need:

- A running instance of Pihole on your network or cloud server.
- Docker installed on your local machine or server.

## Installation

To install and run this Flask app, follow these steps:

1. Clone this repository to your local machine or server.
2. Navigate to the root directory of the cloned repository.
3. Create a file called `credentials.cfg` in the root directory of the project, and add the following information:

```shell
touch credentials.cfg
```

```[piholeApi]
pi_hostname=<your Pihole server hostname>
pi_local_domain=<your Pihole server local domain>
token=<your Pihole API token>
```

Replace `<your Pihole server hostname>` with the hostname of your Pihole server, `<your Pihole server local domain>` with the local domain of your Pihole server, and `<your Pihole API token>` with the API token for your Pihole server. You can find your API token by logging into your Pihole server and going to Settings > API/Web interface.

4. Build the Docker container with the following command:

```shell
 docker build --tag webhooks .
 ```


5. Run the Docker container with the following command:
```shell
 docker run -d -p 5001:5001 --name Webhooks  webhooks
```

## Usage

The app provides two endpoints for enabling and disabling adblocking on your Pihole server:

- `http://localhost:5001/hook/block-enable` - enables adblocking on your Pihole server
- `http://localhost:5001/hook/block-disable` - disables adblocking on your Pihole server

