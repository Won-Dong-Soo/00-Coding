import random
import matplotlib.pyplot as plt

# -----------------------------
# Creature Class
# -----------------------------
class Creature:
    def __init__(self, species):
        self.species = species  # "tteok", "macaron", "rice"
        self.alive = True

    def strategy_against(self, other):
        """Define Rice behavior depending on opponent"""
        if self.species != "rice":
            return self.species
        if other.species == "macaron":
            return "tteok"   # act like tteok
        if other.species == "tteok":
            return "macaron" # act like macaron
        if other.species == "rice":
            return "macaron" # rice vs rice -> macaron strategy
        return "tteok"

# -----------------------------
# Simulation Class
# -----------------------------
class Simulation:
    def __init__(self, num_jars, init_tteok, init_macaron, init_rice, macaron_gen, rice_gen, generations):
        self.num_jars = num_jars
        self.generations = generations
        self.macaron_intro_gen = macaron_gen
        self.rice_intro_gen = rice_gen
        self.initial_macaron = init_macaron
        self.initial_rice = init_rice

        # populations
        self.tteoks = [Creature("tteok") for _ in range(init_tteok)]
        self.macarons = []
        self.rices = []

        self.tteok_history = []
        self.macaron_history = []
        self.rice_history = []

    def compete(self, a, b):
        """Competition logic between two creatures"""
        # Determine strategy types
        species_a = a.strategy_against(b)
        species_b = b.strategy_against(a)

        # macaron vs tteok
        if species_a == "macaron" and species_b == "tteok":
            if random.random() < 0.75:
                b.alive = False
                a.alive = True
                return a, (random.random() < 0.5)
            else:
                a.alive = random.random() >= 0.5
                b.alive = True
                return b, False
        if species_a == "tteok" and species_b == "macaron":
            if random.random() < 0.25:
                b.alive = False
                a.alive = True
                return a, (random.random() < 0.5)
            else:
                a.alive = random.random() >= 0.5
                b.alive = True
                return b, False

        # macaron vs macaron → both die
        if species_a == species_b == "macaron":
            a.alive = False
            b.alive = False
            return None, False

        # tteok vs tteok → one survives
        if species_a == species_b == "tteok":
            survivor = random.choice([a, b])
            survivor.alive = True
            return survivor, False

        return None, False  # fallback

    def run(self):
        for gen in range(self.generations):
            # Introduce new species
            if gen == self.macaron_intro_gen:
                self.macarons = [Creature("macaron") for _ in range(self.initial_macaron)]
            if gen == self.rice_intro_gen:
                self.rices = [Creature("rice") for _ in range(self.initial_rice)]

            sugar_jars = [[] for _ in range(self.num_jars)]

            # Assign creatures to jars
            for c in self.tteoks + self.macarons + self.rices:
                if not c.alive:
                    continue
                idx = random.randrange(self.num_jars)
                attempts = 0
                while len(sugar_jars[idx]) >= 2 and attempts < 10:
                    idx = random.randrange(self.num_jars)
                    attempts += 1
                if len(sugar_jars[idx]) < 2:
                    sugar_jars[idx].append(c)

            new_tteoks, new_macarons, new_rices = [], [], []

            for jar in sugar_jars:
                if len(jar) == 1:
                    c = jar[0]
                    if c.alive:
                        new = Creature(c.species)
                        if c.species == "tteok":
                            new_tteoks.extend([c, new])
                        elif c.species == "macaron":
                            new_macarons.extend([c, new])
                        elif c.species == "rice":
                            new_rices.extend([c, new])
                elif len(jar) == 2:
                    a, b = jar
                    winner, reproduce = self.compete(a, b)
                    if winner and winner.alive:
                        if winner.species == "tteok":
                            new_tteoks.append(winner)
                            if reproduce:
                                new_tteoks.append(Creature("tteok"))
                        elif winner.species == "macaron":
                            new_macarons.append(winner)
                            if reproduce:
                                new_macarons.append(Creature("macaron"))
                        elif winner.species == "rice":
                            new_rices.append(winner)
                            if reproduce:
                                new_rices.append(Creature("rice"))

            # Update populations
            self.tteoks = [t for t in new_tteoks if t.alive]
            self.macarons = [m for m in new_macarons if m.alive]
            self.rices = [r for r in new_rices if r.alive]

            # Record stats
            self.tteok_history.append(len(self.tteoks))
            self.macaron_history.append(len(self.macarons))
            self.rice_history.append(len(self.rices))

            print(f"Gen {gen+1}: Tteok={len(self.tteoks)}, Macaron={len(self.macarons)}, Rice={len(self.rices)}")

    def plot(self):
        plt.plot(self.tteok_history, color="gray", label="Tteok")
        plt.plot(self.macaron_history, color="hotpink", label="Macaron")
        plt.plot(self.rice_history, color="orange", label="Rice")
        plt.xlabel("Generation")
        plt.ylabel("Population")
        plt.title("Tteok vs Macaron vs Rice Dynamics")
        plt.legend()
        plt.show()


# -----------------------------
# Input
# -----------------------------
num_jars = int(input("Number of sugar jars: "))
init_tteok = int(input("Initial Chapsaltteok: "))
init_macaron = int(input("Initial Macaron (spawned later): "))
init_rice = int(input("Initial Rice (spawned later): "))
macaron_gen = int(input("Generation to introduce Macarons: "))
rice_gen = int(input("Generation to introduce Rice: "))
generations = int(input("Total number of generations: "))

# -----------------------------
# Run Simulation
# -----------------------------
sim = Simulation(num_jars, init_tteok, init_macaron, init_rice, macaron_gen, rice_gen, generations)
sim.run()
sim.plot()