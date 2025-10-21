"""
Utilidades para el plan de estudio de LeetCode
Funciones helper comunes para testing y validación
"""

import time
from functools import wraps
from typing import Any, Callable

def timer(func: Callable) -> Callable:
    """Decorador para medir tiempo de ejecución de funciones"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # en milisegundos
        print(f"⏱️  {func.__name__} ejecutó en {execution_time:.2f} ms")
        return result
    return wrapper

def validate_solution(test_func: Callable, description: str = "") -> None:
    """Ejecuta y valida una función de test"""
    try:
        test_func()
        print(f"✅ {description or test_func.__name__} - Todos los tests pasaron")
    except Exception as e:
        print(f"❌ {description or test_func.__name__} - Error: {str(e)}")

def compare_solutions(*solutions: Callable) -> None:
    """Compara el rendimiento de múltiples soluciones"""
    print("\n🔄 Comparando rendimiento de soluciones:")
    print("-" * 50)
    
    for i, solution in enumerate(solutions, 1):
        solution_name = solution.__name__ if hasattr(solution, '__name__') else f"Solución {i}"
        print(f"{i}. {solution_name}")

class ComplexityAnalyzer:
    """Clase para analizar complejidad temporal y espacial"""
    
    @staticmethod
    def analyze_time_complexity(func: Callable, input_sizes: list, description: str = ""):
        """Analiza la complejidad temporal empíricamente"""
        print(f"\n📊 Análisis de complejidad temporal: {description}")
        print("Tamaño de entrada → Tiempo de ejecución")
        print("-" * 40)
        
        for size in input_sizes:
            # Aquí iría la lógica específica según el tipo de problema
            # Este es un ejemplo genérico
            start_time = time.time()
            # func(generate_test_input(size))  # Función específica del problema
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(f"n = {size:6d} → {execution_time:8.2f} ms")

def print_problem_header(problem_number: int, title: str, difficulty: str, link: str):
    """Imprime un header formateado para el problema"""
    print("=" * 60)
    print(f"🎯 LeetCode #{problem_number}: {title}")
    print(f"📊 Dificultad: {difficulty}")
    print(f"🔗 Link: {link}")
    print("=" * 60)

def print_approach_info(approach_name: str, time_complexity: str, space_complexity: str):
    """Imprime información de un approach específico"""
    print(f"\n🔍 {approach_name}")
    print(f"⏰ Tiempo: {time_complexity}")
    print(f"💾 Espacio: {space_complexity}")
    print("-" * 30)

# Constantes útiles
LEETCODE_BASE_URL = "https://leetcode.com/problems/"

# Mapeo de dificultades con emojis
DIFFICULTY_EMOJI = {
    "Easy": "🟢",
    "Medium": "🟡", 
    "Hard": "🔴"
}

def format_test_result(test_name: str, expected: Any, actual: Any, passed: bool):
    """Formatea el resultado de un test"""
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"{status} {test_name}")
    if not passed:
        print(f"   Expected: {expected}")
        print(f"   Actual:   {actual}")