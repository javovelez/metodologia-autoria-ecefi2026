# Esquema de filtro completo: Eg + RG -- [4 cuadripolos en cascada] -- RL
# up/down=1.30 centra las cajas (sobresalen igual arriba y abajo).
V g0 v0; up=1.30, l=E_g
W v0 v1; right=0.3
RG v1 a_in; right=1.0, l=R_G
W g0 a_inb; right=1.3
TP1 b1t b1b a_in a_inb; right=1.3, fill=utnblue!8, l={\shortstack{Hemisec.\\adaptación\\$m{=}0{,}6$}}
TP2 b2t b2b b1t b1b; right=1.3, fill=utnblue!8, l=Prototipo
TP3 b3t b3b b2t b2b; right=1.3, fill=utnblue!8, l={\shortstack{Sección\\$m$-derivada}}
TP4 b4t b4b b3t b3b; right=1.3, fill=utnblue!8, l={\shortstack{Hemisec.\\adaptación\\$m{=}0{,}6$}}
W b4t r1; right=0.4
W b4b r1b; right=0.4
RL r1 r1b; down=1.30, l=R_L
