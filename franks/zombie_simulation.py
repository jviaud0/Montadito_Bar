import logging
import threading
import time
import random
import concurrent.futures
import traceback
import mysql.connector
import webbrowser


class Nuke:
    def __init__(self, id, city):
        self.id = id
        self.city = city
        self.deployed = False

    def nuking(self):
        try:
            while not self.deployed:
                self.city.zombie_queue_lock.acquire()
                self.city.healthy_queue_lock.acquire()
                self.city.dead_queue_lock.acquire()
                if (len(self.city.zombie_queue) / (len(self.city.zombie_queue) + len(self.city.healthy_queue))) > 0.95:
                    print(f"City: {self.city.name} is in a horrible situation, zombies make up more then 95% of the population.")
                    print("Military proposes operation Oppenheimer!")

                    self.city.dead_queue.extend(self.city.healthy_queue)
                    self.city.dead_queue.extend(self.city.zombie_queue)
                    self.city.healthy_queue = []
                    self.city.zombie_queue = []
                    for dead in self.city.dead_queue:
                        dead.alive = False

                    webbrowser.open('https://www.youtube.com/watch?v=bryWiNw9Rzg')
                    self.deployed = True
                    print(f"NUCLEAR BOMB DEPLOYED IN {self.city.name}")
                self.city.zombie_queue_lock.release()
                self.city.healthy_queue_lock.release()
                self.city.dead_queue_lock.release()
                time.sleep(0.5)
        except Exception:
            print(Exception)


class Military:
    def __init__(self, id, type, rank, city_name):
        self.id = id
        self.type = type
        self.rank = rank
        self.city_name = city_name
        self.infected = False
        self.alive = True
        self.job = "Military"
        self.city_name.healthy_queue_lock.acquire()
        self.city_name.healthy_queue.append(self)
        self.city_name.healthy_queue_lock.release()
        print("Military", id, "was created in", city_name.name)

    def zombie_destruction(self):
        try:
            while True:
                if self.alive == False:
                    print(f"Thread Soldier {self.id}, is dead, thread stopping.")
                    break
                self.city_name.zombie_queue_lock.acquire()
                if len(self.city_name.zombie_queue) <= 45:
                    self.city_name.zombie_queue_lock.release()
                    print("Military disactivated!")
                    time.sleep(5)
                elif len(self.city_name.zombie_queue) > 45:
                    self.city_name.zombie_queue_lock.release()
                    if self.type == "Soldier":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 5)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 10)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 15)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                    elif self.type == "Soldier Armoured":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 10)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 15)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 20)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                    elif self.type == "Tank":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 15)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 25)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 35)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                    elif self.type == "Plane":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 20)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 30)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 40)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue.remove(moving)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(10)
                if self.infected:
                    print("Military personnel", self.id, "has been infected! ")
                    self.city_name.healthy_queue_lock.acquire()
                    citizen = random.choice(self.city_name.healthy_queue)
                    self.city_name.healthy_queue.remove(citizen)
                    self.city_name.healthy_queue_lock.release()
                    citizen.infected = True
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(10)

        except Exception as e:
            print("There was an error: MILITARY")
            logging.error(traceback.format_exc())
            print(e)


class Medic:
    def __init__(self, id, type, city_name):
        self.id = id
        self.type = type
        self.city_name = city_name
        self.infected = False
        self.alive = True
        self.job = "Medic"
        self.city_name.healthy_queue_lock.acquire()
        self.city_name.healthy_queue.append(self)
        self.city_name.healthy_queue_lock.release()
        print("Medic", id, "was created in", city_name.name)

    def zombie_cure(self):
        try:
            while True:
                if self.alive == False:
                    print(f"Thread Medic {self.id}, is dead, thread stopping.")
                    break
                if self.type == "Medic":
                    self.city_name.zombie_queue_lock.acquire()
                    if len(self.city_name.zombie_queue) / (len(self.city_name.zombie_queue) + len(self.city_name.healthy_queue)) >= 0.75:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(7, 25)
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = random.choice(self.city_name.zombie_queue)
                            self.city_name.zombie_queue.remove(moving)
                            self.city_name.zombie_queue_lock.release()
                            print(moving.job, moving.id, "has been cured! ")
                            moving.infected = False
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    elif 0.75 > len(self.city_name.zombie_queue) / (len(self.city_name.zombie_queue) + len(self.city_name.healthy_queue)) >= 0.5:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(5, 20)
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = random.choice(self.city_name.zombie_queue)
                            self.city_name.zombie_queue.remove(moving)
                            self.city_name.zombie_queue_lock.release()
                            print(moving.job, moving.id, "has been cured! ")
                            moving.infected = False
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    elif 0.5 > len(self.city_name.zombie_queue) / (len(self.city_name.zombie_queue) + len(self.city_name.healthy_queue)) >= 0.25:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(3, 15)
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = random.choice(self.city_name.zombie_queue)
                            self.city_name.zombie_queue.remove(moving)
                            self.city_name.zombie_queue_lock.release()
                            print(moving.job, moving.id, "has been cured! ")
                            moving.infected = False
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    else:
                        self.city_name.zombie_queue_lock.release()
                        print("No need for medics yet!")
                        time.sleep(5)
                if self.infected:
                    print("Medic", self.id, "has been infected! ")
                    self.city_name.healthy_queue_lock.acquire()
                    citizen = random.choice(self.city_name.healthy_queue)
                    self.city_name.healthy_queue.remove(citizen)
                    self.city_name.healthy_queue_lock.release()
                    citizen.infected = True
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(10)

        except Exception as e:
            print("There was an error: MEDIC")
            logging.error(traceback.format_exc())
            print(e)


