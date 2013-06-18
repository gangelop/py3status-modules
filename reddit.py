class Py3status:


    def reddit(self, json, i3status_config):
        """
        Get and display link and comment karma from reddit.
        """
        response = {'full_text':'', 'name':'reddit', 'color':'#ff9000' }
        position = 0

        try:
            import requests

            # reddit username goes here:
            user = ''

            # reddit.com asks that we use a unique user agent
            # for accessing the api.
            # See https://github.com/reddit/reddit/wiki/API#rules
            # NEVER LIE ABOUT YOUR USER-AGENT!!!
            user_agent = 'py3status from /u/' + user + ' :D'

            s = requests.Session()
            s.headers.update({'User-Agent':user_agent})
            r = s.get('http://www.reddit.com/user/' + user +
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
