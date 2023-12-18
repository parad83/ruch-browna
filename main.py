from Brown import Particle, Simulation

p = Particle()
s = Simulation(p)
s.run(1000)
s.animate_trajectory()
s.plot_trajectory()
