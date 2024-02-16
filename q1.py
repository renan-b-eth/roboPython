import time
from util import Mapa

class Control(): # A Classe Control Herdando da Classe Mapa
    mapa = Mapa()

    def __init__(self):
        # Inicializa a classe Pai
        ## seu código aqui

        # maquina de estados
        self.robot_state = 'stop'
        self.state_machine = {
            'forward': self.forward,
            'left': self.left,
            'right': self.right,
            'stop': self.stop,
        }

    
    
    def forward(self) -> None:
        # Move subtraindo 1 uma linha
        # Atualiza a posição
        self.mapa.posicao = ((self.mapa.linhas-1),self.mapa.colunas)
        self.mapa.atualizar_posicao(self.mapa.posicao)
        pass


    def left(self) -> None:
        # Move subtraindo 1 uma coluna
        # Atualiza a posição
        self.mapa.posicao = (self.mapa.linhas,(self.mapa.colunas-1))
        self.mapa.atualizar_posicao(self.mapa.posicao)
        pass

    def right(self) -> None:
        # Move somando 1 uma coluna
        # Atualiza a posição
        self.mapa.posicao = (self.mapa.linhas,(self.mapa.colunas+1))
        self.mapa.atualizar_posicao(self.mapa.posicao)
        pass
    
    def stop(self) -> None:
        # Não faz nada
        pass

    def mostrar(self) -> None:
        print(self.mapa.linhas)
        self.mapa.atualizar_posicao(self.mapa.posicao)
        print(self.mapa.linhas)
        pass

    def control(self) -> None:
        # Verifica se a posição acima está livre, se sim, move para cima.
        # Se não, verifica se a posição à esquerda ou à direita está livre, se sim, move para um dos lados.
        # Pare quando estiver na primeira linha.
        

        # Chamada do método de movimento a partir do dicionário
        # por exemplo.....
        # self.robot_state = 'forward'  # para mudar o estado
        self.robot_state = 'forward'
        # self.state_machine[self.robot_state]() # para chamar o método correspondente
        self.state_machine[self.robot_state]()


        # Mostre a grade atual
        self.mostrar()
        pass

def main():
    # Inicializa a classe Control como control
    # seu código aqui
    control = Control(); 
    
    
    #chama o método mostrar
    control.mostrar()
    
    i = 40
    
    while not control.robot_state == 'stop' and i > 0:
        control.control()
        time.sleep(1)
        i -= 1

if __name__=="__main__":
    main()