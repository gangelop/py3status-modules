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

            sp = subprocess.Popen( ["bitcoind", "getconnectioncount"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    )
            (out, err) = sp.communicate()
            # this terrible hack servers the dual purpose of
            # 1. discarding the newline ('\n') from the output
            # 2. converting the bytecode returned by Popen into actual strings
            # If there's a more elegant way to do this, let me know.
            out = out[0:-1].decode('ascii')
            err = err[0:-1].decode('ascii')

            if sp.returncode > 0:
                raise Exception("bitcoind failed")
            else:
                response['full_text'] += out


        except Exception as e:
            response['full_text'] = 'btcd'
            response['color'] = '#888888'
        finally:
            return (position, response)
