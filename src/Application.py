# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
from direct.showbase.Audio3DManager import Audio3DManager

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # carregando um Model simples utilizando o objeto loader
        self.smiley = loader.loadModel("smiley")
        # adicionando o objeto smaley a raiz da cena gráfica
        self.smiley.reparentTo(render)
        self.audio = Audio3DManager(self.sfxManagerList[0])
        self.audio.attachListener(self.cam)
        self.loop = self.audio.loadSfx("../sounds/loop.wav")
        self.loop.setLoop(True)
        self.audio.attachSoundToObject(self.loop, self.smiley)
        self.loop.play()
        self.cam.setPos(0, -40, 0)