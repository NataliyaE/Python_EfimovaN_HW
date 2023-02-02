# дана функция f(x) = sin(x)**2 - cos(x)**2  
# 1. + определить корни
# 2. + найти интервалы, на которых функция возрастает
# 3. + найти интервалы, на которых функция убывает
# 4. + построить график
# 5. + вычислить вершину
# 6. + определить промежутки, на котором F > 0
# 7. + определить промежутки, на котором F < 0

# 
#  - найти х, при которых f(x) = 0 (solve - в sympy)
# для домашки: численное решение сцыпай scipy библеотека (для второго задания)
# (домашка, син и кос - импортировать из sympy)

# 4. построить график
from sympy.plotting import plot
from sympy import Symbol, solve, diff, evalf, solveset, S, pprint, sin, cos
x = Symbol('x')
f = sin(x)**2 - cos(x)**2
plot(f)
print()

# 1. определить корни
ans = solve(f, x)
print(ans)
for i in ans:
    print(i.evalf())
print()

# 6. определить промежутки, на котором F > 0
# 7. определить промежутки, на котором F < 0
pprint(solveset(f > 0, x, domain=S.Reals), use_unicode=True) # или solve(f > 0, x)
pprint(solveset(f < 0, x, domain=S.Reals), use_unicode=True) # или solve(f < 0, x)
print()

# 5. вычислить вершину
diff_f = diff(f, x) # поиск производной
print(diff_f)
print(solve(diff_f, x))
print()

# 2. найти интервалы, на которых функция возрастает (решить неравентсва, где производная больше или меньше 0)
# 3. найти интервалы, на которых функция убывает
pprint(solveset(diff_f > 0, x, domain=S.Reals), use_unicode=True)
pprint(solveset(diff_f < 0, x, domain=S.Reals), use_unicode=True)
