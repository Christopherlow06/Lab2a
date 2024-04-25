def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    num_list = get_user_input()
    average = calc_average_temperature(num_list)
    tempList = calc_min_max_temperature(num_list)

    print("The average temperature is " + str(average))

    print("The maximum value is " + str(tempList[1]))
    print("The minimum value is " + str(tempList[0]))
    
def get_user_input():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
    x = input()
    s = x.split(",")
    n = list(map(float, s))
    return n

def calc_average_temperature(num_list):
    average = sum(num_list)/len(num_list)
    return average

def calc_min_max_temperature(num_list):
    num_list.sort()
    max = num_list[-1]
    min = num_list[0]
    
    integerList = [max, min]
    return integerList
    

if __name__ == "__main__":
    main()
