import subprocess
import webiopi

def setup():
	subprocess.call('../videostream/start_stream.sh', shell=True)

def destroy():
	subprocess.call('../videostream/stop_stream.sh', shell=True)