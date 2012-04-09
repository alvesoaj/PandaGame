# -*- coding: UTF-8 -*-
'''
    @author: zerokol
'''
from direct.showbase.ShowBase import ShowBase
from panda3d.core import GeoMipTerrain

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # criando uma instância de um objeto GeoMipTerrain chamado "terrain"
        self.terrain = GeoMipTerrain("terrain")
        # configurando o objeto terrain com a imagem de campo de altura chamada height.png
        self.terrain.setHeightfield("../textures/height.png")
        # aplicando a textura do terreno
        self.terrain.setColorMap("../textures/grass.png")
        # Configurando a escala de variação do eixo Z na construção do terreno
        self.terrain.getRoot().setSz(50)
        # adicionando o objeto terrain a raiz da cena gráfica
        self.terrain.getRoot().reparentTo(render)
        # efetivamente gerando matemática e geometricamente o terreno
        self.terrain.generate()
        # capiturando a elevação na coordenada (256,256) do terreno
        # e multiplicando por a elevação máxima do terreno somado com um valor de segurança para maior precisão
        z = self.terrain.getElevation(256, 256) * (50 + 10)
        # posicionando a câmera padrão no centro do terreno a uma altura maior que o ponto mais alto
        self.cam.setPos(256, 256, z)
        # informando que o ponto de foco será na região onde a câmera está
        self.terrain.setFocalPoint(self.cam)
        # Tarefa para atualizar sempre o ponto de foco do terreno, a medida que a ãmera se movimenta
        self.taskMgr.add(self.updateTerrain, "update terrain")
        
    def updateTerrain(self, task):
        self.terrain.update()
        return task.cont
