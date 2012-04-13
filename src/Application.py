# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Vec3
from direct.interval.IntervalGlobal import Sequence
# importação local
from FollowCam import FollowCam

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # carregando o modelo world que será o ambiente
        self.world = loader.loadModel("environment")
        # relacionando o modelo world com a cena gráfica raiz
        self.world.reparentTo(render)
        # demensionando o modelo world
        self.world.setScale(0.5)
        # posicionando espacialmente o modelo world
        self.world.setPos(-8, 80, 0)
        
        # carregando o ator panda
        self.panda = Actor("panda", {"walk": "panda-walk"})
        # relacionando o ator panda com a cena gráfica raiz
        self.panda.reparentTo(render)
        # rotacionando espacialmente o ator panda
        self.panda.setHpr(270, 0, 0)
        # colocando o ator panda em loop infinito
        self.panda.loop("walk")
        
        # crinado interpoladores de movimento para o ator panda
        self.walkIval1 = self.panda.posInterval(2, Vec3(-8, -8, 0), startPos = Vec3(8, -8, 0))
        self.walkIval2 = self.panda.posInterval(2, Vec3(-8, 8, 0), startPos = Vec3(-8, -8, 0))
        self.walkIval3 = self.panda.posInterval(2, Vec3(8, 8, 0), startPos = Vec3(-8, 8, 0))
        self.walkIval4 = self.panda.posInterval(2, Vec3(8, -8, 0),startPos = Vec3(8, 8, 0))
        self.turnIval1 = self.panda.hprInterval(0.5, Vec3(180, 0, 0), startHpr = Vec3(270, 0, 0))
        self.turnIval2 = self.panda.hprInterval(0.5, Vec3(90, 0, 0), startHpr = Vec3(180, 0, 0))
        self.turnIval3 = self.panda.hprInterval(0.5, Vec3(0, 0, 0), startHpr = Vec3(90, 0, 0))
        self.turnIval4 = self.panda.hprInterval(0.5, Vec3(-90, 0, 0), startHpr = Vec3(0, 0, 0))
        
        # cirnado um objeto Sequence para gerenciar os interpoladores de movimento do ator panda
        self.pandaWalk = Sequence(self.walkIval1, self.turnIval1, self.walkIval2, self.turnIval2, self.walkIval3, self.turnIval3, self.walkIval4, self.turnIval4)
        # colocando o objeto Sequence pandaWalk em loop infinito
        self.pandaWalk.loop()
        
        # configurando a camera principal para sequir o ator panda
        self.followCam = FollowCam(self.cam, self.panda)