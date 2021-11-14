"""
Módulo collections - Deque

Podemos dizer que deque é uma lista de alta performance.

"""
from collections import deque

# Criando deques
deq = deque('geek')
print(deq)

# Diferencial do deque para lista comum
deq.appendleft('y')  # -> Adiciona no inicio
print(deq)

# Remove e retorna o último elemento, deq.popleft exlui o primeiro
print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)
