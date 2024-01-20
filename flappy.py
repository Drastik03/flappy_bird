from code.window import Windows
class Main:
    def __init__(self):
        try:    
            self.game = Windows()
            self.game.initComponents()
        except Exception as e:
            print(f"Error al inicializar el juego: {e}")

if __name__ == '__main__':
    main_instance = Main()