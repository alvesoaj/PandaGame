# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
# from direct.actor.Actor import Actor
from direct.directutil.Mopath import Mopath
from direct.interval.IntervalGlobal import MopathInterval

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # carregando o modelo smiley
        self.smiley = self.loader.loadModel("smiley")
        # relacionando o modelo smiley com a raiz da cena gráfica
        self.smiley.reparentTo(render)
        # criando um objeto Mopath
        self.mopath = Mopath()
        # carregando o arquivo que será usado como path
        self.mopath.loadFile("../models/path.egg")
        # através de um objeto MopathInterval, vinculando o path mopath ao modelo smiley e sua duração
        self.ival = MopathInterval(self.mopath, self.smiley, duration = 10)
        # colocando o interpolador em loop infinito
        self.ival.loop()
        # posicionando espacialmente a camera principal
        self.cam.setPos(0, -20, 0)
