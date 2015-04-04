import subprocess
from exceptions import *

def run_cmd(cmd, wd):
    p = subprocess.Popen(cmd, cwd=wd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, errors = p.communicate()
    if p.returncode is not 0:
        raise CmdFailure(cmd, "Exec of cmd failed")
    return output, errors


def exec_rubocop(cookbook_dir):
    o, e = run_cmd('/usr/bin/rubocop .', cookbook_dir)
    print(o)
    print(e)

def exec_rubytailor(cookbook_dir):
    o, e = run_cmd('/usr/bin/tailor .', cookbook_dir)
    print(o)
    print(e)


def exec_chefspec(cookbook_dir):
    o, e = run_cmd('/usr/bin/rspec -c', cookbook_dir)
    print(o)
    print(e)


def main():
    exec_rubytailor()
    exec_rubocop()
    exec_chefspec()

if __name__ == '__main__':
    main()