# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
#from panda3d.core import Vec3

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # carregando o modelo chamado sun
        self.sun = loader.loadModel("smiley")
        # relacionando o modelo sun a raiz da cena gráfica
        self.sun.reparentTo(render)
        # dimensionanco o modelo sun para uma escala de cinco vezes
        self.sun.setScale(5)
        
        # carregando um modelo chamado phanton
        self.phantom = loader.loadModel("teapot")
        # ralacionando o modelo phanton ao modelo sun
        self.phantom.reparentTo(self.sun)
        # dimensionando a escala do modelo phantom para zero ponto um
        self.phantom.setScale(0.1)
        # posicionando espacialmente o modelo phantom
        self.phantom.setPos(0, -5, 0)
        # configurando o objeto phantom como invisivel
        self.phantom.hide()
        
        # carregando um modelo chamdao earth
        self.earth = loader.loadModel("frowney")
        # criando uma nova cena gráfica chamada earthCenter
        self.earthCenter = render.attachNewNode("earthCenter")
        # relacionando o modelo earth a cena gráfica earthCenter
        self.earth.reparentTo(self.earthCenter)
        # posicionando espacialmente o modelo earth
        self.earth.setPos(20, 0, 0)
        
        # carregando um ator chamado panda
        self.panda = Actor("panda", {"walk": "panda-walk"})
        # relacionando o ator panda ao modelo earth
        self.panda.reparentTo(self.earth)
        # dimensionando o ator panda para uma escala de zero ponto um
        self.panda.setScale(0.1)
        # posicionando espacialmente o ator panda
        self.panda.setPos(0.7, 0, 0.7)
        # posicionando direcionalmente o ator panda
        self.panda.setHpr(0, 0, 40)
        # inicinando a animação walk do ator panda
        self.panda.loop("walk")
        
        # carregando um modelo chamado moon
        self.moon = loader.loadModel("box")
        # criando uma nova cena gráfica chamada moonCenter
        self.moonCenter = self.earthCenter.attachNewNode("moonCenter")
        # relacionando o modelo moon a cena gráfica moonCenter
        self.moon.reparentTo(self.moonCenter)
        # posicionando espacialmente a cena gráfica moonCenter na mesma posição do modelo earth 
        self.moonCenter.setPos(self.earth.getPos())
        # posicionando espacialmente o modelo moon
        self.moon.setPos(0, 0, 6)
        
        # posicionando espacialmente a camera padrão
        self.cam.setPos(0, -100, 0)
        # adiciononando uma tarefa a aplicação
        self.taskMgr.add(self.update, "update")
        
    def update(self, task):
        # rotacionando o modelo sun no eixo x em dez unidades vezes o tempo total des de que a tarefa foi iniciada
        self.sun.setP(task.time * 10)
        # rotacionando o modelo earth no eixo z em menos cem unidades vezes o tempo total da tarefa
        self.earth.setH(task.time * -100)
        # rotacionado a cena gráfica earthCenter no eixo z em cinquenta unidades vezes o tempo total da tarefa
        self.earthCenter.setH(task.time * 50)
        # rotacionando a cena gráfica moonCenter no eixo y  em cento e cinquenta unidadess vezes o tempo toral da tarefa
        self.moonCenter.setR(task.time * 150)
        # retornando a tarefa para garantir continuidade
        return task.cont
