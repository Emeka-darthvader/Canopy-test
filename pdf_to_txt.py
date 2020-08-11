import  subprocess
import argparse
from helper_modules.response_messages import success_extracted

#get the arguments parsed
parser = argparse.ArgumentParser()
parser.add_argument("-d","--data", help="Directory for PDF to be extracted",default="data/canopy_technical_test_input.pdf")
args = parser.parse_args()

#get the value of the arguments parsed and run pdftotext command
data_directory = args.data
command  = ['pdftotext', '-layout', data_directory,'-nodiag']
output   =  subprocess.check_output(command).decode()

#show success message
success_extracted()
