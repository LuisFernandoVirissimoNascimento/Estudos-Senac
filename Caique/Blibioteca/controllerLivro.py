from livros import Livros
from database import Database

class ControllerLivro:
    def cadastrarLivro(self):
        bd = Database("10.28.2.69","suporte","suporte","blibioteca")
        bd.conectar()

        livros = Livros("bah","nah","wqeqwe",111)
        bd.cursor.execute(livros.create())
        bd.conexao.commit()
        bd.desconectar()

    def DELETARLIVRO(self, codigo):
        bd = Database("10.28.2.69","suporte","suporte","blibioteca")
        bd.conectar()

        bd.cursor.execute(f" delete from livro where id_livro = {codigo};")
        bd.conexao.commit()
        bd.desconectar()

    def reeedlivro(self, codigo):
        bd = Database("10.28.2.69","suporte","suporte","blibioteca")
        bd.conectar()

        bd.cursor.execute(f" delete from livro where id_livro = {codigo};")
        bd.conexao.commit()
        bd.desconectar()

    def upbabe(self, codigo):
        bd = Database("10.28.2.69","suporte","suporte","blibioteca")
        bd.conectar()


        bd.cursor.execute()
        bd.conexao.commit()
        bd.desconectar()


ControllerLivro().cadastrarLivro()

