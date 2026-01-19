# --- THE PARENT CLASS (The Blueprint) ---
class Character:
    # 1. We only pass DATA here (Name, Health, Power)
    def __init__(self, name, health, power):
        self._name = name
        self._health = health
        self._power = power

    # 2. This is a robust string representation
    def __str__(self):
        return f"{self._name} (HP: {self._health})"

    # 3. The "Receiver" Logic (Same for everyone)
    # This method changes the data safely
    def take_damage(self, amount):
        self._health -= amount
        if self._health < 0:
            self._health = 0
        print(f" > {self._name} took {amount} damage! HP is now {self._health}.")

    # 4. The "Check" Logic
    def is_alive(self):
        return self._health > 0


# --- THE CHILD CLASS (The Specific Implementation) ---
class Warrior(Character):
    # Note: Warrior doesn't need its own __init__ if it's exactly the same as Parent!
    # We just inherit it automatically.

    # POLYMORPHISM: The Warrior attacks differently than others
    def attack(self, target):
        # 1. Calculate Damage (Warriors are strong! 1.5x Multiplier)
        damage_amount = self._power * 1.5
        
        print(f"⚔️ {self._name} swings a giant sword at {target._name}!")
        
        # 2. Apply damage to the TARGET (Interacting with another object)
        target.take_damage(damage_amount)

class Mage(Character):
    def attack(self,target):
        damage = self._power * 3
        print(f"⚔️ {self._name} swings a giant fireball at {target._name}!")
        target.take_damage(damage)
        self.take_damage(5)

opponent1 = Warrior("Auther",9000,105)
opponent2 = Mage("Odin",1890,320)
# --- BATTLE START ---
print("--- BATTLE START ---")
print(opponent1) # Print initial stats
print(opponent2)

while opponent1.is_alive() and opponent2.is_alive():
    
    # 1. Warrior Attacks Mage
    opponent1.attack(opponent2)
    
    # CRITICAL CHECK: Did the Mage die? 
    # If yes, stop the fight immediately! Don't let a dead mage cast spells.
    if not opponent2.is_alive():
        break 
        
    # 2. Mage Attacks Warrior
    opponent2.attack(opponent1)
    
    # Note: We don't need a break check here because the 'while' loop 
    # will check opponent1.is_alive() at the start of the next turn.

    print("--- End of Round ---")
    # Optional: Print stats to track the fight
    print(opponent1)
    print(opponent2)
    print(" ") # Empty line for readability

# --- GAME OVER LOGIC (Outside the loop) ---
print("--- GAME OVER ---")

if opponent1.is_alive():
    print(f"🏆 The Winner is {opponent1._name} (Warrior)!")
else:
    print(f"🏆 The Winner is {opponent2._name} (Mage)!")

