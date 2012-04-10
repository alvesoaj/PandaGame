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
        # insranciando um objeto Audio3DManager para criar efeitos
        self.audio = Audio3DManager(self.sfxManagerList[0])
        # configurando para a câmera principal ser o objeto ao quel o som irá se relacionar
        self.audio.attachListener(self.cam)
        # criando um objeto AudioSound a partir do objeto Audio3DManager 
        self.loop = self.audio.loadSfx("../sounds/loop.wav")
        # configurando o som em loop infinito
        self.loop.setLoop(True)
        # vinculando o objeto loop ao Model smiley, o som partirá de smiley
        self.audio.attachSoundToObject(self.loop, self.smiley)
        # iniciando a reprodução do som
        self.loop.play()
        # configurando a posição da câmera padrão no espaço
        self.cam.setPos(0, -40, 0)