class Contamination:
    def __init__(self, id, cities):
        self.id = id
        self.cities = cities

    def check_contamination(self):
        while True:
            try:
                if random.random() < 0.05:
                    print(f"Alert: {self.cities.name} has been contaminated due to the fires and gases!")
                    n_of_ppl = random.randrange(1, 10)
                    for i in range(n_of_ppl):
                        self.cities.healthy_queue_lock.acquire()
                        citizen = random.choice(self.cities.healthy_queue)
                        self.cities.healthy_queue_lock.release()
                        citizen.alive = False
                        self.cities.dead_queue_lock.acquire()
                        self.cities.dead_queue.append(citizen)
                        self.cities.dead_queue_lock.release()
                        time.sleep(0.5)
                    if n_of_ppl > 0:
                        print(f"Simulation: {int(n_of_ppl)} people have died in {self.cities.name} due to contamination.")
                    self.cities.healthy_queue_lock.acquire()
                    if n_of_ppl > 0.2 * len(self.cities.healthy_queue):
                        print(f"Alert: {self.cities.name} has lost more than 10% of its population due to contamination!")
                    self.cities.healthy_queue_lock.release()
                else:
                    time.sleep(2)

            except Exception as e:
                print(f"An error occurred: {e}")


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.healthy_queue = []
        self.zombie_queue = []
        self.dead_queue = []
        self.healthy_queue_lock = threading.Lock()
        self.zombie_queue_lock = threading.Lock()
        self.dead_queue_lock = threading.Lock()


class Citizen:
    def __init__(self, id, city_name):
        self.id = id
        self.alive = True
        self.infected = False
        self.city_name = city_name
        self.job = "Civil"
        choice1 = random.choices(["healthy", "infected"], [99, 1])[0]
        if choice1 == "healthy":
            self.city_name.healthy_queue_lock.acquire()
            self.city_name.healthy_queue.append(self)
            self.city_name.healthy_queue_lock.release()
        elif choice1 == "infected":
            self.city_name.zombie_queue_lock.acquire()
            self.city_name.zombie_queue.append(self)
            self.city_name.zombie_queue_lock.release()
            self.infected = True
        print("Citizen", self.id, "was created in", self.city_name.name)

    def zombify(self):
        try:
            while self.alive:
                if self.infected:
                    print("Citizen", self.id, "has been infected in", self.city_name.name)
                    chance = random.choice([1, 0])
                    if chance == 1:
                        self.city_name.healthy_queue_lock.acquire()
                        if self.city_name.healthy_queue:
                            citizen = random.choice(self.city_name.healthy_queue)
                            self.city_name.healthy_queue.remove(citizen)
                            self.city_name.healthy_queue_lock.release()
                            citizen.infected = True
                            print("Citizen", self.id, "INFECTED", citizen.job, citizen.id)
                            self.city_name.zombie_queue_lock.acquire()
                            self.city_name.zombie_queue.append(citizen)
                            self.city_name.zombie_queue_lock.release()
                        else:
                            print("No more healthy in", self.city_name.name)
                            break
                        time.sleep(10)
                    else:
                        pass
                time.sleep(.5)

        except Exception as e:
            print("There was an error: CITIZEN")
            traceback.print_exc()
            logging.error(traceback.format_exc())


