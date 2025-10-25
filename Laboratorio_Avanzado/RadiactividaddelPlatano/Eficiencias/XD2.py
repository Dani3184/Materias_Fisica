import numpy as np

def eps_geom_point_offaxis(Rd, rho, z, Nphi=2000):
    phis = np.linspace(0, 2*np.pi, Nphi, endpoint=False)
    denom = np.sqrt(z*z + Rd*Rd + rho*rho - 2*Rd*rho*np.cos(phis))
    integrand = 1.0 - z/denom
    Omega = 0.5 * np.sum(integrand) * (2*np.pi / Nphi)  # nota: integral de 0..2pi de (1 - z/denom)
    # Omega en la expresión anterior es  the 2*pi*... form; aquí hemos integrado el término que da 2*(1-...)?
    # Para consistencia usar: Omega = np.sum(2*pi*(1 - z/denom))*dphi / ???. 
    # Simpler: compute Omega directly:
    dphi = 2*np.pi / Nphi
    Omega = np.sum(2*np.pi * (1 - z/denom)) * (dphi / (2*np.pi))  # reduces to np.sum(1 - z/denom)*dphi
    # So final:
    Omega = np.sum(1 - z/denom) * dphi
    eps = Omega / (4*np.pi)
    return eps

# Ejemplo:
Rd = 6.5   # cm (detector radio)
rho = 1.0  # cm (desplazamiento radial de la fuente)
z = 25.0   # cm (altura sobre el plano del detector)
print(eps_geom_point_offaxis(Rd, rho, z))
