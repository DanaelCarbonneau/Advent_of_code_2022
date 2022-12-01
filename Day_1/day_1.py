


def main():
    #we get the list
    f = open("input_1.txt","r")
    string_input = f.read()
    f.close()

    #we separate the string to get one by element of the list
    list_calories_per_elves = string_input.split("\n\n")

    #list_res : list[int], records for each elf the total amount of calories carried
    list_res = []
    #we go through the list of calories to calculate how much is an elf carrying
    for elf in list_calories_per_elves : 
        #list_calories_elf : list[string], we split by "\n" to get the numbers in a list of strings
        list_calories_elf = elf.split("\n")

        #res_elf : int, records the total amount of calories of an elf
        res_elf = 0

        #we go through the values to calculate the total amount of calories
        for value in list_calories_elf :
            if(value != ''):
                res_elf = res_elf + int(value, base=10)
        #We've calculated the total amount carried by this elf, we can then add this to the list
        list_res.append(res_elf)
    
    #We sort the list 
    list_res.sort()
    #The result is the last element of the list
    print(list_res[-1])




if __name__ == '__main__':
	main()

