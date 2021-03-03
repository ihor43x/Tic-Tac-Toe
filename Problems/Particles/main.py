particles = {"1/2": {"-1/3": "Strange Quark",
                     "2/3": "Charm Quark",
                     "-1": "Electron Lepton",
                     "0": "Neutrino Lepton"},
             "1": {"0": "Photon Boson"}}
try:
    print(particles[input()][input()])
except KeyError:
    print("Incorrect input")
