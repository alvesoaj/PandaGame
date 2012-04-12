# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
from direct.showbase.RandomNumGen import RandomNumGen
from direct.actor.Actor import Actor
from panda3d.core import Vec3
from direct.interval.IntervalGlobal import Func, Sequence

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # carregando um ator chamado panda
        self.panda = Actor("panda", {"walk": "panda-walk"})
        # relacionando o ator panda a cena gráfica raiz
        self.panda.reparentTo(render)
        # rotacionanado espacialmente o ator panda
        self.panda.setHpr(-90, 0, 0)
        # iniciando a animação walk no ator panda
        self.panda.loop("walk")
        
        # configurando o movimento de ir
        self.walkIval1 = self.panda.posInterval(2, Vec3(-8, 0, 0), startPos = Vec3(8, 0, 0))
        # configurando o movimento de voltar
        self.walkIval2 = self.panda.posInterval(2, Vec3(8, 0, 0), startPos = Vec3(-8, 0, 0))
        # configurando o movimento de virar a esquerda
        self.turnIval1 = self.panda.hprInterval(0.5, Vec3(90, 0, 0), startHpr = Vec3(-90, 0, 0))
        # configurando o movimento de virar a direita
        self.turnIval2 = self.panda.hprInterval(0.5, Vec3(-90, 0, 0), startHpr = Vec3(90, 0, 0))
        # criando uma função de intervalo
        self.colorIval = Func(self.randomColor)
        # instanciando um objerto Sequence para coordenar e repetir os intervalos criados
        self.pandaWalk = Sequence(self.walkIval1, self.turnIval1, self.colorIval, self.walkIval2, self.turnIval2, self.colorIval)
        # colocando o objeto pandaWalk em loop infinito
        self.pandaWalk.loop()
        
        # posicionando espacialmente a camera principal
        self.cam.setPos(0, -50, 6)
    
    def randomColor(self):
        rand = RandomNumGen(globalClock.getFrameTime())
        self.panda.setColorScale(rand.random(), rand.random(), rand.random(), 255)
