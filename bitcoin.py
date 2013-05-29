class Py3status:


    def reddit(self, json, i3status_config):
        """
        Get and display link and comment karma from reddit.
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
