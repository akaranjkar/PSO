import sys
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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

particles = [Particle(2) for _ in range(10)]

global_best_particle = particles[0]

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x1 = np.arange(-5,5,0.5)
x2 = np.arange(-5,5,0.5)
x1,x2 = np.meshgrid(x1,x2)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(0,50)
y = (x1**2) + (x2**2)

for particle in particles:
    particle.current_fitness = sphere(particle.current_position)
    if particle.current_fitness < particle.best_fitness:
        particle.best_position = copy.copy(particle.current_position)
        particle.best_fitness = particle.current_fitness
    if particle.current_fitness < global_best_particle.best_fitness:
        global_best_particle = particle

iterations = 0
while(global_best_particle.current_fitness > 0.0001):
    for particle in particles:
        r1, r2 = random.random(), random.random()
        particle.velocity = inertia * particle.velocity \
            + cognitive_learning_factor * r1 * (particle.best_position - particle.current_position) \
            + social_learning_factor * r2 * (global_best_particle.best_position - particle.current_position)
        particle.current_position = np.clip(particle.current_position + particle.velocity, -5.0,5.0)

    # ax.plot_surface(x1, x2, y, rstride=1, cstride=1, cmap='BuGn')
    ax.plot_wireframe(x1, x2, y, rstride=1, cstride=1)


    for particle in particles:
        particle.current_fitness = sphere(particle.current_position)
        if particle.current_fitness < particle.best_fitness:
            particle.best_position = copy.copy(particle.current_position)
            particle.best_fitness = particle.current_fitness
        if particle.current_fitness < global_best_particle.best_fitness:
            global_best_particle = particle
        ax.scatter(particle.current_position[0],particle.current_position[1],particle.current_fitness,s=32)

    plt.pause(.0001)
    plt.cla()

    print("Iteration {0}, Fitness: {1}".format(iterations, global_best_particle.best_fitness))
    iterations +=1


print("Best particle found at position: {0}\nBest particle fitness: {1}"
      .format(global_best_particle.current_position,sphere(global_best_particle.current_position)))