class Py3status:


    def bitcoin(self, json, i3status_config):
        """
        Display the latest bitcoin/dollar price from bitstamp.net
        """
        response = {'full_text':'BTC: ', 'name':'bitcoin', 'color':'#ffffff' }

        try:
            import json
            import requests

            r = requests.get('https://www.bitstamp.net/api/ticker/')

            ticker = json.loads(r.text)

            response['full_text'] += '$' + ticker['last']

        except Exception as e:
            response['color'] = '#ff0000'
        finally:
            return (0, response)
