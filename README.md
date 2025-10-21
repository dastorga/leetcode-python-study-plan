# LeetCode Python - Plan de Estudio para Entrevistas

## 🎯 Objetivo

Este repositorio contiene un plan de estudio estructurado con 9 problemas clásicos de LeetCode, diseñado específicamente para preparar entrevistas técnicas en Python.

## 📁 Estructura del Proyecto

```
leetcode-python/
├── PLAN_DE_ESTUDIO.md          # Plan detallado con cronograma
├── README.md                   # Este archivo
├── utils.py                    # Utilidades y helpers
├── easy/                       # Problemas nivel Easy
│   ├── 001_two_sum.py
│   ├── 020_valid_parentheses.py
│   └── 021_merge_two_sorted_lists.py
├── medium/                     # Problemas nivel Medium
│   ├── 094_binary_tree_inorder_traversal.py
│   ├── 049_group_anagrams.py
│   ├── 053_maximum_subarray.py
│   └── 200_number_of_islands.py
└── hard/                       # Problemas nivel Hard
    ├── 023_merge_k_sorted_lists.py
    └── 042_trapping_rain_water.py
```

## 🚀 Cómo Usar Este Repositorio

### 1. Ejecutar un Problema Individual

```bash
# Navegar al directorio del problema
cd easy/
python 001_two_sum.py
```

### 2. Ejecutar Tests

Cada archivo incluye tests integrados. Simplemente ejecuta el archivo:

```bash
python easy/001_two_sum.py
```

### 3. Usar Utilidades

```python
from utils import timer, validate_solution, print_problem_header

# Decorador para medir tiempo
@timer
def my_solution():
    # Tu código aquí
    pass

# Validar solución
validate_solution(test_function, "Descripción del test")
```

## 📚 Lista de Problemas por Dificultad

### 🟢 Easy (3 problemas)

1. **Two Sum** - Hash Tables, Arrays
2. **Valid Parentheses** - Stack, String
3. **Merge Two Sorted Lists** - Linked Lists, Recursion

### 🟡 Medium (4 problemas)

4. **Binary Tree Inorder Traversal** - Trees, DFS, Stack
5. **Group Anagrams** - Hash Tables, Sorting
6. **Maximum Subarray** - Dynamic Programming, Kadane's Algorithm
7. **Number of Islands** - Graph, DFS/BFS

### 🔴 Hard (2 problemas)

8. **Merge k Sorted Lists** - Heap, Divide & Conquer
9. **Trapping Rain Water** - Two Pointers, DP, Stack

## 🎯 Conceptos Cubiertos

| Estructura de Datos | Algoritmos          | Técnicas         |
| ------------------- | ------------------- | ---------------- |
| Arrays              | Two Pointers        | Hash Tables      |
| Linked Lists        | DFS/BFS             | Recursión        |
| Stacks              | Dynamic Programming | Divide & Conquer |
| Binary Trees        | Sorting             | Greedy           |
| Graphs              | Graph Traversal     | Sliding Window   |
| Heaps               | Binary Search       | Backtracking     |

## 📅 Cronograma Sugerido

- **Semana 1**: Problemas Easy (1-3)
- **Semana 2**: Problemas Medium (4-7)
- **Semana 3**: Problemas Hard (8-9) + Repaso

## 💡 Metodología de Estudio

Para cada problema:

1. **📖 Análisis (10 min)**: Lee y entiende el problema
2. **🎯 Planificación (10 min)**: Diseña la solución en pseudocódigo
3. **⌨️ Implementación (20-30 min)**: Código en Python
4. **🧪 Testing (10 min)**: Prueba con casos edge
5. **⚡ Optimización (10-15 min)**: Mejora tiempo/espacio
6. **📝 Revisión (5-10 min)**: Documenta lecciones aprendidas

## 🛠️ Configuración del Entorno

### Requisitos

- Python 3.8+
- No se requieren librerías externas

### Instalación

```bash
git clone <tu-repo>
cd leetcode-python
```

## 📊 Seguimiento del Progreso

Marca tu progreso en `PLAN_DE_ESTUDIO.md`:

- [ ] Problema 1: Two Sum
- [ ] Problema 2: Valid Parentheses
- [ ] Problema 3: Merge Two Sorted Lists
- [ ] Problema 4: Binary Tree Inorder Traversal
- [ ] Problema 5: Group Anagrams
- [ ] Problema 6: Maximum Subarray
- [ ] Problema 7: Number of Islands
- [ ] Problema 8: Merge k Sorted Lists
- [ ] Problema 9: Trapping Rain Water

## 🎯 Tips para la Entrevista

1. **🗣️ Comunica tu proceso**: Explica tu razonamiento
2. **🔍 Maneja casos edge**: Considera inputs vacíos, nulos, etc.
3. **📊 Analiza complejidad**: Discute O(n) tiempo y espacio
4. **🔧 Optimiza iterativamente**: Comienza simple, luego mejora
5. **🎤 Practica en voz alta**: Simula condiciones reales

## 🔗 Enlaces Útiles

- [LeetCode](https://leetcode.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue.

---

**¡Buena suerte en tu entrevista! 🚀**
