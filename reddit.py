#!/usr/bin/env python3

class Py3status:


    def reddit(self, json, i3status_config):
        """
        Get and display link and comment karma from reddit.
        """
        response = {'full_text':'', 'name':'reddit'}

        try:
            import json
            import requests

            # Reddit username goes here:
            user = ''

            r = requests.get('http://www.reddit.com/user/' + user + '/about.json')

            about = json.loads(r.text)
            data = about['data']
            response['full_text'] = 'reddit: '
            response['full_text'] += str(data['link_karma'])
            response['full_text'] += '-'
            response['full_text'] += str(data['comment_karma'])

        except Exception as e:
            pass
        finally:
            return (0, response)
