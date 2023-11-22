from typing import List
import yaml

class Cadena:
	cadena: List[str]
	head_pos: int = 0
	blank_s: str

	def move_head(self, direction: str):
		direction = int(direction)
		self.head_pos += direction
		if direction == 1:
			if self.head_pos >= len(self.cadena):
				self.cadena.append(self.blank_s)
		elif direction == -1:
			if self.head_pos < 0:
				self.head_pos = 0
				self.cadena.insert(0, self.blank_s)

class YAML_Turing:
	cadena: Cadena
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
		current_symbol = self.cadena.cadena[self.cadena.head_pos]
		for rule in self.delta:
			if rule['params']['initial_state'] == self.active_state and rule['params']['tape_input'] == current_symbol:
				new_state = rule['output']['final_state']
				new_symbol = rule['output']['tape_output']
				displacement = rule['output']['tape_displacement']
				self.cadena.cadena[self.cadena.head_pos] = new_symbol
				self.cadena.move_head(displacement)
				return self.active_state, current_symbol, new_state, new_symbol, displacement

	def execute(self):
		yaml_temp = []
		yaml_temp.append(f"{self.active_state}{''.join(self.cadena.cadena)}")
		while self.active_state not in self.final_states:
			prev_state, _, new_state, _, _ = self.iteration()
			yaml_temp.append(f"{prev_state}{''.join(self.cadena.cadena)} - {new_state}{''.join(self.cadena.cadena)}")
			self.active_state = new_state
		is_accepted = self.active_state in self.accept_state
		final_tape_output = ''.join(self.cadena.cadena).rstrip(self.blank_symbol)
		return is_accepted, final_tape_output, yaml_temp

with open("machine.yaml", "r") as file: config = yaml.safe_load(file)

machine               = YAML_Turing()
machine.cadena          = None
machine.delta         = config["delta"]
machine.states        = config["q_states"]["q_list"]
machine.alphabet      = config["alphabet"]
machine.blank_symbol  = config["blank"]
machine.final_states  = config["q_states"]["final"]
machine.accept_state  = config["q_states"]["accept"]
machine.active_state  = config["q_states"]["initial"]
machine.tape_alphabet = config["tape_alphabet"]
machine.initial_state = config["q_states"]["initial"]

Input = "abbbb"

machine.cadena = Cadena()
machine.cadena.cadena = list(Input)
machine.cadena.blank_s = machine.blank_symbol

result, tape, iterations = machine.execute()
print(f"\n\n---------------Cadena--------------\n{Input}\n--------Pasos de la Máquina--------")
for iteration in iterations: print(iteration)
print(f"-------------Resultado-------------\n{tape}\n----------Cadena aceptada----------\n{('SI✅' if result else 'No⛔')}\n\n")