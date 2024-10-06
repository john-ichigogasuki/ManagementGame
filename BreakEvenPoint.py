import sys, math
import matplotlib.pyplot as plt

while True:
    try:
        term = int(input("今何期ですか？: "))
        if 1 <= term <= 5:
            break
    except ValueError:
        print("1から5までの数字を入力してください")

while True:
    try:
        table_rule = int(input("「ジュニア卓: 0, シニア卓: 1」 を入力: "))
        if table_rule == 0 or table_rule == 1:
            break
    except ValueError:
        print(f"0または1を入力してください")

if 3 <= term <= 5:
    while True:
        try:
            dice_result = int(input("サイコロの結果を入力: "))
            if 1 <= dice_result <= 6:
                break
            else:
                print(f"1から6までの数字を入力してください")
        except ValueError:
            print("有効な数字を入力")

# 給料計算
employee_now = int(input("現在の従業員数を入力: "))
employee_max = int(input("期中最大人数を入力: "))
machine  = int(input("機械個数を入力: "))

def costs_calculation(employee_now, employee_max, machine, employee_cost, machine_cost, employee_benefit_cost):
    costs = employee_now*employee_cost + machine*machine_cost + employee_max*employee_benefit_cost
    return costs

def dice_result_calculation(dice_result, employee_cost, machine_cost, employee_benefit_cost):
    if dice_result in [1, 2, 3]:
        employee_cost = employee_cost*1.1
        machine_cost = machine_cost*1.1
        employee_benefit_cost = employee_benefit_cost*1.1
        
    elif dice_result in [4, 5, 6]:
        employee_cost = employee_cost*1.2
        machine_cost = machine_cost*1.2
        employee_benefit_cost = employee_benefit_cost*1.2
    
    return round(employee_cost), round(machine_cost), round(employee_benefit_cost)

# 2期の際の給料計算
def personnelAndMachineCosts(term, employee_now, employee_max, machine):
    personnel_cost = 0
    if term == 2:
        employee_cost = int(22)
        machine_cost = int(22)
        employee_benefit_cost = int(11)
        personnel_cost = costs_calculation(employee_now, employee_max, machine, employee_cost, machine_cost, employee_benefit_cost)

    # 3期以降の給料計算
    if term == 3:
        employee_cost = int(24)
        machine_cost = int(24)
        employee_benefit_cost = int(12)
        if table_rule == 1:
            employee_cost, machine_cost, employee_benefit_cost = dice_result_calculation(dice_result, employee_cost, machine_cost, employee_benefit_cost)
        personnel_cost = costs_calculation(employee_now, employee_max, machine, employee_cost, machine_cost, employee_benefit_cost)

    if term == 4:
        employee_cost = int(26)
        machine_cost = int(26)
        employee_benefit_cost = int(13)
        if table_rule == 1:
            employee_cost, machine_cost, employee_benefit_cost = dice_result_calculation(dice_result, employee_cost, machine_cost, employee_benefit_cost)
        personnel_cost = costs_calculation(employee_now, employee_max, machine, employee_cost, machine_cost, employee_benefit_cost)

    if term == 5:
        employee_cost = int(28)
        machine_cost = int(28)
        employee_benefit_cost = int(14)
        if table_rule == 1:
            employee_cost, machine_cost, employee_benefit_cost = dice_result_calculation(dice_result, employee_cost, machine_cost, employee_benefit_cost)
        personnel_cost = costs_calculation(employee_now, employee_max, machine, employee_cost, machine_cost, employee_benefit_cost)
    return personnel_cost

# チップによる固定費計算
def getChipCounts(color):
    while True:
        try:
            chip_count = int(input(f"今期使用「{color}」チップ個数を入力: "))
            if chip_count != "":
                break
        except ValueError:
            print("数値を入力してください")
    return chip_count

while True:
    try:
        red_button = int(input("今期使用「赤」チップ個数を入力: "))
        if red_button != "":
            break
    except ValueError:
        print("数値を入力してください")

while True:
    try:
        blue_button = int(input("今期使用「青」チップ個数を入力: "))
        if blue_button != "":
            break
    except ValueError:
        print("数値を入力してください")


while True:
    try:
        yellow_button = int(input("今期使用「黄」チップ個数を入力: "))
        if yellow_button != "":
            break
    except ValueError:
        print("数値を入力してください")

while True:
    try:
        green_button = int(input("今期使用「緑」チップ個数を入力: "))
        if green_button != "":
            break
    except ValueError:
        print("数値を入力してください")

while True:
    try:
        orange_button = int(input("今期使用「オレンジ」チップ個数を入力: "))
        if orange_button != "":
            break
    except ValueError:
        print("数値を入力してください")

def SeniorStrategyCostsCalculation(red_button, blue_button, yellow_button, green_button, orange_button): #シニア卓ルールの時のみに呼び出す
    total_red_costs, total_blue_costs, total_yellow_costs = 0,0,0
    if red_button != 0:
        express = int(input("「赤チップ」特急個数を入力: "))
        if express != 0:
            red_express_costs = express*40
            red_ready_costs = (red_button - express) * 20
            total_red_costs = red_express_costs + red_ready_costs
        else:
            red_ready_costs = red_button * 20
            total_red_costs = red_ready_costs
    if blue_button != 0:
        express = int(input("「青チップ」特急個数を入力: "))
        if express != 0:
            blue_express_costs = express*40
            blue_ready_costs = (blue_button - express) * 20
            total_blue_costs = blue_express_costs + blue_ready_costs
        else:
            blue_ready_costs = blue_button * 20
            total_blue_costs = blue_ready_costs
    if yellow_button != 0:
        express = int(input("「黄チップ」特急個数を入力: "))
        if express != 0:
            yellow_express_costs = express*40
            yellow_ready_costs = (yellow_button - express) * 20
            total_yellow_costs = yellow_express_costs + yellow_ready_costs
        else:
            yellow_ready_costs = yellow_button * 20
            total_yellow_costs = yellow_ready_costs
    green_cost = green_button*20
    orange_cost = orange_button*5
    total_costs =  total_red_costs + total_blue_costs + total_yellow_costs + green_cost + orange_cost
    return total_costs

