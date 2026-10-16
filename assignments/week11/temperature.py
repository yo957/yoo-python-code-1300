"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
<<<<<<< HEAD
def get_temperatures():
    temps =[]
    for i in range(7):
        temp = float(input(f"Enter your temperature{i+1}: "))
        temps.append(temp)
        return temps
def analyze_temps(temp_list):
        avg = sum(temp_list) / len(temp_list)
        high = max(temp_list)
        low = min(temp_list)
        return avg, high, low
def display_analysis(avg, high, low):
    print("\nTemperature Analysis for the Week: ")
    print(f"Average: {avg:.1f}C")
    print(f"Highest: {high:g}C")
    print(f"Lowest: {low:g}C")
input = get_temperatures()
result = analyze_temps(input)
display_analysis(result[0], result[1], result[2])
=======
    
>>>>>>> upstream/main
