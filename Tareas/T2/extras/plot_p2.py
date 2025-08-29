import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Computer Modern"],
        "font.size": 12,
    }
)

F_o = 0.5
Omg = 3
cte = F_o / (2 * Omg)


def x(t):
    return cte * t * np.sin(Omg * t)


t = np.linspace(0, 2 * np.pi, 1000)

fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(t, x(t), color="#50FA7B")
ax.set_xlabel("$t$  [s]")
ax.set_ylabel("$x(t)$  [s]")
ax.set_title(r"Gráfica $x(t) = \frac{F_{0}}{2\Omega^{2}} t \sin(\Omega t)$", pad=20)

fig.savefig("forced-oscillator.pdf", dpi=300, transparent=True)
plt.show()
