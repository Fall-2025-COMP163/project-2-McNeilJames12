"""
COMP 163 - Project 2: Character Abilities Showcase
Name: James McNeil
Date: 11/08/25

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

import random

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        # Store each fighter for the battle
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")

        # Show starting stats for both characters
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)

        # Only allow counterattack if character2 is still alive
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)

        # Display results at the end of the battle
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()

        # Decide and announce the winner
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """

    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        # Store shared attributes used by all character types
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic


    def attack(self, target):
        """
        Basic attack method that all characters can use.
        Uses strength as the main source of damage.
        """
        # Basic physical damage based on strength
        damage = self.strength
        print(f"{self.name} attacks target for {damage} damage!")
        target.take_damage(damage)


    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # Subtract damage from health
        self.health -= damage
        if self.health < 0:
            self.health=0
        if self.health == 0:
            print(f"{self.name} takes {damage} damage! Health is now: {self.health}.")


    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        # Show formatted stats for readability
        print("===================================")
        print(f"Name:     {self.name}")
        print(f"Health:   {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic:    {self.magic}")
        print("===================================")

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """

    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Calls the base class constructor, then adds class/level/XP.
        """
        # Call parent constructor to set shared stats
        super().__init__(name, health, strength, magic)

        # Player-specific attributes
        self.character_class = character_class
        self.level = 1
        self.experience = 0



    def display_stats(self):
        """
        Show both base stats and extra player information.
        """
        # Display base stats first
        super().display_stats()

        # Add player-specific info
        print(f"Class:   {self.character_class}")
        print(f"Level:   {self.level}")
        print(f"Experience:   {self.experience}")
        print("===================================")

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Warriors specialize in physical power.
        """
        # Provide strong physical stats to the warrior
        super().__init__(name, "Warrior", health = 120, strength = 15, magic = 5)


    def attack(self, target):
        """
        Warrior attack has bonus damage compared to basic attack.
        """
        # Warrior-specific bonus to physical damage
        damage = self.strength + 5
        print(f"{self.name} attacks target for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """
        Special warrior ability - extremely strong attack.
        """
        # Heavy bonus on top of strength for power strike
        damage = self.strength + 15
        print(f"{self.name} unleashes a POWER STRIKE on the target for {damage} damage!")
        target.take_damage(damage)

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Mages specialize in magic attacks and abilities.
        """
        # Provide magic-focused stat distribution
        super().__init__(name, "Mage", health = 80, strength = 8, magic = 20)

    def attack(self, target):
        """
        Mage attack uses magic instead of strength.
        """
        # Magic-based primary attack
        damage = self.magic + 7
        print(f"{self.name} attacks target for {damage} damage!")
        target.take_damage(damage)


    def fireball(self, target):
        """
        High-damage magical spell.
        """
        # Fireball adds strong bonus to magic stat
        damage = self.magic + 20
        print(f"{self.name} reveals that they have a powerful spell that hits the target for {damage} damage!")
        target.take_damage(damage)

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Rogues balance speed and precision.
        """
        # Balanced stat distribution with crit mechanics
        super().__init__(name, "Rogue", health = 90, strength = 12, magic = 10)

    def attack(self, target):
        """
        Rogue has a chance for a critical hit.
        """
        # Base damage for rogue
        damage = self.strength

        # Roll to check for critical hit (approx. 30% chance)
        roll = random.randint(1, 10)
        if roll <= 3:
            damage *= 2  # Apply crit multiplier
            print(f"💥 CRITICAL HIT! {self.name} strikes {target.name} for {damage} damage!")
        else:
            print(f"{self.name} swiftly attacks {target.name} for {damage} damage.")

    def sneak_attack(self, target):
        """
        Guaranteed critical hit attack.
        """
        # Always double damage for sneak attack
        damage = self.strength * 2
        print(f"{self.name} attacks target with a SNEAK ATTACK for {damage} damage!")
        target.take_damage(damage)

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """

    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # Store info for weapon bonuses
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """
        Display information about this weapon.
        """
        # Print weapon stats
        print(f"Weapon: {self.name} (Damage Bonus: + {self.damage_bonus})")

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create one instance of each character subclass
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    # Display initial stats for all characters
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Demonstrate polymorphism: same method name, different results
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    # Loop through each character and call attack to show differences
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset after each test

    # Test each character's unique special ability
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)

    # Demonstrate composition via Weapon objects
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Run a full simulated battle
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
