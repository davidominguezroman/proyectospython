import math
import numpy as np
import matplotlib.pyplot as plt

G = -9.81
N = 1000

print("This is a program to calculate the parabolic trayectory of a projectile\n")
print("You will be asked to provide some initial values to calculate the trajectory\n")
print("Let's begin.................................................................\n")

mass = float(input("Enter the mass of the projectile (kg): "))

if mass <= 0:
    print("Mass must be a positive number")
    exit()

v0 = float(input("Enter the initial velocity (m/s): "))
angle_deg = float(input("Enter the launch angle (degrees): "))
x0 = float(input("Enter the initial horizontal position (m): "))
y0 = float(input("Enter the initial vertical position (m): "))

angle_rad = angle_deg * math.pi / 180 #changes degrees to radians
print(str(angle_rad))
discriminant = math.pow(v0 *math.sin(angle_rad), 2) - 2 * G * y0 #calculates the discriminant to see if it touches the ground

if discriminant < 0:
    print("The projectile will not reach the ground with the given parameters.")
    exit()

t_flight = 2 * v0 * math.sin(angle_rad)/ -G #calculates the flight time
print(str(t_flight))
tmax = v0 * math.sin(angle_rad) / -G #calculates time when it reaches maximun altitud
xmax = x0 + v0 * math.cos(angle_rad) * tmax # horizontal position for tmax
ymax = y0 + v0 * math.sin(angle_rad) * tmax # maximum vertical position
max_distance = x0 + v0 * math.cos(angle_rad) * t_flight #calculates maximun horizontal distance
time = []
posx = []
posy = []

for i in range(N):
    t = t_flight * i / (N-1)
    time.append(round(t, 2))
    x = x0 + v0 * math.cos(angle_rad) * t
    y = y0 + v0 * math.cos(angle_rad) * t + 0.5 * G * math.pow(t, 2)
    posx.append(round(x, 2))
    posy.append(round(y, 2))

#for i in range(N):
#    print("Position at t = " + str(time[i]) + "s: x = " + str(posx[i]) + " m, y = " + str(posy[i]) + " m")

fig, ax = plt.subplots()
ax.plot(posx, posy)
plt.savefig('XvsY.png')


