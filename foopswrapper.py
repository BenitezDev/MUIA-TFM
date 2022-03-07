from _thread import *
import threading
import os
from psutil import process_iter
from signal import SIGKILL
from subprocess import Popen
import subprocess, json

class FoopsWrapper:
    def __init__(self, port):
        self.port = port
        # command = "java -jar -Dserver.port={0} vendors/fair_ontologies/target/fair_ontologies-0.1.0.jar".format(self.port)
        # os.system(command)


    #def finish_foops_server(self):
        #self.p.kill()

    def get_metric(self, url):
        cmd = f'curl -X POST "http://localhost:{self.port}/assessOntology" -H "accept: application/json;charset=UTF-8" -H "Content-Type: application/json;charset=UTF-8" -d "{{ \\"ontologyUri\\": \\"{url}\\"}}"'
        result = os.popen(cmd).read()

        json_object = json.loads(result)
        return json_object