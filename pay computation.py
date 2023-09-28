def compute_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate

    else:
        regualar_hours = 40 
        overtime_hours = hours - 40 
        pay = (regualar_hours * rate) + (overtime_hours * rate * 1.5)
    return pay 


hours_worked = float(input("Enter hours --> "))
hours_rate = float(input("Enter Rate: "))
total_pay = compute_pay(hours_worked, hours_rate)

print(f"Pay: {total_pay:1f}")

    