class Plague_inc:
    def __init__(self, id, city):
        self.id = id
        self.city = city
        self.prompts_healthy = [f"Business as Usual in {self.city.name}", "New study shows that people who eat pizza every day are more immune to viruses", "Scientists discover a bacteria that eats plastic", f"Juice WRLD hologram performs at sold-out concert in {self.city.name}", "AI development accelerating at an alarming rate", "Summer 2023 hottest on record", "Giant mutant chickens wreak havoc on cities worldwide", f"World's largest banana cultivated in {self.city.name}", f"{self.city.name} vows to be car free by 2033", "Government issues warning after mysterious epidemic causes people to speak in pirate language", "Government advises citizens to stop licking doorknobs to prevent spread of virus", f"Cultural tensions on the rise in {self.city.name} "]
        self.prompts_low_concern = ["World's largest pillow fight cancelled","Odd disease spotted", "Epidemiologists concerned", "FOX news claims hoax, blames progressives", "Local governments consider lockdown", "Parents pull children out of schools", "New study shows that infection rates are highest among people who use Comic Sans", "Global toilet paper shortage as people panic-buy in response to new virus", "New Marvel movie to be a zombie film"]
        self.prompts_high_concern = ["Desperate civians eat pizza in hopes to boost immunity","Experts warn of impending doom as cute and cuddly zombies begin attacking humans", f"Schools in {self.city.name} close down", "Widespread chaos", "Shops looted", "Widespread power outages", "FOX news advocates for reopening of schools"]
        self.prompts_defeat = ["Few humans remain", f"Woman tries to marry zombie in {self.city.name}, becomes infected", "Government has ceased to function", "Zombies begin to starve", "FOX news blames Obama", f"Nuclear Reactor in {self.city.name} breaks down"]

    def prompts(self):
        try:
            while True:
                self.city.healthy_queue_lock.acquire()
                if len(self.city.healthy_queue) == 0:
                    print('News Outlets Run By Zombies')
                    self.city.healthy_queue_lock.release()
                    break
                self.city.healthy_queue_lock.release()
                self.city.zombie_queue_lock.acquire()
                if len(self.city.zombie_queue) < 5:
                    print("News: ")
                    self.city.zombie_queue_lock.release()
                    print(random.choice(self.prompts_healthy))
                    time.sleep(0.5)
                elif len(self.city.zombie_queue) < 50:
                    print("News: ")
                    self.city.zombie_queue_lock.release()
                    print(random.choice(self.prompts_low_concern))
                    time.sleep(0.5)
                elif len(self.city.zombie_queue) < 100:
                    print("News: ")
                    self.city.zombie_queue_lock.release()
                    print(random.choice(self.prompts_high_concern))
                    time.sleep(0.5)
                else:
                    print("News: ")
                    self.city.zombie_queue_lock.release()
                    print(random.choice(self.prompts_defeat))
                    time.sleep(0.5)
                time.sleep(5)
        except Exception:
            traceback.print_exc()


class Natural_disaster:
    def __init__(self, id, city):
        self.id = id
        self.city = city
        self.disaster = ['fire', 'flood', 'tornado', 'earthquake', 'epidemic']

    def disaster_function(self):
        try:
            while True:
                    chance = random.randint(1, 30)
                    if chance == 30:
                        choice_of_disaster = random.choice(self.disaster)
                        print("Disaster: ")
                        print("\nA", choice_of_disaster, f"has occured in {self.city.name}!")

                        self.city.healthy_queue_lock.acquire()
                        proportion = random.uniform(0, 0.15)
                        killed = round(len(self.city.healthy_queue) * proportion)
                        killed = random.sample(self.city.healthy_queue, killed)
                        self.city.healthy_queue_lock.release()
                        for died in killed:
                            self.city.healthy_queue_lock.acquire()
                            self.city.healthy_queue.remove(died)
                            self.city.healthy_queue_lock.release()
                            self.city.dead_queue_lock.acquire()
                            self.city.dead_queue.append(died)
                            self.city.dead_queue_lock.release()
                        print("\n", len(killed), "citizens died in ", f"{self.city.name}")

                        self.city.zombie_queue_lock.acquire()
                        proportion = random.uniform(0, 0.15)
                        killed = round(len(self.city.zombie_queue) * proportion)
                        killed = random.sample(self.city.zombie_queue, killed)
                        self.city.zombie_queue_lock.release()
                        for died in killed:
                            self.city.zombie_queue_lock.acquire()
                            self.city.zombie_queue.remove(died)
                            self.city.zombie_queue_lock.release()
                            self.city.dead_queue_lock.acquire()
                            self.city.dead_queue.append(died)
                            self.city.dead_queue_lock.release()
                        print("\n", len(killed), "zombies died in ", f"{self.city.name}")
                        time.sleep(10)
                    else:
                        time.sleep(10)
                        pass

        except Exception:
            print(Exception)
            traceback.print_exc()


