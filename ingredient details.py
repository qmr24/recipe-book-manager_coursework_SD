recipes = {}  
rec_count = 1  
units = ['g', 'kg', 'ml', 'l', 'cup', 'tbsp', 'tsp', 'piece'] 


def validate_recipe_input():   
    global rec_count
    global recipes
    ing = []  
    count = 0
    main_ing=[]

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

        for i in range(len(receipe_name)):      
            if receipe_name[i].isalpha():       
                letter = True
            elif receipe_name[i] in (" ", "-", "'"):    
                pass    
            else:   
                print("Only letters, hyphen (-), apostrophe ('), and space are allowed.")
                valid = False
                break   

        if valid == False:   
            continue    

        if letter == False:
            print("Recipe name must contain at least one letter.")
            continue   

        break   


    while True:
        try:
            ingr_count = int(input("Enter the number of ingredients (3-20): "))
            if 3 <= ingr_count <= 20:
                break
            else:
                print("Number of ingredients must be between 3 and 20.")
        except ValueError:
            print("Please provide the ingredient count as a whole number.")


    while count < ingr_count:
        while True:
            ing_name = input("Enter the ingredient name: ")
            if not (3 <= len(ing_name) <= 30):
                print("Ingredient name should be between 3 and 30 characters.")
                continue

          
            ing_name = ing_name.lower()
            if ing_name in ing :
                ask = input("Duplicate ingredient detected! Add anyway? (y/n): ")
                if ask.lower() != "y":
                    continue
            ing.append(ing_name)
            break

        while True:
            try:
                ing_quan = float(input("Enter the quantity of the ingredient: "))
                if ing_quan > 0:
                    break
                else:
                    print("Ingredient quantity should be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        while True:
            ing_uni = input("Enter the unit (g, kg, ml, l, cup, tbsp, tsp, piece): ")
            if ing_uni.lower() in units:
                break
            else:
                print("Invalid unit! Accepted units: g, kg, ml, l, cup, tbsp, tsp, piece")
        count = count + 1
        main_ing.append((ing_name,ing_quan,ing_uni))
        


    while True:
        try:
            time = input("Enter the cooking time as HH:MM: ")
            if len(time) == 5 and time[2] == ":":
                Hour = int(time[0:2])
                Min = int(time[3:5])
                if not (0 <= Hour <= 12 and 0 <= Min <= 59):
                    print("Invalid hours or minutes. Hours: 0-12, Minutes: 0-59.")
                    continue
                if 5 <= (Hour * 60) + Min <= 720:
                    break
                else:
                    print("Time must be between 00:05 and 12:00.")
            else:
                print("Time format is wrong. It should be HH:MM (e.g. 01:30).")
        except ValueError:
            print("Enter the time in correct format HH:MM.")

    
    cate = ["BREAKFAST", "LUNCH", "DINNER", "DESSERT", "SNACK", "BEVERAGE"]
    while True:
        rec_cate = input("Enter the recipe category (BREAKFAST, LUNCH, DINNER, DESSERT, SNACK, BEVERAGE): ")
        if rec_cate.upper() in cate:
            rec_cate = rec_cate.upper()  
            break
        print("Invalid category. Please choose from: BREAKFAST, LUNCH, DINNER, DESSERT, SNACK, BEVERAGE")
    tags=set()
    while True:
        rec_tags=input("enter the tags related to this recipe")
        tags.add(rec_tags)
        permission=input("add more or enough(+/-)")
        if permission=="+":
            continue
        elif permission=="-":
            break

    rec_num="RCP"+str(rec_count).zfill(3)
    recipes[rec_num] = {"name": receipe_name,"Ingredients": main_ing, "time": time,"Category": rec_cate,"tags":tags}
    rec_count=rec_count+1



    
    print("\n========================================")
    print("       Recipe Validated Successfully")
    print("========================================")
    print(f"  Name        : {receipe_name}")
    print(f"  Ingredients : {len(ing)}")
    print(f"  Category    : {rec_cate}")
    print(f"  Cooking Time: {time}")
    print("========================================\n")



def single_display(REC_ID):
    try:
        print("========================================")
        print(f"Recipe ID: {REC_ID}")
        print(f"Name: {recipes[REC_ID]['name']}")
        print(f"Category: {recipes[REC_ID]['Category']}")
        print(f"Cooking Time: {recipes[REC_ID]['time']}")
        print("----------------------------------------")
        print("Ingredients:")
        for Ingredient in recipes[REC_ID]['Ingredients']:
            print(Ingredient[0],Ingredient[1],Ingredient[2])
        
        print("========================================\n")
    except:
        print("enter the valid and available ID")




def summary_display():
    print("Display All Recipes (Summary)")
    print(f"Total Recipes: {len(recipes)}")
    print("----------------------------------------")
    for key in recipes:
        print(f"Recipe ID: {key} | {recipes[key]['name']} | {recipes[key]['Category']} | {recipes[key]['time']} ")

def cate_display():
    print("01.BREAKFAST")
    print("02.LUNCH")
    print("03.DINNER")
    print("04.DESSERT")
    print("05.SNACK")
    print("06.BEVERAGE")
    while True:
        try:
            rec_cat=int(input("enter the category number"))
            if rec_cat==1:
                count=0
                rec=[]
                for key in recipes:
                    if recipes[key]["Category"] == "BREAKFAST" :
                        count=count+1
                        rec.append(recipes[key]["name"])
                print(f"WE FOUND {count} RECEPIES UNDER THIS CATEGORY")
                if len(rec)>0:
                    for i in rec:
                        print(i)
                else:
                    print("not found any recipe in that categotry")
                break
                    
            elif rec_cat==2:
                count=0
                rec=[]
                for key in recipes:
                    if recipes[key]["Category"] == "LUNCH" :
                        count=count+1
                        rec.append(recipes[key]["name"])
                print(f"WE FOUND {count} RECEPIES UNDER THIS CATEGORY")
                if len(rec)>0:
                    for i in rec:
                        print(i)
                else:
                    print("not found any recipe in that categotry")
                break
            elif rec_cat==3:
                count=0
                rec=[]
                for key in recipes:
                    if recipes[key]["Category"] == "DINNER" :
                        count=count+1
                        rec.append(recipes[key]["name"])
                print(f"WE FOUND {count} RECEPIES UNDER THIS CATEGORY")
                if len(rec)>0:
                    for i in rec:
                        print(i)
                else:
                    print("not found any recipe in that categotry")
                break
            elif rec_cat==4:
                count=0
                rec=[]
                for key in recipes:
                    if recipes[key]["Category"] == "DESSERT" :
                        count=count+1
                        rec.append(recipes[key]["name"])
                print(f"WE FOUND {count} RECEPIES UNDER THIS CATEGORY")
                if len(rec)>0:
                    for i in rec:
                        print(i)
                else:
                    print("not found any recipe in that categotry")
                break
            elif rec_cat==5:
                count=0
                rec=[]
                for key in recipes:
                    if recipes[key]["Category"] == "SNACK" :
                        count=count+1
                        rec.append(recipes[key]["name"])
                print(f"WE FOUND {count} RECEPIES UNDER THIS CATEGORY")
                if len(rec)>0:
                    for i in rec:
                        print(i)
                else:
                    print("not found any recipe in that categotry")
                break
            elif rec_cat==6:
                count=0
                rec=[]
                for key in recipes:
                    if recipes[key]["Category"] == "BEVERAGE" :
                        count=count+1
                        rec.append(recipes[key]["name"])
                print(f"WE FOUND {count} RECEPIES UNDER THIS CATEGORY")
                if len(rec)>0:
                    for i in rec:
                        print(i)
                else:
                    print("not found any recipe in that categotry")
                break
            else:
                print("enter a valid category number")
        except:
            print("enter the number value of the category")
        
def save_rec():
 #recipes[rec_num] = {"name": receipe_name,"Ingredients": main_ing, "time": time,"Category": rec_cate,"tags":tags}
    f=open("recipes.txt","w")
    try:
        if len(recipes) > 0:
            for key,value in recipes.items():
                f.write("===RECIPE===\n")
                f.write(f"ID:{key}\n")
                f.write(f"NAME:{recipes[key]['name']}\n")
                f.write(f"CATEGORY:{recipes[key]['Category']}\n")
                f.write(f"TIME:{recipes[key]['time']}\n")
                f.write(f"Ingredients:\n")
                for i in value['Ingredients']:
                    f.write(f"{i[0]}|{i[1]}|{i[2]}\n")
                f.write(f"TAGS:{','.join(recipes[key]['tags'])}\n")
                f.write("===END===\n")
                #recipes[rec_num] = {"name": receipe_name,"Ingredients": main_ing, "time": time,"Category": rec_cate,"tags":tags}
            print("Recipes saved successfully to recipes.txt")
        else:
            print("you must enter atleast one recipe inorder to save in the file")
    except:
        print("Error cant save your file")

def prevsa():
    try:
        global recipes
        global rec_count
        f = open("recipes.txt", "r")
        rec_num = ""
        while True:
            read = f.readline()
            if read == "":
                break
            read = read.strip()
            if read == "===RECIPE===":
                rec_count = rec_count + 1
            elif read.startswith("ID:"):
                rec_num = read[3:]
                recipes[rec_num] = {}
                recipes[rec_num]["Ingredients"] = []
            elif read.startswith("NAME:"):
                recipes[rec_num]["name"] = read[5:]
            elif read.startswith("CATEGORY:"):
                recipes[rec_num]["Category"] = read[9:]
            elif read.startswith("TIME:"):
                recipes[rec_num]["time"] = read[5:]
            elif read.startswith("TAGS:"):
                recipes[rec_num]["tags"] = set(read[5:].split(","))
            elif "|" in read:
                parts = read.split("|")
                recipes[rec_num]["Ingredients"].append((parts[0], parts[1], parts[2]))
        f.close()
        print(f"Loaded {rec_count - 1} recipes successfully")
    except:
        print("No saved recipes found. Starting Fresh")
                
                
            
def export_recipe():
    while True:
        rec_id = input("Enter the recipe ID to export (e.g. RCP001): ").upper()
        if rec_id in recipes:
            recipe_name = recipes[rec_id]["name"]
            file_name = "recipe_" + recipe_name + ".txt"
            f = open(file_name, "w")
            f.write(f"RECIPE: {recipes[rec_id]['name']}\n")
            f.write("==============================\n")
            f.write(f"Category: {recipes[rec_id]['Category']}\n")
            f.write(f"Cooking Time: {recipes[rec_id]['time']}\n")
            f.write("INGREDIENTS:\n")
            for i in recipes[rec_id]['Ingredients']:
                f.write(f"- {i[0]}: {i[1]} {i[2]}\n")
            f.write(f"TAGS: {','.join(recipes[rec_id]['tags'])}\n")
            f.write("==============================\n")
            f.close()
            print(f"Recipe exported successfully to {file_name}")
            break
        else:
            print("Recipe ID not found! Try again")

def search_ingredient():
    while True:
        try:
            found=0
            ask=input("enter the ingredient name")
            for i in recipes:
                for y in recipes[i]["Ingredients"]:
                    if ask.lower() in y[0].lower():
                        print(recipes[i]["name"])
                        found=found+1
                        break
            print(f"we found{found} recipes related to {ask} ingredient name")
            break
            
        except:
            print("enter valid ingredient name")
            continue







            #recipes[rec_num] = {"name": receipe_name,"Ingredients": main_ing, "time": time,"Category": rec_cate,"tags":tags}

def filter_recipes():
    time=input("do you want filter by time (yes/no)")
    if time.lower()=="yes":
        max_time=int(input("enter the maximun cooking time in minutes"))
        min_time=int(input("enter the maximun cooking time in minutes"))
    no_ingredient=input("do you want filter by no.ingredients (yes/no)")
    if no_ingredient.lower()=="yes":
        max_ingre=int(input("enter the maximum ingredient count"))
        min_ingre=int(input("enter the minimum ingredient count"))
    cate=input("do you want filter by category (yes/no)")
    if cate.lower():
        categ=input("enter the category name")
    
    








                
                
                
            
        
        









prevsa()
while True:
    print("                             ")
    print("                             ")
    print("=============================")
    print("=WELCOME TO THE QUMAIR HOTEL=")
    print("Today, what you would like to do ?")
    print(" 1.Add recipe to collection \n 2.View specific recipe by ID \n 3.List all recipe ID with names \n 4.Count recipe per category \n 5.Exit \n 6.Save \n 7.export recipe \n 8.search ingredient")

    try:
        value = int(input("enter the required service number"))

        if value == 1:
            while True:
                validate_recipe_input()
                add = input("Add another recipe? (yes/no)") 
                if add.lower() == "yes":
                    pass
                else:
                    break

        elif value == 2:
            try:
                if len(recipes) > 0:
                    recid = input("enter the recipe id")
                    rec_id = recid.upper()
                    single_display(rec_id)
                else:
                    print("there is no recipes available to do this function")
            except:
                print("enter correct recipe id as (RCP001)")

        elif value == 3:
            if len(recipes) > 0:
                summary_display()
            else:
                print("there is no recipes available to do this function")

        elif value == 4:
            if len(recipes) > 0:
                cate_display()
            else:
                print("there is no recipes available to do this function")

        elif value == 6:
            save_rec()

        elif value == 5:
            try:
                ask=input("do you want to save(yes/no)")
                if ask.lower()=="yes":
                    save_rec()
                    print("thank you !!")
                    break
                else:
                    print("thank you !!")
                    break
            except:
                print("enter a valid input")
        elif value== 7:
            export_recipe()
        elif value == 8:
            search_ingredient()
            
                

        else:
            print("enter service number between 1-5")

    except:
        print("enter correct service number")
