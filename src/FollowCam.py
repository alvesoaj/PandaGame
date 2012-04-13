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
        
        heading = self.clampAngle(self.dummy.getH())
        turnDiff = self.target.getH() - heading
        turnDiff = self.clampAngle(turnDiff)
        dt = globalClock.getDt()
        turn = turnDiff * dt
        self.dummy.setH(heading + turn * self.turnRate)
        self.camera.setPos(self.dummy.getPos())
        self.camera.setY(self.dummy, 40)
        self.camera.setZ(self.dummy, 10)
        self.camera.lookAt(self.target.getPos() + Vec3(0, 0, 7))
        return task.cont
    
    def clampAngle(self, angle):
        while angle < -180:
            angle = angle + 360
        while angle > 180:
            angle = angle - 360
        return angle
