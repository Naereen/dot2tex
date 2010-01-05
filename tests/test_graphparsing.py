"""Test that output from dotparsing and dot is the same"""

import re, os,shutil, glob,sys,time

import ImageChops,Image

from os.path import join,basename,splitext,normpath
from dot2tex import dotparsing

# Directory with test files
BASE_DIR = "d:/pycode/textools/dotconv/tests/testgraphs/"
TESTFILES_DIR = "dotparsingtests"
TESTFILES_PATH = join(BASE_DIR,TESTFILES_DIR)

PNG_DIR = join(TESTFILES_PATH,'pngs')
DOT_DIR = join(TESTFILES_PATH,'dpdots')

import logging

# intitalize logging module
log = logging.getLogger("test_graphparser")
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
# set a format which is simpler for console use
formatter = logging.Formatter('%(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
log.addHandler(console)

LOG_FILENAME = splitext(__file__)[0]+'.log'
hdlr = logging.FileHandler(LOG_FILENAME)
log.addHandler(hdlr)
formatter = logging.Formatter('%(levelname)-8s %(message)s')
hdlr.setFormatter(formatter)
log.setLevel(logging.INFO)


def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None

def get_testfiles():
    filelist = []
    for f in glob.glob(join(TESTFILES_PATH,"*.dot")):
        filelist.append(os.path.normpath(f))
    return filelist

if __name__ == '__main__':
    graphparser = dotparsing.DotDataParser()
    log.info('%s Start of run',time.asctime())
    dotfiles = get_testfiles()
    matchingfiles = []
    nonmatchingfiles = []
    failedfiles = []
    for dotfile in dotfiles:
        try:
            log.info('Processing %s', dotfile)
            basefilename = basename(dotfile)
            basefilenamenoext = os.path.splitext(basefilename)[0]
            f = open(dotfile)
            try:
                data = f.read()
            except:
                log.warning('Could not open %s',dotfile)
                continue
            f.close()
            try:
                graph = graphparser.parse_dot_data(data)
                # create a dotparsing version of the dot file
                newfilename = normpath(join(DOT_DIR,basefilename+'.new'))
                f = open(newfilename,'w')
                f.write(str(graph))
                f.close()
            except:
                log.exception('Failed to parse and save %s',basefilename)
                continue
            origpngfilename = join(PNG_DIR,basefilenamenoext+'.png')
            newpngfilename = join(PNG_DIR,basefilenamenoext+'.new.png')
            # create PNG from original dot file
            syscmd = 'dot -Tpng %s > %s' % (dotfile,origpngfilename)
            log.debug("Run %s",syscmd)
            err = os.system(syscmd)
            if err:
                log.warning("Failed to create original %s",origpngfilename)
                failedfiles.append(basefilename)
                continue
            # create PNG from dot file generated by dotparsing
            syscmd = 'dot -Tpng %s > %s' % (newfilename,newpngfilename)
            log.debug("Run %s",syscmd)
            err = os.system(syscmd)
            if err:
                log.warning("Failed to create new %s",origpngfilename)
                failedfiles.append(basefilename)
                continue
            # load and compare images
            try:
                imorig = Image.open(origpngfilename)
                imnew = Image.open(newpngfilename)
            except:
                log.exception('Could not load %s images',basefilename)
                continue
            if equal(imorig,imnew):
                log.info('%s matches.', basefilename)
                matchingfiles.append(basefilename)
                # remove files
                os.remove(origpngfilename)
                os.remove(newpngfilename)
                os.remove(newfilename)

            else:
                log.warning('%s did not match!', basefilename)
                nonmatchingfiles.append(basefilename)
        except:
            log.exception('Failed to process %s', basefilename)
            continue

    log.info('Nonmatching files:\n%s',nonmatchingfiles)
    log.info('Matching files:\n%s',matchingfiles)
    log.info('Failed files:\n%s',failedfiles)
    log.info('%s End of run',time.asctime())
