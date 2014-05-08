class Py3status:

    status = 'total'


    def on_click(self, json, i3status_config, event):
        """
        Handles click events.
        """
        if self.status == 'total':
            self.status = 'split'
        else:
            self.status = 'total'


    def btcd_conncount(self, json, i3status_config):
        """
        Display the number of connections for the bitcoin daemon.
        """
        import time

        response = {'full_text':'btcd: ',
                    'name':'btcd_conncount',
                    'color':'#CCCC00',
                    }
        response['cached_until'] = time.time() + 1 # refresh every second
        position = 1

        try:
            import subprocess
            import json

            sp = subprocess.Popen( ["bitcoind", "getpeerinfo"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    )

            (out, err) = sp.communicate()

            if sp.returncode != 0:
                raise Exception("bitcoind failed")
            # this terrible hack servers the dual purpose of
            # 1. discarding the newline ('\n') from the output
            # 2. converting the bytecode returned by Popen into actual strings
            # If there's a more elegant way to do this, let me know.
            out = out.decode('ascii')
            err = err.decode('ascii')
            out = json.loads(out)

            conn_count = len(out)
            conn_outbound = 0
            conn_inbound = 0

            for conn in out:
                if conn['inbound'] == True:
                    conn_inbound += 1
                elif conn['inbound'] == False:
                    conn_outbound += 1

            if self.status == 'total':
                response['full_text'] += str(conn_count)
            elif self.status == 'split':
                response['full_text'] += "in " + str(conn_inbound) + " out " + str(conn_outbound)


        except Exception as e:
            response['full_text'] = 'btcd'
            response['color'] = '#888888'
        finally:
            return (position, response)
