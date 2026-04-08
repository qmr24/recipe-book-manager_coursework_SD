#Note: The Main code has been divided according to task numbers for clarity and ease of evaluation.
#These sections are intended for demonstration purposes and may not run as a complete standalone program.

recipes = {} #main recipes dictionary
rec_count = 1  #recipe count
units = ['g', 'kg', 'ml', 'l', 'cup', 'tbsp', 'tsp', 'piece'] #permissable ingredient units


#TASK 1
def validate_recipe_name(): 
    while True:  
        receipe_name = input("Enter the recipe name: ") 
        if len(receipe_name) == 0:   
            print("Recipe name can't be empty.")
            continue
        if not (3 <= len(receipe_name) <= 50): 
            print("Recipe name should contain between 3 and 50 characters.")
            continue
        if receipe_name.isspace():   
            print("Recipe name can't contain only spaces.")
            continue
        valid = True  
        letter = False 
        for i in receipe_name:   
            if i.isalpha(): 
                letter = True   
            elif i in (" ", "-", "'"): 
                pass  #going to the next loop(next character)
            else:
                print("Only letters, hyphen (-), apostrophe ('), and space are allowed.")
                valid = False 
                break
        if not valid:
            continue
        if not letter: 
            print("Recipe name must contain at least one letter.")
            continue
        return receipe_name  #returning the recipe_name 

#TASK 1
def validate_ingredient_name():
    main_ing = [] #main list which contain main ingredient information such as ingredient name,quantity,unit
    ing = []
    
    while True:
        try:
            ingr_count = int(input("Enter the number of ingredients (3-20): ")) #assking the user number of ingredients
            if 3 <= ingr_count <= 20:  #checking whether ingredient count is in between 3-20
                break # if so coming out of the loop
            else:
                print("Number of ingredients must be between 3 and 20.")
        except ValueError: #if user enter any string value printing this error message and asking again the ingredient count
            print("Please provide the ingredient count as a whole number.")
    count=0
    while count < ingr_count: #setting the loop which cover the ingredient count
        while True:
            ing_name = input("Enter the ingredient name: ")
            if not (3 <= len(ing_name) <= 30): #checking whether the length of the ingredient name is in between 3-30
                print("Ingredient name should be between 3 and 30 characters.")
                continue
            ing_name = ing_name.lower() #converting the entered ingredient name into lower case
            if ing_name in ing: #checking whether is the ingredient name is already exist
                ask = input("Duplicate ingredient detected! Add anyway? (yes/no): ") #if exist asking whether to re enter again 
                if ask.lower() != "yes": #if no need to re enter again continue to ask the ingredient name again 
                    continue
            ing.append(ing_name) #appending the ingredient name to the ing list
            ing_quan_unit=validate_ingredient_details(ing_name)
            main_ing.append(ing_quan_unit)
            count= count+ 1 #adding the  count by 1 after getting user ingredient name, quantity and unit
            break
    return main_ing
        
        
#TASK 1
def validate_ingredient_details(ing_name):
    while True:
        try:
            ing_quan = float(input("Enter the quantity: ")) #asking the ingredient quantity 
            if ing_quan > 0: #checkinng whether quantity is greather than 0
                break
            else:
                print("Quantity must be greater than 0.")
        except ValueError: #if the user enter any other unsupported input such as string
            print("Enter a valid number.")
    while True:
        ing_uni = input("Enter unit (g, kg, ml, l, cup, tbsp, tsp, piece): ")#asking the user input the ingredient unit
        if ing_uni.lower() in units: #checking the entered unit is in the accepted list of units by making the entered input in to lower case
            break
        else:
            print("Invalid unit!")
    return (ing_name,ing_quan,ing_uni)
    

#TASK 1
def recipe_time_validation():
    while True:
        try:
            time = input("Enter cooking time (HH:MM): ")
            if len(time) == 5 and time[2] == ":": #checking the length of enterd string is 5 and 2 position is ":"
                Hour = int(time[:2]) #denoting hour value in integer
                Min = int(time[3:]) #denoting minute value in integer
                if not (0 <= Hour <= 12 and 0 <= Min <= 59): #checking whether the hour and minute in the specified value
                    print("Invalid time range,Time must be between 00:05 and 12:00")
                    continue
                if 5 <= (Hour * 60 + Min) <= 720:  #checking the entered time value is in the value between 5 minutes and 12 hour
                    return time
                else:
                    print("Time must be between 00:05 and 12:00.")
            else:
                print("Format must be HH:MM")
        except ValueError:
            print("Invalid format.") #if the user input the time any other format generating an error message 
    
#TASK 1
def recipe_category_tags_validation():
    cate = ["BREAKFAST", "LUNCH", "DINNER", "DESSERT", "SNACK", "BEVERAGE"]
    while True:
        rec_cate = input("Enter the recipe category (BREAKFAST, LUNCH, DINNER, DESSERT, SNACK, BEVERAGE): ").upper() #taking the category from the user in upper case
        if rec_cate in cate: #checking whether the entered category is in the verified category list
            break
        print("Invalid category.")
    return rec_cate


#TASK 1
def recipe_tags():
    tags = set()
    while True:
        rec_tags = input("Enter a tag: ") #asking for the tags
        tags.add(rec_tags) #adding the enetered tags to the list 

        permission = input("Add more? (+/-): ") #asking the user whether to add more
        if permission == "-":
            print("tags added successfuly")
            break
        if permission == "+":
            continue
        else:
            print("enter either + or -")
    return tags
