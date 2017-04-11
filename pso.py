import sys
import numpy as np
import random
import copy

inertia = 0.729
cognitive_learning_factor = 1.49445
social_learning_factor = 1.49445

def sphere(x):
    return np.sum(x**2)

class Particle:

    def __init__(self,dim):
        self.current_position = np.array([random.uniform(-5.0,5.0) for _ in range(dim)])
        self.velocity = np.array([0.0 for _ in range(dim)])
        self.current_fitness = sys.float_info.max
        self.best_position = copy.copy(self.current_position)
        self.best_fitness = self.current_fitness

particles = [Particle(2) for _ in range(5)]

global_best_particle = particles[0]

for particle in particles:
    particle.current_fitness = sphere(particle.current_position)
    if particle.current_fitness < particle.best_fitness:
        particle.best_position = copy.copy(particle.current_position)
        particle.best_fitness = particle.current_fitness
    if particle.current_fitness < global_best_particle.best_fitness:
        global_best_particle = particle

iterations = 0
while(global_best_particle.current_fitness > 0.001):
    for particle in particles:
        r1, r2 = random.random(), random.random()
        particle.velocity = inertia * particle.velocity \
            + cognitive_learning_factor * r1 * (particle.best_position - particle.current_position) \
            + social_learning_factor * r2 * (global_best_particle.best_position - particle.current_position)
        particle.current_position = particle.current_position + particle.velocity

    for particle in particles:
        particle.current_fitness = sphere(particle.current_position)
        if particle.current_fitness < particle.best_fitness:
            particle.best_position = copy.copy(particle.current_position)
            particle.best_fitness = particle.current_fitness
        if particle.current_fitness < global_best_particle.best_fitness:
            global_best_particle = particle

    print("Iteration {0}, Fitness: {1}".format(iterations, global_best_particle.best_fitness))
    iterations +=1


print("Best particle found at position: {0}\nBest particle fitness: {1}"
      .format(global_best_particle.current_position,sphere(global_best_particle.current_position)))