class SQL:
    def __init__(self, city):
        self.city = city


    def record(self):
        while True:
            cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='ILOVEBOOBIES',
                database='ZombieSimulation'
            )

            cursor = cnx.cursor()
            query = "INSERT INTO statistics (Time, City_Name, Healthy, Zombies, Dead, Civil,  Military, Medics) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            self.city.healthy_queue_lock.acquire()
            self.city.zombie_queue_lock.acquire()
            self.city.dead_queue_lock.acquire()
            military = 0
            medics = 0
            civils = 0
            for healthy in self.city.healthy_queue:
                if healthy.job == 'Military':
                    military += 1
                elif healthy.job == 'Medic':
                    medics += 1
                else:
                    civils += 1

            values = (time.time(), self.city.name, len(self.city.healthy_queue), len(self.city.zombie_queue),
                      len(self.city.dead_queue), civils, military, medics)
            if len(self.city.healthy_queue) == 0:
                self.city.healthy_queue_lock.release()
                self.city.zombie_queue_lock.release()
                self.city.dead_queue_lock.release()
                break
            self.city.healthy_queue_lock.release()
            self.city.zombie_queue_lock.release()
            self.city.dead_queue_lock.release()
            cursor.execute(query, values)
            cnx.commit()

            self.city.healthy_queue_lock.acquire()
            if len(self.city.healthy_queue) == 0:
                self.city.healthy_queue_lock.release()
                break
            self.city.healthy_queue_lock.release()
            time.sleep(0.1)


# Creating the map / cities
MackersCity = City("Mackers City", random.randrange(500, 1001))
GulansTown = City("Gulans Town", random.randrange(20, 201))
NogalesVillage = City("Nogales Village", random.randrange(50, 451))
AlbonoHills = City("Albono Hills", random.randrange(250, 701))
ZeidelBorough = City("Zeidel Borough", random.randrange(400, 951))


#######################################################################
## MECHANICS ##

citizen_queue_init = []
citizen_id = 0
for i in range(1800):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])[0]
    citizen_queue_init.append(Citizen(citizen_id, city_prob))
    citizen_id = citizen_id + 1

military_queue_init = []
military_id = 0
for i in range(100):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])[0]
    mtype = random.choices(["Soldier", "Soldier Armoured", "Tank", "Plane"], [5, 4, 2, 1])[0]
    mrank = random.choices([1, 2, 3], [6, 3, 1])[0]
    military_queue_init.append(Military(military_id, mtype, mrank, city_prob))
    military_id = military_id + 1

medic_queue_init = []
medic_id = 0
for i in range(50):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])[0]
    medic_queue_init.append(Medic(medic_id, "Medic", city_prob))
    medic_id = medic_id + 1

news_queue_init = []
news_id = 0
for i in [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]:
    news_queue_init.append(Plague_inc(news_id, i))
    news_id = news_id + 1

sql_queue_init = []
for i in [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]:
    sql_queue_init.append(SQL(i))

natural_disaster_init = []
natural_id = 0
for i in [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]:
    natural_disaster_init.append(Natural_disaster(natural_id, i))
    natural_id = natural_id + 1

contamination_init = []
contamination_id = 0
for i in [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]:
    contamination_init.append(Contamination(contamination_id, i))
    natural_id = natural_id + 1


with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for medic in medic_queue_init:
        executor.submit(medic.zombie_cure)
        print(f"{medic.job, medic.id}, is now WORKING!")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor2:
        for personnel in military_queue_init:
            executor2.submit(personnel.zombie_destruction)
            print(f"{personnel.job, personnel.id}, is now WORKING!")

        with concurrent.futures.ThreadPoolExecutor(max_workers=1800) as executor3:
            for citizen in citizen_queue_init:
                print(f"{citizen.job, citizen.id}, is now WORKING!")
                executor3.submit(citizen.zombify)

            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor4:
                for news in news_queue_init:
                    print(f"{news.id} in, {news.city.name}, is now WORKING!")
                    executor4.submit(news.prompts)

                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor5:
                    for query in sql_queue_init:
                        print(f"{query.city.name} SQL records STARTED! ")
                        executor5.submit(query.record)

                    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor6:
                        for disaster in natural_disaster_init:
                            print(f"Disaster {disaster.id} in, {disaster.city.name}, is now WORKING!")
                            executor6.submit(disaster.disaster_function)

                        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor7:
                            for j in contamination_init:
                                print(f"Contamination function {j.id} in, {j.cities.name}, is now WORKING!")
                                executor7.submit(j.check_contamination)
