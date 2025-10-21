#!/usr/bin/env python3
"""
Script para trackear el progreso del plan de estudio de LeetCode
Ejecuta: python progress_tracker.py
"""

import os
import re
from datetime import datetime
from typing import Dict, List, Tuple

class ProgressTracker:
    def __init__(self, base_path: str = "."):
        self.base_path = base_path
        self.problems = [
            ("Easy", "001_two_sum.py", "Two Sum"),
            ("Easy", "020_valid_parentheses.py", "Valid Parentheses"),
            ("Easy", "021_merge_two_sorted_lists.py", "Merge Two Sorted Lists"),
            ("Medium", "094_binary_tree_inorder_traversal.py", "Binary Tree Inorder Traversal"),
            ("Medium", "049_group_anagrams.py", "Group Anagrams"),
            ("Medium", "053_maximum_subarray.py", "Maximum Subarray"),
            ("Medium", "200_number_of_islands.py", "Number of Islands"),
            ("Hard", "023_merge_k_sorted_lists.py", "Merge k Sorted Lists"),
            ("Hard", "042_trapping_rain_water.py", "Trapping Rain Water"),
        ]
    
    def check_implementation_status(self, file_path: str) -> str:
        """Verifica si un problema está implementado o solo tiene TODO"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Contar TODOs vs implementaciones reales
            todo_count = len(re.findall(r'# TODO:', content))
            
            # Buscar patrones que indiquen implementación real
            implementation_patterns = [
                r'return\s+\w+',  # return statements
                r'for\s+\w+\s+in',  # for loops
                r'while\s+\w+',  # while loops
                r'if\s+\w+',  # if statements (básicos)
            ]
            
            implementation_count = sum(
                len(re.findall(pattern, content)) 
                for pattern in implementation_patterns
            )
            
            if todo_count > 2 and implementation_count < 3:
                return "🔴 No implementado"
            elif todo_count > 0 and implementation_count >= 3:
                return "🟡 Parcialmente implementado"
            elif todo_count == 0 and implementation_count >= 3:
                return "🟢 Implementado"
            else:
                return "🔵 Estado desconocido"
                
        except FileNotFoundError:
            return "❌ Archivo no encontrado"
        except Exception as e:
            return f"⚠️ Error: {str(e)}"
    
    def generate_progress_report(self) -> str:
        """Genera un reporte de progreso completo"""
        report = []
        report.append("📊 REPORTE DE PROGRESO - LEETCODE PYTHON")
        report.append("=" * 60)
        report.append(f"📅 Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        report.append("")
        
        # Estadísticas por dificultad
        difficulty_stats = {"Easy": [], "Medium": [], "Hard": []}
        
        for difficulty, filename, title in self.problems:
            file_path = os.path.join(
                self.base_path, 
                difficulty.lower(), 
                filename
            )
            status = self.check_implementation_status(file_path)
            difficulty_stats[difficulty].append((title, status))
        
        # Mostrar progreso por dificultad
        for difficulty, problems in difficulty_stats.items():
            emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}[difficulty]
            report.append(f"{emoji} {difficulty.upper()} ({len(problems)} problemas)")
            report.append("-" * 40)
            
            for i, (title, status) in enumerate(problems, 1):
                report.append(f"{i}. {title:<35} {status}")
            
            report.append("")
        
        # Estadísticas generales
        all_statuses = [status for _, problems in difficulty_stats.items() 
                       for _, status in problems]
        
        completed = sum(1 for status in all_statuses if "🟢" in status)
        partial = sum(1 for status in all_statuses if "🟡" in status)
        not_started = sum(1 for status in all_statuses if "🔴" in status)
        total = len(all_statuses)
        
        report.append("📈 ESTADÍSTICAS GENERALES")
        report.append("-" * 30)
        report.append(f"✅ Completados: {completed}/{total} ({completed/total*100:.1f}%)")
        report.append(f"🔄 En progreso: {partial}/{total} ({partial/total*100:.1f}%)")
        report.append(f"⏳ Sin empezar: {not_started}/{total} ({not_started/total*100:.1f}%)")
        report.append("")
        
        # Progreso visual
        progress_bar = self.create_progress_bar(completed, total)
        report.append(f"🎯 Progreso total: {progress_bar}")
        report.append("")
        
        # Próximos pasos recomendados
        report.append("🎯 PRÓXIMOS PASOS RECOMENDADOS")
        report.append("-" * 35)
        
        if not_started > 0:
            # Encontrar el primer problema sin implementar
            for difficulty, problems in difficulty_stats.items():
                for title, status in problems:
                    if "🔴" in status:
                        report.append(f"1. Comenzar con: {title} ({difficulty})")
                        break
                else:
                    continue
                break
        
        if partial > 0:
            report.append("2. Completar problemas parcialmente implementados")
        
        if completed > 0:
            report.append("3. Revisar y optimizar soluciones completadas")
        
        return "\n".join(report)
    
    def create_progress_bar(self, completed: int, total: int, length: int = 20) -> str:
        """Crea una barra de progreso visual"""
        if total == 0:
            return "No hay problemas"
        
        progress = completed / total
        filled_length = int(length * progress)
        
        bar = "█" * filled_length + "░" * (length - filled_length)
        percentage = progress * 100
        
        return f"{bar} {percentage:.1f}% ({completed}/{total})"
    
    def run_quick_check(self):
        """Ejecuta un chequeo rápido y muestra estadísticas básicas"""
        print("🔍 Ejecutando chequeo rápido...")
        print()
        
        completed = 0
        total = len(self.problems)
        
        for difficulty, filename, title in self.problems:
            file_path = os.path.join(self.base_path, difficulty.lower(), filename)
            status = self.check_implementation_status(file_path)
            
            if "🟢" in status:
                completed += 1
            
            emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}[difficulty]
            print(f"{emoji} {title:<35} {status}")
        
        print()
        progress_bar = self.create_progress_bar(completed, total)
        print(f"📊 Progreso: {progress_bar}")

def main():
    tracker = ProgressTracker()
    
    print("LeetCode Python - Progress Tracker")
    print("1. Reporte completo")
    print("2. Chequeo rápido")
    print()
    
    choice = input("Selecciona una opción (1-2): ").strip()
    
    if choice == "1":
        report = tracker.generate_progress_report()
        print("\n" + report)
        
        # Guardar reporte en archivo
        with open("progress_report.txt", "w", encoding="utf-8") as f:
            f.write(report)
        print("\n📝 Reporte guardado en 'progress_report.txt'")
        
    elif choice == "2":
        tracker.run_quick_check()
    else:
        print("❌ Opción no válida")

if __name__ == "__main__":
    main()