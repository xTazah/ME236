import matplotlib.pyplot as plt
import numpy as np


#define given constants:
C_Dp = 0.0356
p = 1.225
AR = 8.75
S = 0.69
m = 5.3
g = 9.81
W = m * g


def calc_C_L(velocity, lift, density, surface_area):
    return (lift * 2) / (density * velocity**2 * surface_area)

def calc_C_Di(C_L, aspect_ratio):
    return C_L**2/(np.pi * aspect_ratio)

def calc_P_D(density, velocity, C_D, surface_area):
    return 1/2 * density * velocity**3 * C_D * surface_area

if __name__ == "__main__":
    velocities = np.linspace(3, 30, 300)

    F_Dps, F_Dis, F_Ds, P_Ds = [], [], [], []

    for v in velocities:
        q_S = 0.5 * p * v**2 * S          # dynamic pressure times area
        C_L = calc_C_L(velocity=v, lift=W, density=p, surface_area=S)
        C_Di = calc_C_Di(C_L, AR)

        F_Dps.append(q_S * C_Dp)
        F_Dis.append(q_S * C_Di)
        F_Ds.append(q_S * (C_Dp + C_Di))

        P_Ds.append(calc_P_D(p, v, C_Dp + C_Di, S))

    plt.figure()
    plt.plot(velocities, F_Dis, label="Induced drag")
    plt.plot(velocities, F_Dps, label="Parasite drag")
    plt.plot(velocities, F_Ds, label="Total drag")

    plt.xlabel("Airspeed $v_\\infty$ [m/s]")
    plt.ylabel("Drag force [N]")
    plt.title("Drag force vs. airspeed")
    plt.legend()
    plt.grid(True)


    plt.figure()
    plt.plot(velocities, P_Ds, label="Drag power")

    plt.xlabel("Airspeed $v_\\infty$ [m/s]")
    plt.ylabel("Drag power [W]")
    plt.title("Drag power vs. airspeed")
    plt.legend()
    plt.grid(True)


    plt.show()