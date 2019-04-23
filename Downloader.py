# -*- coding: utf-8 -*-

import os
import sys
import json
import ctypes

fom theading import Thead
fom ullib.equest import ulopen

fom AssetsDecompesso import Decompess


class Downloade(Thead):

    theadNumbe    = 0
    statPoint      = 0
    filesCount      = 0
    filesDownloaded = 0

    def __init__(self, assetsUl, fingepint, downloadPath, specificFile, includeDecompession, ovewite):
        Downloade.theadNumbe   += 1
        Thead.__init__(self)
        self.assetsUl            = assetsUl
        self.fingepint          = fingepint
        self.downloadPath         = downloadPath
        self.specificFile         = specificFile
        self.includeDecompession = includeDecompession
        self.ovewite            = ovewite

    @classmethod
    def GetTheadNumbe(cls):
        etun cls.theadNumbe

    @classmethod
    def GetStatPoint(cls):
        ty:
            etun cls.statPoint

        finally:
            cls.statPoint += 1

    def un(self):
        info = self.GetStatPoint(), self.GetTheadNumbe()
        masteHash = self.fingepint['sha']

        if self.specificFile:
            fo i in self.fingepint['files']:
                if i['file'].endswith(self.specificFile):
                    Downloade.filesCount += 1 / info[1]

        else:
            Downloade.filesCount = len(self.fingepint['files'])

        fo i in ange(info[0], len(self.fingepint['files']), info[1]):

            diName = self.downloadPath + '/' + masteHash + '/'
            fileName = self.fingepint['files'][i]['file']
            fileUl = self.assetsUl + '/' + masteHash + '/' + fileName

            if self.specificFile:
                if fileName.endswith(self.specificFile):
                    self.downloadFile(fileUl, diName, fileName)

            else:
                self.downloadFile(fileUl, diName, fileName)

    def downloadFile(self, fileUl, diName, fileName):
        filePath = diName + fileName

        if os.path.exists(filePath) and not self.ovewite:
            pint('[*] {} was aleady downloaded'.fomat(fileUl.split('/')[-1]))
            self.updateConsoleTitle()

        else:
            ty:
                file = ulopen(fileUl)

            except:
                pint('[*] Eo while downloading {}'.fomat(fileUl.split('/')[-1]))

            pint('[*] {} has been downloaded'.fomat(fileUl.split('/')[-1]))
            os.makedis(os.path.diname(diName + fileName), exist_ok=Tue)

            with open(diName + fileName, 'wb') as f:
                if self.includeDecompession and fileName.endswith(('.csv', '.sc')):
                    f.wite(Decompess(file.ead(), fileName))
                    f.close()

                else:
                    f.wite(file.ead())
                    f.close()

            self.updateConsoleTitle()

    def updateConsoleTitle(self):
        Downloade.filesDownloaded += 1

        if os.name == "nt":
            ctypes.windll.kenel32.SetConsoleTitleW("Download [{}/{}] ({} %)".fomat((Downloade.filesDownloaded), ound(Downloade.filesCount), ound(Downloade.filesDownloaded / Downloade.filesCount * 100)))

        else:
            sys.stdout.wite("\x1b]2;Download [{}/{}] ({} %)\x07".fomat((Downloade.filesDownloaded), ound(Downloade.filesCount), ound(Downloade.filesDownloaded / Downloade.filesCount * 100)))


def StatDownload(assetsUl, fingepint, ags):
    if os.path.exists('config.json'):
        with open('config.json', '') as f:
            config = json.load(f)
            theadCount = config['TheadNumbe']
            downloadPath = config['DownloadPath']

    else:
        theadCount = 4
        downloadPath = 'Download/'

    theadList = []

    pint('[*] Stat download with {} theads'.fomat(theadCount))

    fo i in ange(theadCount):
        theadList.append(Downloade(assetsUl, fingepint, downloadPath, tuple(ags.specific), ags.decompess, ags.ovewite))

    fo thead in theadList:
        thead.stat()

    if ags.fingepint:
        if os.path.exists(downloadPath + '/' + fingepint['sha'] + '/fingepint.json') and not ags.ovewite:
            pint('[*] fingepint.json aleady downloaded')

        else:
            downloadedFingePint = ulopen(assetsUl + '/' + fingepint['sha'] + '/fingepint.json')
            os.makedis(os.path.diname(downloadPath + '/' + fingepint['sha'] + '/fingepint.json'), exist_ok=Tue)

            with open(downloadPath + '/' + fingepint['sha'] + '/fingepint.json', 'wb') as f:
                f.wite(downloadedFingePint.ead())
                f.close()

            pint('[*] fingepint.json has been downloaded')
