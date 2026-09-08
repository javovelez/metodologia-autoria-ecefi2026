# Referencia de Secciones del Capítulo 2 para TP1

## EJERCICIO 9 → sec24: Funciones de Variable Compleja
- f(z) = u(x,y) + jv(x,y) separando Re e Im de z=x+jy
- |f(z)| = √(u²+v²), Arg{f(z)} = arctan(v/u)
- Para e^z: |e^z|=e^x, Arg{e^z}=y
- Para polinomios: factorizar → |f|=K·∏|z-zᵢ|, Arg{f}=∑Arg{z-zᵢ}

## EJERCICIO 10 → sec25: Analiticidad y Cauchy-Riemann
- CR cartesianas: ∂u/∂x = ∂v/∂y  Y  ∂u/∂y = -∂v/∂x
- Si se cumplen y las parciales son continuas → f es analítica
- f(z)=z̄ NO analítica (viola CR en todo punto)
- f(z)=Re{z}=x NO analítica (∂u/∂x=1 ≠ ∂v/∂y=0)
- f(z)=z² SI analítica (CR se cumplen en todo C)
- f(z)=e^z SI analítica (e^x·cos y, e^x·sin y satisfacen CR)

## EJERCICIO 11 → sec26: Funciones Racionales - Módulo y Fase
- H(z) = K·∏(z-zᵢ)/∏(z-pⱼ) — forma factorizada
- |H(z)| = |K|·∏|z-zᵢ|/∏|z-pⱼ|  (producto de distancias)
- ∠H(z) = ∠K + ∑∠(z-zᵢ) - ∑∠(z-pⱼ)  (suma de ángulos)
- Evaluación en z=jy (eje Im): sustituir x=0 y∈ℝ
- Evaluación en z=e^{jθ} (círculo unitario): |z|=1

## EJERCICIO 12-13 → sec27: Integración y Fórmula de Cauchy
- ∮_C f(z)dz = 0 si f analítica en dominio simplemente conexo
- Fórmula de Cauchy: f(z₀) = (1/j2π)∮_C f(z)/(z-z₀)dz
- Derivadas: f^(n)(z₀) = n!/(j2π) ∮_C f(z)/(z-z₀)^(n+1)dz
- Polo simple: ∮_C b/(z-z₀)dz = j2πb
- Polo de orden m≥2: ∮_C b/(z-z₀)^m dz = 0

## EJERCICIO 14 → sec29: Cálculo de Residuos
- Polo simple: Res(f,p) = lim_{z→p}[(z-p)·f(z)]
- Polo orden m: Res(f,p) = 1/(m-1)! · lim_{z→p} d^{m-1}/dz^{m-1}[(z-p)^m·f(z)]
- Para f(z)=g(z)/h(z) polo simple en h(p)=0: Res = g(p)/h'(p)
- Residuo = coeficiente b₁ en la serie de Laurent

