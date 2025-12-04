# models/health_model.py
import numpy as np

# 假設的一些健康建議資料
diet_recommendations = {
    "減脂": {
        "meal_plan": "減少碳水化合物的攝取，增加蛋白質和蔬菜的比例。",
        "calories_per_day": 1500
    },
    "增肌": {
        "meal_plan": "增加蛋白質的攝取，並搭配適量碳水化合物和健康脂肪。",
        "calories_per_day": 2500
    },
    "維持體重": {
        "meal_plan": "保持平衡的飲食，搭配足夠的運動。",
        "calories_per_day": 2000
    }
}

exercise_recommendations = {
    "減脂": "有氧運動（如跑步、騎自行車）每周至少 4 次，每次 30 分鐘。",
    "增肌": "力量訓練每周至少 3 次，重點訓練大肌群。",
    "維持體重": "每周運動 3 次，混合有氧與力量訓練。",
}

# 假設的BMI計算邏輯
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# 健康分析函數
def analyze_health(user_data):
    # 基本健康分析
    bmi = calculate_bmi(user_data["weight"], user_data["height"])
    
    # 判斷健康目標並生成建議
    target = user_data["target"]
    diet = diet_recommendations.get(target, {})
    exercise = exercise_recommendations.get(target, "")
    
    # BMI 評估
    if bmi < 18.5:
        bmi_status = "體重過輕"
    elif 18.5 <= bmi < 24.9:
        bmi_status = "正常體重"
    elif 25 <= bmi < 29.9:
        bmi_status = "過重"
    else:
        bmi_status = "肥胖"
    
    return {
        "bmi": bmi,
        "bmi_status": bmi_status,
        "diet_advice": diet.get("meal_plan", "未提供飲食建議"),
        "calories_needed": diet.get("calories_per_day", 2000),
        "exercise_advice": exercise
    }
