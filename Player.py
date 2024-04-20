from dataclasses import dataclass

#this file holds a struct for the player
@dataclass
class playerStats:
    
    shooting: int
    inLineup: bool
    brains: int
    total: int
    name: str

