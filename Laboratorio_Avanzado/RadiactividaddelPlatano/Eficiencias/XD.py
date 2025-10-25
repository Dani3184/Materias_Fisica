import numpy as np

# Parámetros (modifica con tus valores)
Rd = 6.5        # radio detector [cm]
Rs = 4.8        # radio muestra [cm]
d_top = 7.0     # distancia desde detector hasta superficie superior de la muestra [cm]
h = 1.8         # altura/espesor de la muestra [cm]

# Discretización (ajusta para convergencia / velocidad)
Nz = 40
Nr = 200
Nphi = 400

zs = np.linspace(d_top, d_top + h, Nz)
rs = np.linspace(0, Rs, Nr)
phis = np.linspace(0, 2*np.pi, Nphi, endpoint=False)

# Pesos en r para integración (usamos trapecio en r, pero incluimos el factor r en integrando)
dr = Rs/(Nr-1)
dz = h/(Nz-1)
dphi = 2*np.pi/Nphi

integral = 0.0
for z in zs:
    for r in rs:
        # calcular inner integral en phi
        denom = np.sqrt(z*z + Rd*Rd + r*r - 2*Rd*r*np.cos(phis))
        integrand_phi = 1.0 - z/denom  # corresponde al (1 - z/sqrt(...))
        Iphi = np.sum(integrand_phi) * dphi  # aproximación trapecio uniforme
        # el elemento de volumen contribuye: r * Iphi
        integral += r * Iphi * dr * dz

# prefactor
eps_geom = integral / (2.0 * np.pi * Rs*Rs * h)
print("Eficiencia geométrica (numérica) =", eps_geom, "->", eps_geom*100, "%")
