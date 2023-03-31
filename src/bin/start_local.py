#!/usr/bin/env python3

import os, argparse
from dotenv import load_dotenv

bin_folder = os.path.dirname(os.path.realpath(__file__))
src_folder = os.path.dirname(bin_folder)
repo_folder = os.path.dirname(src_folder)

dotenv_path = repo_folder + "/.env/RunTime/envs/.env"
activate_path = repo_folder + "/.env/bin/activate"
app_path = src_folder + "/main.py"

parser = argparse.ArgumentParser(
    prog='local_start.py',
    description='Starts server with frontloaded dotenv file for local development.',
    epilog='''---'''
)

def main():
    load_dotenv(dotenv_path)
    os.system(f". {activate_path} && python -B {app_path} >&1")

if __name__ == "__main__":
    main()