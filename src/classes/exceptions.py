class InvalidTypeException(Exception):
    def __init__(self, message="O tipo passado é inválido."):
        """Inicializa uma nova instância da classe InvalidTypeException.

        Parameters
        ----------
        message : str, optional
            Mensagem da exceção, by default "O tipo passado é inválido."
        """
        self.message = message
        super().__init__(self.message)

class InvalidPositionException(Exception):
    def __init__(self, message="A posição passada é inválida."):
        """Inicializa uma nova instância da classe InvalidPositionException.

        Parameters
        ----------
        message : str, optional
            Mensagem da exceção, by default "A posição passada é inválida."
        """
        self.message = message
        super().__init__(self.message)

class NoImageException(Exception):
    def __init__(self, message="Não foi possível carregar a imagem."):
        """Inicializa uma nova instância da classe NoImageException.

        Parameters
        ----------
        message : str, optional
            Mensagem da exceção, by default "Não foi possível carregar a imagem."
        """
        self.message = message
        super().__init__(self.message)