def JuniorStrategyCostsCalculation(red_button, blue_button, yellow_button, green_button, orange_button): #ジュニア卓ルールの時のみに呼び出す
    red_cost, blue_cost, yellow_cost = 0,0,0
    if red_button > 4:
        red_cost = (red_button - 3)*20
    else:
        red_cost = 20
    if blue_button > 4:
        blue_cost = (blue_button - 3)*20
    else:
        blue_cost = 20
    if yellow_button > 4:
        yellow_cost = (yellow_cost - 3)*20
    else:
        yellow_cost = 20
    green_cost = green_button*20
    orange_cost = orange_button*5
    total_costs = red_cost + blue_cost + yellow_cost + green_cost + orange_cost
    return total_costs

# 減価償却を計算
small_machines = int(input("小型機械の個数: "))
large_machines = int(input("大型機械の個数: "))
attachments = int(input("アタッチメントの個数: "))

def depreciations(small_machines, large_machines, attachments):
    if table_rule == 0:
        small_depreciations = int(10)
        large_depreciations = int(20)
        attachments_depreciations = int(3)
        depreciations_cost = small_machines*small_depreciations + large_machines*large_depreciations + attachments*attachments_depreciations
    else:
        small_depreciations = int(20)
        large_depreciations = int(40)
        attachments_depreciations = int(6)
        depreciations_cost = small_machines*small_depreciations + large_machines*large_depreciations + attachments*attachments_depreciations
    print(f"減価償却費：{depreciations_cost}円")
    return depreciations_cost


# 借金返済による固定費計算
short_term_loans = int(input("短期借入金の額を入力してください(ない場合は0): "))
long_term_loans = int(input("長期借入金の額を入力してください(ない場合は0: )"))

def loansCalculation(short_term_loans, long_term_loans):
    short_term_repayment = round(short_term_loans*0.2)
    long_term_repayment = round(long_term_loans*0.1)
    total_repayment = short_term_repayment + long_term_repayment
    return total_repayment

# その他損失に関する計算
other_costs = int(input("その他人件費や損失を入力してください(例：クレーム処理・採用・配転・退職など: )"))

#　全てのコストを以下で計算（シニア卓の場合とジュニア卓の場合で条件分岐）

def all_total_costs_calculation():
    if table_rule == 1:
        all_total_costs = personnelAndMachineCosts(term, employee_now, employee_max, machine) + SeniorStrategyCostsCalculation(red_button, blue_button, yellow_button, green_button, orange_button) + depreciations(small_machines, large_machines, attachments) + loansCalculation(short_term_loans, long_term_loans)*2 + other_costs
    else:
        all_total_costs = personnelAndMachineCosts(term, employee_now, employee_max, machine) + JuniorStrategyCostsCalculation(red_button, blue_button, yellow_button, green_button, orange_button) + depreciations(small_machines, large_machines, attachments) + loansCalculation(short_term_loans, long_term_loans)*2 + other_costs
    return all_total_costs

all_total_costs = all_total_costs_calculation()

print("------------------------------------------------")
print(f"今期の予想固定費は: {all_total_costs}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 次に損益分岐までに必要な売上を計算する


f = all_total_costs
import_price = [14,15,16]

def variableCostCalculation(import_price):
    variable_cost = import_price + 2
    return variable_cost

def breakEvenPointCalculation(f, target_price, variable_cost):
    break_even_point = math.ceil(f/(target_price - variable_cost))
    return break_even_point

def printEvenPointCalculation(f, import_price, target_price):
    for i in import_price:
        variable_cost = variableCostCalculation(i)
        print(f"平均仕入れ価格: {i} --> 変動費: {variable_cost}\n")
        max_price = min(target_price + 5, 40)
        min_price = max(target_price - 5, 20)
        prices = range(min_price, max_price + 1)
        for target_price in prices:
            break_even_point = breakEvenPointCalculation(f, target_price, variable_cost)
            print(f"目標価格: {target_price} --> 必要販売数: {break_even_point}")
while True:
    try:
        target_price = int(input("今期、商品ひとつあたりの目標販売価格を入力してください（範囲: 20~40) : "))
        if 20 <= target_price <= 40:
            break
    except ValueError:
            print(f"20から40までの数字で入力してください")

printEvenPointCalculation(f, import_price, target_price)

# ----------------------------------------------------------------------------------------------------------------------------------
# 損益分岐点の関係をグラフ化する関数
def GraphDisplay(f, import_price, target_price):
    prices = range(max(target_price - 5, 20), min(target_price + 5, 40) + 1)
    for i in import_price:
        variable_cost = variableCostCalculation(i)
        break_even_points = []
        for price in prices:
            bep = breakEvenPointCalculation(f, price, variable_cost)
            break_even_points.append(bep if bep != float('inf') else None)
        
        plt.plot(prices, break_even_points, marker='o', label=f'Variable Costs: {variable_cost}')

    plt.title("Relationship between BreakEvenPoint and Prices")
    plt.xlabel("Prices")
    plt.ylabel("BreakEvenPoint (Sum of Sales)")
    plt.xticks(prices)
    plt.legend()
    plt.grid(True)
    plt.show()

# グラフ表示を実行
GraphDisplay(f, import_price, target_price)