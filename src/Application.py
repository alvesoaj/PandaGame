# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Vec3
from pandac.PandaModules import loadPrcFileData

# habilitando a aba de ferramentas
loadPrcFileData("", "want-directtools #t")
loadPrcFileData("", "want-tk #t")

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # importando um objeto "Model", teapot, com auxílio do objeto "loader"
        self.teapot = loader.loadModel("teapot")
        # adicionando o objeto teapot ao objeto raiz, "render"
        self.teapot.reparentTo(render)
        # posicionando o objeto teapot cinco unidades espacialmente a esquerda
        self.teapot.setPos(-5, 0, 0)
        # importando um objeto "Actor" panda, e seus movimentos
        self.pandaActor = Actor("panda", {"walk": "panda-walk"})
        # adicionando o objeto pandaActor ao objeto raiz, "render"
        self.pandaActor.reparentTo(render)
        # posicionando o objeto pandaActor cinco unidades espaciais a direita
        # self.pandaActor.setPos(Vec3(5, 0, 0))
        self.pandaActor.setPos(5, 0, 0)
        # colocando o ator pandaActor em loop na animação "walk"
        self.pandaActor.loop("walk")
        # configurando a camera padrão "cam" para a posição apropriada
        self.cam.setPos(0, -30, 6)
