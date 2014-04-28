class Py3status:

    def btcd_conncount(self, json, i3status_config):
        """
        Display the number of connections for the bitcoin daemon.
        """
        import time

        response = {'full_text':'btcd: ', 'name':'btcd_conncount', 'color':'#CCCC00' }
        response['cached_until'] = time.time() + 5 # refresh every 5s
        position = 1

        try:
            import subprocess

            out = subprocess.getoutput('bitcoind getconnectioncount')

            response['full_text'] += out

        except Exception as e:
            response['full_text'] = 'btcd'
            response['color'] = '#888888'
        finally:
            return (position, response)
