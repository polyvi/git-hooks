import os
import re

def isAlreadyLicensed(filePath):
    aFile = open(filePath, 'r')
    content= aFile.read()
    matchObject = re.search('(GNU General Public License|Apache License, Version 2\.0)',
     content, re.IGNORECASE)
    aFile.close()
    return matchObject

def isPlainTextFile(filePath):
    """
        mimetypes guess type simply by file name, python-magic would be
        better since it touches file content and then makes decision. However,
        extra lib would be required, just check out at,
        https://github.com/ahupp/python-magic
    """

    validSourceFileSuffixes = ['.m', '.mm', '.h', '.cpp', '.c', '.cs', '.java', '.js',
    '.html']

    for suffix in validSourceFileSuffixes:
        if filePath.endswith(suffix):
            return True

    return False

def validateLicense(files):
    unlicensedSources = []
    for source in files:
        if isPlainTextFile(source):
            fullPath = os.path.join(os.getcwd(), source)
            if not isAlreadyLicensed(fullPath):
                unlicensedSources.append(source)

    if len(unlicensedSources) > 0:
        print "You may miss license statement in following source files:"

    for source in unlicensedSources:
        print source

    return len(unlicensedSources) == 0

def precommit(git_state):
    return validateLicense(git_state["files"])
