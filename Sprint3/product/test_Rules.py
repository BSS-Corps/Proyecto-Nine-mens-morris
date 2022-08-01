from pickle import TRUE
import pytest
from Rules import Rules
from Tablero import Tablero
from Player import Player


class TestRules:
    board = Tablero()
    rules = Rules()
    player = Player(0,'B')


    def test_casillaVaciaOk(self):
        assert self.rules.casillaVacia(0,self.board.board) == True

    def test_casillaVaciaNoOk(self):
        self.board.board = list("Wxxxxxxxxxxxxxxxxxxxxxxx")
        assert self.rules.casillaVacia(0,self.board.board) == False 

    def test_colocarPiezaOk(self):
        self.rules.colocarPieza(3,self.player,self.board.board)
        assert self.board.board[3] == self.player.simb


    def test_changeTurn(self):
        assert self.rules.changeTurn(self.player) == self.player
        

    def test_checkmill_pass(self):
        self.board.board = "WWWxxxxxxxxxxxxxxxxxxxxx"
        assert self.rules.check_mill(0,self.board.board) == True

    def test_checkmill_nopass(self):
        self.board.board = list("WWBxxxxxxxWBBxxxxxxxxxxx")
        assert self.rules.check_mill(0,self.board.board) == False

    def test_removerPieza(self):
        assert self.rules.removerPieza(2,self.player,self.board.board) == True

