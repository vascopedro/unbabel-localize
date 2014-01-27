#!/usr/bin/env python
#-*- mode: python -*-
 
from subprocess import Popen, PIPE
import sys
 
syntax_checker = "pyflakes"
 
def run(command):
    p = Popen(command.split(), stdout=PIPE, stderr=PIPE)
    p.wait()
    return p.returncode, p.stdout.read().strip().split(), p.stderr.read()
 
_, files_modified, _= run("git diff-index --name-only --cached HEAD")
 
for fname in files_modified:
    if fname.endswith(".po"):
        print >>sys.stderr, "Checking for new strings on %s: ... "%(fname,),
#         exit_code, _, errors = run("%s %s"%(syntax_checker, fname))
#         if exit_code != 0:
#             print >>sys.stderr, "\rChecking syntax on %s: FAILED! \n%s"%(fname, errors)
#             sys.exit(exit_code)
#         else:
#             print >>sys.stderr, "\rChecking syntax on %s: OK!"%(fname,)