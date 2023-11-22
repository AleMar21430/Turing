from typing import List
import yaml

class YAML_Turing:
	tape: 'Tape'

	def init (self):
		self.tape = Tape()
		self.tape_alphabet
		self.alphabet
		self.states

		self.initial_state
		self.accept_state
		self.final_states

		self.current_state
		self.blank_symbol
		self.delta

class Tape:
	tape: List[str]
	head_position: int = 0
	blank_symbol: str

	def init (self, tape: str, epsilon: str):
		self.tape = list(tape)
		self.blank_symbol = epsilon
