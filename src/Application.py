# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
# import desnecessário
# from direct.interval.FunctionInterval import Func

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # carregando o ator panda
        self.pandaActor = Actor("panda", {"walk": "panda-walk"})
        # relacionando o ator pandaActor a raiz da cena gráfica
        self.pandaActor.reparentTo(render)
        # setando a animação do ator pandaActor
        self.pandaActor.loop("walk")
        # criando um array de cameras,
        # a primeira é a camera padrão, e a segunda é uma nova camera
        self.cameras = [self.cam, self.makeCamera(self.win)]
        # desativando a nova camera, para que só a camera padrão seja utilizada
        self.cameras[1].node().getDisplayRegion(0).setActive(0)
        # criando uma variavel para saber qual camera está ativa
        self.activeCam = 0
        # posicionando espacialmente a camera principal
        self.cameras[0].setPos(0, -30, 6)
        # posicionando espacialmente a camera secuandária
        self.cameras[1].setPos(30, -30, 20)
        # posicionando o foco da camera secundária
        self.cameras[1].lookAt(0, 0, 6)
        # chamando um agendador para executar uma tarefa com atrase de 5 segundos
        self.taskMgr.doMethodLater(5, self.toggleCam, "toggle camera")
        
    def toggleCam(self, task):
        # desativando a camera que estava ativa
        self.cameras[self.activeCam].node().getDisplayRegion(0).setActive(0)
        # sinalizando que a camera que será ativada é a que está desativda
        self.activeCam = not self.activeCam
        # ativando a camera que estava desativada
        self.cameras[self.activeCam].node().getDisplayRegion(0).setActive(1)
        # retornando um objeto que diz que a tarefa irá se repetir
        return task.again
