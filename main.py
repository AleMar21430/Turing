from typing import List, Dict
import yaml

class YAML_Turing:
	tape: "Tape"
	states: str
	initial_state: str
	final_states: str
	accept_state: str
	alphabet: str
	tape_alphabet: str
	blank_symbol: str
	delta: str
	current_state: str


class Tape:
	tape: List[str]
	head_position: int = 0
	blank_symbol: str

with open("machine.yaml", "r") as file: config = yaml.safe_load(file)

machine               = YAML_Turing()
machine.tape          = None
machine.delta         = config["delta"]
machine.states        = config["q_states"]["q_list"]
machine.alphabet      = config["alphabet"]
machine.blank_symbol  = config["blank"]
machine.final_states  = config["q_states"]["final"]
machine.accept_state  = config["q_states"]["accept"]
machine.tape_alphabet = config["tape_alphabet"]
machine.initial_state = config["q_states"]["initial"]
machine.current_state = machine.initial_state