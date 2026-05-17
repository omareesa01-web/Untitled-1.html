# سكربت بايثون لمحاكاة حركة الحراس الذكية في حصن المصمك
import random

def calculate_enemy_patrol(current_x, speed, level):
    # زيادة ذكاء الحارس وسرعته بناءً على المرحلة
    modifier = level * 1.5
    new_x = current_x + (speed * modifier)
    # إضافة حركة عشوائية طفيفة لجعل الحارس غير متوقع
    new_x += random.choice([-2, 0, 2])
    return new_x

print("=== Al-Masmak Python AI Helper Implemented ===")
