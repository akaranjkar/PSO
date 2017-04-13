import sys
import numpy as np
import random
import copy
import cProfile

inertia = 0.729
cognitive_learning_factor = 1.49445
social_learning_factor = 1.49445

def sphere(x):
    return np.sum(x**2)

class Particle:

    def __init__(self,dim):
        self.current_position = np.array([random.uniform(-5.0,5.0) for _ in range(dim)])
        self.velocity = np.array([0.0 for _ in range(dim)])
        self.current_error = sys.float_info.max
        self.best_position = copy.copy(self.current_position)
        self.least_error = self.current_error

particles = [Particle(2) for _ in range(10)]

global_best_particle = particles[0]

for particle in particles:
    particle.current_error = sphere(particle.current_position)
    if particle.current_error < particle.least_error:
        particle.best_position = copy.copy(particle.current_position)
        particle.least_error = particle.current_error
    if particle.current_error < global_best_particle.least_error:
        global_best_particle = particle


iterations = 0
while(global_best_particle.current_error > 0.0001):
    pr = cProfile.Profile()
    pr.enable()

    for particle in particles:
        r1, r2 = random.random(), random.random()
        particle.velocity = inertia * particle.velocity \
            + cognitive_learning_factor * r1 * (particle.best_position - particle.current_position) \
            + social_learning_factor * r2 * (global_best_particle.best_position - particle.current_position)
        particle.current_position = np.clip(particle.current_position + particle.velocity, -5.0,5.0)

    for particle in particles:
        particle.current_error = sphere(particle.current_position)
        if particle.current_error < particle.least_error:
            particle.best_position = copy.copy(particle.current_position)
            particle.least_error = particle.current_error
        if particle.current_error < global_best_particle.least_error:
            global_best_particle = particle

    print("Iteration {0}, Least error: {1}".format(iterations, global_best_particle.least_error))
    iterations +=1

    pr.disable()
    pr.print_stats(sort='time')

print("Best particle found at position: {0}\nLeast error: {1}"
      .format(global_best_particle.current_position,global_best_particle.least_error))