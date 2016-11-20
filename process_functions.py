from config import *

def startProcess(path):
        process = subprocess.Popen(shlex.split(path), shell=False)
        return process.pid

def killProcess(processId):
        if processId:
                try:
                        os.kill(processId, signal.SIGTERM)
                except OSError:
                        print("UNABLE TO KILL: " + str(processId))
                        return False
                else:
                        return True
