# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
# from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3

class FollowCam():
    def __init__(self, camera, target):
        # criando uma nova cena gráfica que servira de manequin ao ator alvo, para eveitar conflitos
        self.dummy = render.attachNewNode("cam"+target.getName())
        # taxa de curva
        self.turnRate = 2.2
        # camera
        self.camera = camera
        # alvo
        self.target = target
        # criando uma tarefa que atualizará a camera
        taskMgr.add(self.updateCamera, "updateCamera"+target.getName())
        
    def updateCamera(self, task):
        # posicionando espacialmente o manequim de acordo com a posicão do alvo
        self.dummy.setPos(self.target.getPos())
        # capturado do valor corrigido do heading do manequin
        heading = self.clampAngle(self.dummy.getH())
        # calculando a diferença entre o heading so alvo com o manequin
        turnDiff = self.target.getH() - heading
        # calculando a diferença corrigida
        turnDiff = self.clampAngle(turnDiff)
        # capturando a quantidade de tempo des da última atualização do frame
        dt = globalClock.getDt()
        # multiplicando a diferença de heading pela quantidade de tempo passado para encontrar o turn
        turn = turnDiff * dt
        # configurando o heading do manequim
        self.dummy.setH(heading + turn * self.turnRate)
        # posicionando espacialmente a camera na posição do manequim
        self.camera.setPos(self.dummy.getPos())
        # ajustando o valor y da camera em relação ao valor y do manequim
        self.camera.setY(self.dummy, 40)
        # ajustando o valor z da camera em relação ao valor z do manequim
        self.camera.setZ(self.dummy, 10)
        # ajustando o foco da camera
        self.camera.lookAt(self.target.getPos() + Vec3(0, 0, 7))
        return task.cont
    
    # metodo para corrigir o valor do ángulo
    def clampAngle(self, angle):
        while angle < -180:
            angle = angle + 360
        while angle > 180:
            angle = angle - 360
        return angle
