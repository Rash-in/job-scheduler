import os

job_log = os.environ['LOG_PATH'] + "/job_error.log"
ssl_ca_path = os.environ['CERTS_PATH'] + "/ca.pem"

app_config = {
    'job_log': job_log,
    'ssl_ca_path': ssl_ca_path
}