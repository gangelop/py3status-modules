class Py3status:
    import webbrowser


    def on_click(self, json, i3status_config, event):
        """
        Handles click events.
        """
        import os
        import subprocess

        if event['button'] == 1:
            with open(os.devnull, 'w') as fnull:
                result = subprocess.call(['xdg-open', 'http://www.reddit.com/user/' + self.user],
                                            stdout=fnull,
                                            stderr=fnull)


    def reddit(self, json, i3status_config):
        """
        Get and display link and comment karma from reddit.
        """
        response = {'full_text':'', 'name':'reddit', 'color':'#ff9000' }
        position = 0

        try:
            import requests

            # reddit username goes here:
            self.user = ''

            # reddit.com asks that we use a unique user agent
            # for accessing the api.
            # See https://github.com/reddit/reddit/wiki/API#rules
            # NEVER LIE ABOUT YOUR USER-AGENT!!!
            user_agent = 'py3status from /u/' + self.user + ' :D'

            s = requests.Session()
            s.headers.update({'User-Agent':user_agent})
            r = s.get('http://www.reddit.com/user/' + self.user +
                            '/about.json')

            about = r.json()
            data = about['data']
            response['full_text'] = 'reddit: '
            response['full_text'] += str(data['link_karma'])
            response['full_text'] += '-'
            response['full_text'] += str(data['comment_karma'])

        except Exception as e:
            response['full_text'] = 'reddit'
            response['color'] = '#ff0000'
        finally:
            return (position, response)
