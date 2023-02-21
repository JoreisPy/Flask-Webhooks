from flask import Flask, request, render_template, make_response, url_for, redirect, Markup
import requests
import configparser


# Read the Cloudflare account information from the config file
config = configparser.ConfigParser()
config.read('credentials.cfg')
pi_hostname = config.get('piholeApi', 'pi_hostname')
pi_local_domain = config.get('piholeApi', 'pi_local_domain')
token = config.get('piholeApi', 'token')


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/hook/block-enable', methods=['GET'])
def block_enable():

    url = f'http://{pi_hostname}.{pi_local_domain}/admin/api.php?enable&auth={token}'
    r = requests.request("GET", url)
    r.raise_for_status()

    if r.status_code == 200:
        return('Adblocking enabled')

    else:
        return('Error: not possible to enable Adblocking')

@app.route('/hook/block-disable', methods=['GET'])
def block_disable():

    url = f'http://{pi_hostname}.{pi_local_domain}/admin/api.php?disable&auth={token}'
    r = requests.request("GET", url)
    r.raise_for_status()

    if r.status_code == 200:
        return('Adblocking disabled')

    else:
        return('Error: not possible to disable Adblocking')


if __name__ == "__main__":
    app.run(debug=True)
