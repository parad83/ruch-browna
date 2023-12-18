import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Particle():
    def __init__(self, loc=0.0, scale=1.0):
        self.normal = (loc, scale)
        self.x = np.random.normal(*self.normal)
        self.y = np.random.normal(*self.normal)
        self.z = np.random.normal(*self.normal)
        self.distance = 0

    def move(self):
        self.x += np.random.normal(*self.normal)
        self.y += np.random.normal(*self.normal)
        self.z += np.random.normal(*self.normal)
        self.calculate_distance()

    def calculate_distance(self):
        self.distance += np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def get_distance(self):
        return self.distance

    def get_position(self):
        return self.x, self.y, self.z


class Simulation():
    def __init__(self, object):
        self.object = object

    def run(self, steps):
        self.steps = steps

        self.xs = np.zeros(steps)
        self.ys = np.zeros(steps)
        self.zs = np.zeros(steps)
        self.distances = np.zeros(steps)

        for i in range(steps):
            self.xs[i], self.ys[i], self.zs[i] = self.object.get_position()
            self.distances[i] = self.object.get_distance()
            self.object.move()

    def plot_trajectory(self):
        ax = plt.figure().add_subplot(projection='3d')

        ax.plot(self.xs, self.ys, self.zs, 'k-',
                linewidth=0.5, label='trajektoria ruchu cząstki')

        # ax.plot([self.xs[0], self.xs[-1]], [self.ys[0], self.ys[-1]],
        # [self.zs[0], self.zs[-1]], 'ro', label='poczatek i koniec')

        ax.plot(self.xs[0], self.ys[0], self.zs[0],
                'ro', label='pozycja cząstki dla t=0', markersize=4)
        ax.plot(self.xs[-1], self.ys[-1], self.zs[-1],
                'go', label=f'pozycja cząstki dla t={self.steps}', markersize=4)

        ax.set_xlabel('oś x')
        ax.set_ylabel('oś y')
        ax.set_zlabel('oś z')

        ax.legend()
        ax.set_title('Ruch Browna')

        ax.text(0, 0, 0, f'odległość przebyta przez cząstkę: {self.object.get_distance().round(2)}', horizontalalignment='left',
                verticalalignment='bottom', transform=ax.transAxes)

        plt.show()

    def animate_trajectory(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        line, = ax.plot([], [], [], 'k-', lw=0.5,
                        label='trajektoria ruchu cząstki')

        point, = ax.plot([], [], [], 'go', markersize=5)

        distance = ax.text(0, 0, 0, '', transform=ax.transAxes)

        ax.plot(self.xs[0], self.ys[0], self.zs[0],
                'ro', label='pozycja cząstki dla t=0', markersize=5)

        def init():
            line.set_data([], [])
            line.set_3d_properties([])

            point.set_data([], [])
            point.set_3d_properties([])
            point.set_label('')

            distance.set_text('')

            return line, point, distance

        def update(i):
            line.set_data(self.xs[:i], self.ys[:i])
            line.set_3d_properties(self.zs[:i])

            point.set_data(self.xs[i], self.ys[i])
            point.set_3d_properties(self.zs[i])
            point.set_label(f'pozycja cząstki w t={i}')

            distance.set_text(
                f'odległość przebyta przez cząstkę: {self.distances[i].round(2)}')

            return line, point, distance

        ax.set_xlabel('oś x')
        ax.set_ylabel('oś y')
        ax.set_zlabel('oś z')

        ax.set_title('Ruch Browna')
        ax.legend()

        ax.set_xlim3d([min(self.xs), max(self.xs)])
        ax.set_ylim3d([min(self.ys), max(self.ys)])
        ax.set_zlim3d([min(self.zs), max(self.zs)])

        ani = animation.FuncAnimation(
            fig=fig, init_func=init, func=update, blit=True, frames=self.steps, interval=10, repeat=False)

        plt.show()
