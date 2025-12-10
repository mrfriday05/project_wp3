import math


def fastener_geometry(type):
    if type == "M2":
        d = 2e-3
        p = 0.4e-3
        d_minor = 1.6e-3
        d_head = 5.0e-3

    elif type == "M3":
        d = 3e-3
        p = 0.5e-3
        d_minor = 2.5e-3
        d_head = 6.0e-3
    elif type == "M4":
        d = 4e-3
        p = 0.7e-3
        d_minor = 3.141e-3
        d_head = 7.0e-3
    elif type == "M5":
        d = 5e-3
        p = 0.8e-3
        d_minor = 4.134e-3
        d_head = 8.0e-3
    elif type == "M6":
        d = 6e-3
        p = 1.0e-3
        d_minor = 4.917e-3
        d_head = 10.0e-3
    elif type == "M8":
        d = 8e-3
        p = 1.25e-3
        d_minor = 6.466e-3
        d_head = 13.0e-3
    elif type == "M10":
        d = 10e-3
        p = 1.5e-3
        d_minor = 8.159e-3
        d_head = 16.0e-3
    elif type == "M12":
        d = 12e-3
        p = 1.75e-3
        d_minor = 9.853e-3
        d_head = 18.0e-3
    else:
        raise ValueError("Unsupported fastener type")

    # Areas
    A_nom = math.pi * (d**2) / 4
    A_minor = math.pi * (d_minor**2) / 4
    A_eff = math.pi * (d - 0.9382*p)**2 / 4  # Tensile stress area

    return d, A_nom, A_minor, A_eff, d_head

def material_properties(material):
    #print(material)
    if material == "Steel":     #D6AC
        E = 210e9               # Pa
        yield_stress = 1724e6    # Pa
        alpha = 1.2e-5          # 1/K
    elif material == "Aluminum":
        E = 71.7e9              # Pa
        yield_stress = 506e6    # Pa
        alpha = 2.3e-5          # 1/K
    elif material == "Titanium":
        E = 116e9               # Pa
        yield_stress = 880e6    # Pa
        alpha = 8.6e-6          # 1/K
    else:
        raise ValueError(f"Unsupported material type: {material}")
    
    return E, yield_stress, alpha