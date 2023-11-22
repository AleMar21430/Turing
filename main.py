from typing import List
import yaml

class YAML_Turing:
	tape: 'Tape'
	states: str
	alphabet: str

	initial_state: str
	active_state: str
	final_states: str
	accept_state: str

	delta: str
	blank_symbol: str
	tape_alphabet: str

	def iteration(self):
		current_symbol = self.tape[self.tape.head_pos]
		for rule in self.delta:
			if rule['params']['initial_state'] == self.active_state and rule['params']['tape_input'] == current_symbol:
				new_state = rule['output']['final_state']
				new_symbol = rule['output']['tape_output']
				displacement = rule['output']['tape_displacement']
				self.tape[self.tape.head_pos] = new_symbol
				self.tape.move_head(displacement)
				return self.active_state, current_symbol, new_state, new_symbol, displacement

	def execute(self):
		yaml_temp = []
		yaml_temp.append(f"{self.active_state}{''.join(self.tape.tape)}")
		while self.active_state not in self.final_states:
			prev_state, _, new_state, _, _ = self.iteration()
			yaml_temp.append(f"{prev_state}{''.join(self.tape.tape)} - {new_state}{''.join(self.tape.tape)}")
			self.active_state = new_state
		is_accepted = self.active_state in self.accept_state
		final_tape_output = ''.join(self.tape.tape).rstrip(self.blank_symbol)
		return is_accepted, final_tape_output, yaml_temp

class Tape:
	tape: List[str]
	head_pos: int = 0
	blank_s: str

	def move_head(self, direction: int):
		self.head_pos += direction
		if direction == 1:
			if self.head_pos >= len(self.tape):
				self.tape.append(self.blank_s)
		elif direction == -1:
			if self.head_pos < 0:
				self.head_pos = 0
				self.tape.insert(0, self.blank_s)


with open("machine.yaml", "r") as file: config = yaml.safe_load(file)

machine               = YAML_Turing()
machine.tape          = None
machine.delta         = config["delta"]
machine.states        = config["q_states"]["q_list"]
machine.alphabet      = config["alphabet"]
machine.blank_symbol  = config["blank"]
machine.final_states  = config["q_states"]["final"]
machine.accept_state  = config["q_states"]["accept"]
machine.active_state  = config["q_states"]["initial"]
machine.tape_alphabet = config["tape_alphabet"]
machine.initial_state = config["q_states"]["initial"]

Input = ""

machine.tape = Tape()
machine.tape.tape = list(Input)
machine.tape.blank_s = machine.blank_symbol

result, tape, iterations = machine.execute()
print(f"Cinta de entrada:\n {Input}\nPasos de la Máquina de Turing:")
for iteration in iterations: print(iteration)
print(f"\nResultado de la Máquina de Turing:\n{tape}\nCadena aceptada: {('SI✅' if result else 'No⛔')}")