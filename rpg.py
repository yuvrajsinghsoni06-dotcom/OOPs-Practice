from abc import ABC , abstractmethod

# --- WEAPONS ---
class Weapon(ABC):
    @abstractmethod
    def use(self):
        pass

class Sword(Weapon):
    def use(self):
        return f"Slash with the Sharp steel!!"

class Bow(Weapon):
    def use(self):
        return f"Shoot the Arrow!!"

# --- MAGIC ---
class Magic(ABC):
    @abstractmethod
    def cast(self): # <--- The Contract says "cast"
        pass

class FireBall(Magic):
    def cast(self): # <--- FIX: Changed from 'use' to 'cast' to match Interface
        return f"Hurl a Ball of Fire ! Boom"

class Heal(Magic):
    def cast(self): # <--- FIX: Changed from 'use' to 'cast'
        return f"A holy heal your Wounds.."

# --- CHARACTER ---
class Character:
    def __init__(self, name, starting_weapon, spell):
        self._name = name
        self._weapon = starting_weapon
        self._spell = spell
        
    def behavior(self):
        action = self._weapon.use()
        return f"{self._name} attacks: {action}"
    
    def equip_weapon(self, new_weapon):
        self._weapon = new_weapon
        return f">> Weapon Switching is Successful to {self._weapon}"
        
    def cast_spell(self):
        return f"{self._name} casts: {self._spell.cast()}" # Calls 'cast' on the spell object

# --- TEST CASE ---
Spear = Sword()
Divin_Bow = Bow()
fireball = FireBall()
healspell = Heal()

person = Character("Auther", Spear, fireball)

print(person.behavior())
print(person.cast_spell()) # <--- FIX: Changed 'person.cast()' to 'person.cast_spell()'
person.equip_weapon(Divin_Bow)
print(person.behavior())