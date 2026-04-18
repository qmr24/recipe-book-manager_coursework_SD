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
            


#TASK 2
def single_display(REC_ID):#no need global since we are only reading in this function(no modification)
    try:
        print("========================================")
        print(f"Recipe ID: {REC_ID}")                     #printing the recipe id
        print(f"Name: {recipes[REC_ID]['name']}")         #printing the recipe name by accessing the dictionary
        print(f"Category: {recipes[REC_ID]['Category']}") #printing the recipe category by accessing the dictionary
        print(f"Cooking Time: {recipes[REC_ID]['time']}") #printing the recipe time by accessing the dictionary
        print("----------------------------------------")
        print("Ingredients:")
        for Ingredient in recipes[REC_ID]['Ingredients']:    #creating a loop for a the list in the ingredient
            print(Ingredient[0],Ingredient[1],Ingredient[2]) #accessing the tuple which  is in the main list
        
        print("========================================\n")
    except:
        print("enter the valid and available ID") #if the error occour due to not available of that respective id printhing this message




#TASK 2
def summary_display():
    print("Display All Recipes (Summary)")  
    print(f"Total Recipes: {len(recipes)}")
    print("----------------------------------------")
    for key in recipes:
        print(f"Recipe ID: {key} | {recipes[key]['name']} | {recipes[key]['Category']} | {recipes[key]['time']} ") #by accessing the dictionary by a for loop printing the the id,name,category and the time


#TASK 2    
def save_rec():
    f=open("recipes.txt","w") #opening the recipes.txt in write mode
    try:
        if len(recipes) > 0: #access to the body if the length of the recipes is more than 0
            for key,value in recipes.items(): #taking the key and the value of the recipes to the kay and value variable
                f.write("\n ===RECIPE===\n")
                f.write(f"ID:{key}\n")
                f.write(f"NAME:{recipes[key]['name']}\n")
                f.write(f"CATEGORY:{recipes[key]['Category']}\n")
                f.write(f"TIME:{recipes[key]['time']}\n")
                f.write(f"Ingredients:\n")
                for i in value['Ingredients']: # craeting a loop for the each value's ingredient 
                    f.write(f"{i[0]}|{i[1]}|{i[2]}\n") #writing the ingredient name,quantity and the unit by seperating by "|"
                f.write(f"TAGS:{','.join(recipes[key]['tags'])}\n") # Convert the set of tags into a comma-separated string and write it to the file with "TAGS:" label
                f.write("===END===\n \n")
                #recipes[rec_num] = {"name": receipe_name,"Ingredients": main_ing, "time": time,"Category": rec_cate,"tags":tags}
            f.close()
            print("Recipes saved successfully to recipes.txt")
        else:
            print("you must enter atleast one recipe inorder to save in the file")
    except:
        print("Error cant save your file")

#TASK 2
def prevsa():
    try:
        global recipes
        global rec_count
        f = open("recipes.txt", "r") #opening the recipes.txt in read mode 
        rec_num = "" 
        while True:
            read = f.readline() #reading a line
            if read == "": #if the read is empty break for the loop
                break
            read = read.strip()
            if read.startswith("ID:"): #if the raed starts with ID
                rec_num = read[3:] #getting only the ID from  the read
                recipes[rec_num] = {} #creating a key in recipes dictionary
                recipes[rec_num]["Ingredients"] = [] #creating a list for the ingredient for that id
            elif read.startswith("NAME:"): #if the read starts with NAME
                recipes[rec_num]["name"] = read[5:] #getting only the name of the recipe from the  read and assigning as the name of that recipe 
            elif read.startswith("CATEGORY:"): #if the read starts with CATEGORY
                recipes[rec_num]["Category"] = read[9:] #getting only the category of the recipe from the  read and assigning as the category of that recipe 
            elif read.startswith("TIME:"): #if the read starts with TIME
                recipes[rec_num]["time"] = read[5:] #getting only the time of the recipe from the  read and assigning as the time of that recipe 
            elif read.startswith("TAGS:"): #if the read starts with TAGS
                recipes[rec_num]["tags"] = set(read[5:].split(",")) #getting only the tags of the recipe from the  read and assigning as the tags of that recipe which is seperated by , 
            elif "|" in read:
                parts = read.split("|")
                recipes[rec_num]["Ingredients"].append((parts[0], parts[1], parts[2]))
            elif read.startswith ("===RECIPE==="):
                pass
            elif read.startswith("===END==="):
                pass
        rec_count=len(recipes)+1 #adding a 1 to the length of recipes to make the rec_count 
        f.close()
        print(f"Loaded {rec_count - 1} recipes successfully")
    except:
        print("No saved recipes found. Starting Fresh") #if any error happen when the file is not there to read printing  this messaege
                
                
#TASK 3            
def export_recipe():
    while True:
        rec_id=input("Enter the recipe ID to export (e.g. RCP001):").upper().strip() #asking the user whcih recipe should be export to the file 
        if rec_id in recipes: #checking whether the id is in the recipes
            recipe_name = recipes[rec_id]["name"] #getting the name of the recipe for cretion of the file name
            file_name = "recipe_" + recipe_name + ".txt" #creating a file with the recipe name 
            f = open(file_name, "w")  #openig that file in write mode
            f.write(f"RECIPE: {recipes[rec_id]['name']}\n")  #writing the name of the recipe that should be export
            f.write("==============================\n")
            f.write(f"Category: {recipes[rec_id]['Category']}\n")   #writing the categoty of the recipe that should be export
            f.write(f"Cooking Time: {recipes[rec_id]['time']}\n")    #writing the time of the recipe that should be export
            f.write("INGREDIENTS:\n")
            for i in recipes[rec_id]['Ingredients'] :  #writing the ingredient of the recipe that should be export 
                f.write(f" {i[0]}: {i[1]} {i[2]}\n")
            f.write(f"TAGS: {','.join(recipes[rec_id]['tags'])}\n")
            f.write("==============================\n")
            f.close()
            print(f"Recipe exported successfully to {file_name}")
            break
        else:
            print("Recipe ID not found! Try again")

#TASK 3
def search_ingredient():
    while True:
        try:
            found=0
            ask=input("enter the ingredient name")
            for recipe_id in recipes:
                for item in recipes[recipe_id]["Ingredients"]:
                    if ask.lower() in item[0].lower():
                        print(recipes[recipe_id]["name"])
                        found=found+1
                        break
            print(f"we found{found} recipes related to {ask} ingredient name")
            break
            
        except:
            print("enter valid ingredient name")
            continue

#TASK 3
def cate_display():
    print("01.BREAKFAST\n02.LUNCH\n03.DINNER\n04.DESSERT\n05.SNACK\n06.BEVERAGE")
    
    categories = ["BREAKFAST", "LUNCH", "DINNER", "DESSERT", "SNACK", "BEVERAGE"]
    
    while True:
        try:
            rec_cat = int(input("enter the category number"))
            global recipes

            if 1 <= rec_cat <= 6:
                selected_category = categories[rec_cat - 1]  # map number to category
                
                count = 0
                rec = []

                for key in recipes:
                    if recipes[key]["Category"] == selected_category:
                        count += 1
                        rec.append(recipes[key]["name"])

                print(f"WE FOUND {count} RECEPIES UNDER THIS CATEGORY")

                if len(rec) > 0:
                    for i in rec:
                        print(i)
                else:
                    print("not found any recipe in that categotry")

                break
            else:
                print("enter a valid category number")

        except:
            print("enter the number value of the category")






            #recipes[rec_num] = {"name": receipe_name,"Ingredients": main_ing, "time": time,"Category": rec_cate,"tags":tags}

#TASK 3
results=[]
def filter_recipes_time():
    global recipes
    global results
    while True:
        time=input("do you want filter by time (yes/no)")
        if time.lower()=="yes":
            max_time=input("enter the maximun cooking time ")
            min_time=input("enter the minimum cooking time ")
            max_time_cal=int(max_time[0:2])*60+int(max_time[3:5])
            min_time_cal=int(min_time[0:2])*60+int(min_time[3:5])
            for key in recipes:
                time=recipes[key]["time"]
                time_cal=int(time[0:2])*60+int(time[3:5])
                if max_time_cal > time_cal > min_time_cal:
                    results.append(key)
            break
        elif time.lower()=="no":
            print("ok")
            break
        else:
            print("enter valid input")
            
    
#TASK 3
def filter_recipes_no_ingre():
    global recipes
    global results
    while True:
        no_ingredient=input("do you want filter by no.ingredients (yes/no)")
        if no_ingredient.lower()=="yes":
            max_ingre=int(input("enter the maximum ingredient count"))
            min_ingre=int(input("enter the minimum ingredient count"))
            for key in recipes:
                ingre_count=len(recipes[key]['Ingredients'])
                if max_ingre > ingre_count >  min_ingre:
                    if  key not in results :
                        results.append(key)
            break
        elif no_ingredient.lower()=="no":
            print("ok")
            break
        else:
            print('enter valid input')

#TASK 3
def filter_recipes_category():
    global results
    global recipes
    while True:            
        cate=input("do you want filter by category (yes/no)")
        if cate.lower()== "yes":
            categ=input("enter the category name")
            for key in recipes:
                if categ.upper()== recipes[key]["Category"]:
                    if  key not in results :
                        results.append(key)
            break
        elif cate.lower()=="no":
            print('ok')
            break
        else:
            print('enter valid input')
    print(f'=====FILTTER RESULT===== \n{results}')


#TASK 3
def change_name():
    global recipes
    rec_id=input("Enter the Recipe ID ").upper()
    if rec_id in recipes:
        new_name=validate_recipe_name()
        recipes[rec_id]['name'] = new_name
        print(f"Recipe {rec_id} updated successfully")
    else:
        print("Entered Recipe Id is not available")

#TASK 3
def add_ingredient():
    global recipes
    rec_id=input("Enter the Recipe ID ").upper()
    if rec_id in recipes:
        new_ingredient = validate_ingredient_name()
        recipes[rec_id]['Ingredients'].extend(new_ingredient)
        print(f"Recipe {rec_id} updated successfully")
    else:
        print("Entered Recipe Id is not available")
                    

#TASK 3
def del_ing_name():
    global recipes
    rec_id=input("Enter the Recipe ID ").upper()
    if rec_id in recipes:
        del_ing_name = input("Enter the ingredient name to remove: ").lower()
        found = False
        for item in recipes[rec_id]["Ingredients"]:
            if del_ing_name == item[0].lower():
                recipes[rec_id]["Ingredients"].remove(item)
                print(f"Ingredient removed from Recipe {rec_id} successfully")
                found = True
                break
        if not found:
            print("Ingredient not found")

#TASK 3           
def time_chan():
    global recipes
    rec_id=input("Enter the Recipe ID ").upper()
    if rec_id in recipes:
        time=recipe_time_validation()
        recipes[rec_id]["time"] = time
        print(f"Recipe {rec_id} time updated successfully")
    else:
        print("Entered Recipe Id is not available")
        
#TASK 3           
def cate_change():
    global recipes           
    rec_id=input("Enter the Recipe ID ").upper()
    if rec_id in recipes:
        rec_cate = recipe_category_tags_validation()        
        recipes[rec_id]["Category"] = rec_cate
        print(f"Recipe {rec_id} Category updated successfully")
    else:
        print("Entered Recipe Id is not available")

#TASK 3
def add_tags():
    global recipes
    rec_id=input("Enter the Recipe ID ").upper()
    if rec_id in recipes:
        tags=recipe_tags()
        recipes[rec_id]["tags"] = tags
        print(f"Recipe {rec_id} tags updated successfully")
    else:
        print("Entered Recipe Id is not available")

#TASK 3
def delete_recipe():
    global recipes
    rec_id=input("Enter the Recipe ID ").upper()
    if rec_id in recipes:
        del recipes[rec_id]
        print(f"Recipe {rec_id} deleted successfully")
    else:
        print("Entered Recipe Id is not available")

#TASK 3

def duplicate_rec():
    rec_id=input("ENTER THE RECIPE ID WHICH YOU NEED TO DUPLICATE: ").upper().strip()
    global recipes
    global rec_count
    if rec_id in recipes:
        rec_num = "RCP" + str(rec_count).zfill(3)
        recipes[rec_num] ={
        "name": recipes[rec_id]['name'],
        "Ingredients": recipes[rec_id]['Ingredients'],
        "time": recipes[rec_id]['time'],
        "Category": recipes[rec_id]['Category'],
        "tags": recipes[rec_id]['tags']}
        rec_count += 1
        print(f"Recipe duplicated successfully as {rec_num}")
    else:
        print("Entered Recipe Id is not available")    


#TASK 4
def statis_category():
    bre_count=0 #assigning bre_count as 0 to count breakfast recipe
    lun_count=0 #assigning lun_count as 0 to count lunch recipe
    din_count=0 #assigning din_count as 0 to count dinner recipe
    des_count=0 #assigning des_count as 0 to count dessert recipe
    sna_count=0 #assigning sna_count as 0 to count snack recipe
    bev_count=0 #assigning bev_count as 0 to count beverage recipe
    global recipes
    print("\n=====RECIPE BOOK SUMMARY=====")
    print(f"Total Recipes:{len(recipes)}\n Recipes by Category:")
    for x in recipes:
        if recipes[x]['Category'] == "BREAKFAST": 
            bre_count=bre_count+1  
        if recipes[x]['Category'] == "LUNCH":
            lun_count=lun_count+1
        if recipes[x]['Category'] == "DINNER":
            din_count=din_count+1
        if recipes[x]['Category'] == "DESSERT":
            des_count=des_count+1
        if recipes[x]['Category'] == "SNACK":
            sna_count=sna_count+1
        if recipes[x]['Category'] == "BEVERAGE":
            bev_count=bev_count+1
    print(f"BREAKFAST:{bre_count}\nLUNCH:{lun_count}\nDINNER:{din_count}\nDESSERT:{des_count}\nSNACK:{sna_count}\nBEVERAGE:{bev_count}\n ")
    
#TASK 4    
def statis_time():
    print("Cooking Time Distribution:\n")
    quick=0
    medium=0
    long=0
    global recipes
    for x in recipes: #looping the through the recipe 
        time_duration=recipes[x]['time'] #getting the time of the recipe
        time_in_min=(int(time_duration[:2])*60)+int(time_duration[3:]) #converting the time to the minutes
        if time_in_min < 30: #checking the time is less than 30
            quick=quick + 1
        elif 30<=time_in_min < 60: #checking the time is less than 60
            medium=medium + 1
        elif time_in_min >= 60: #checking the time is equal or greater than 60
            long=long+1
    print(f"01.Quick (<30 min):{quick}recipes")
    print(f"02.Medium (30-60 min):{medium}recipes")
    print(f"03.Long (>60 min):{long}recipes\n ")
   
#TASK 04
def top_ing_count():
    global recipes
    ing_count = {}
    for key in recipes:
        for i in recipes[key]["Ingredients"]:
            ing_name = i[0].lower()
            if ing_name in ing_count:
                ing_count[ing_name] += 1
            else:
                ing_count[ing_name] = 1

    sort_list= sorted(ing_count.items(), key=lambda x: x[1], reverse=True) #used ChatGpt to generate this line
    print("\nMost Used Ingredients:")
    if len(sort_list) == 0:
        print("No ingredients found")
        return
    if len(sort_list) >= 3:
        top_n = 3
    else:
        top_n = len(sort_list)
    for i in range(top_n):
        print(f"{i+1}. {sort_list[i][0].capitalize()} - appears in {sort_list[i][1]} recipes")


#TASK 04
def statis_ingredient():
    total_ing=0 #assigning total_ing as o which will get the total number of ingredients
    max_ing_rec=0 #assigning max_ing_rec as 0 which will store tha max ingredient count
    max_rec_name ="not" #used to store the id of the recipe which has the max ingredient
    min_ing_rec=50 #assigning min_ing_rec as 50 which will store tha min ingredient count
    min_rec_name = "not"  #used to store the id of the recipe which has the min ingredient
    global recipes
    for x in recipes:
        total_ing=total_ing + len(recipes[x]['Ingredients'])  
        len_ing_rec=len(recipes[x]['Ingredients'])
        if max_ing_rec < len_ing_rec:
            max_ing_rec=len_ing_rec
            max_rec_name= x
        elif min_ing_rec > len_ing_rec:
            min_ing_rec = len_ing_rec
            min_rec_name= x
    avg_rec=total_ing/len(recipes) #calculating the average of the ingredient
    print(f"\n01.Average Ingredients per Recipe:{avg_rec}")
    print(f"02.Largest Recipe:{max_rec_name} with {max_ing_rec} ingredients")
    print(f"03.Smallest Recipe:{min_rec_name} with {min_ing_rec} ingredients")
    print(f"{'='*45}")
    
    
    
    

prevsa()   
while True:
    print("                             ")
    print("=============================")
    print("DIGITAL RECIPE BOOK MANAGER")
    print("=============================")
    print(" 1.Add New Recipe \n 2.View All Recipes \n 3.View Recipe by ID \n 4.Count recipe per category \n 5.View Statistics \n 6.Save Recipes \n 7.Export Recipe \n 8.Search by Ingredient \n 9.Filter Recipes \n 10.Edit Recipe \n 11.Exit")
    print("=============================\nEnter your choice(1-11)")
    try:
        value = int(input("Enter the required service number"))

        if value == 1:
            while True:
                receipe_name=validate_recipe_name()
                main_ing=validate_ingredient_name()
                time=recipe_time_validation()
                rec_cates=recipe_category_tags_validation()
                tags=recipe_tags()
                rec_num = "RCP" + str(rec_count).zfill(3)

                recipes[rec_num] = {"name": receipe_name,"Ingredients": main_ing,"time": time,"Category": rec_cates,"tags": tags}
                rec_count += 1 #adding the recipe count by one since all the details related to the recipe were validate successfully
    
                print("\n========================================")
                print("       Recipe Validated Successfully")
                print("========================================")
                print(f"  Name        : {receipe_name}")
                print(f"  Ingredients : {len(main_ing)}")
                print(f"  Category    : {rec_cates}")
                print(f"  Cooking Time: {time}")
                print(f"  Tags: {tags}")
                print("========================================\n")
                add = input("Add another recipe? (yes/no)") 
                if add.lower() == "yes":
                    pass
                elif add.lower()=="no":
                    break
                else:
                    print("invalid input")

        elif value == 3:
            try:
                if len(recipes) > 0:
                    recid = input("enter the recipe id")
                    rec_id = recid.upper()
                    single_display(rec_id)
                else:
                    print("there is no recipes available to do this function")
            except:
                print("enter correct recipe id as (RCP001)")

        elif value == 2:
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

        elif value == 11:
            try:
                ask=input("do you want to save(yes/no)")
                if ask.lower()=="yes":
                    save_rec()
                    print("thank you !!")
                    break
                elif ask.lower()=="no":
                    print("thank you !!")
                    break
                else:
                    print("enter either yes or no")
            except:
                    print("enter a valid input")
        elif value== 7:
            export_recipe()
        elif value == 8:
            search_ingredient()
        elif value == 9:
            if len(recipes)>0:
                filter_recipes_time()
                filter_recipes_no_ingre()
                filter_recipes_category()
            else:
                print("There is no recipes available to filter")
            
        elif value == 10:
            print(" 1.change name \n 2.add an ingredient \n 3.remove an ingredient \n 4.update cooking time \n 5.change category \n 6.Change tags \n 7.Delete a recipe \n 8.Duplicate Recipe")
            try:
                no_edit_service=int(input("Enter the service number to be performed"))
                if no_edit_service == 1:
                    change_name()
                elif no_edit_service == 2:
                    add_ingredient()
                elif no_edit_service == 3 :
                    del_ing_name()
                elif no_edit_service == 4:
                    time_chan()
                elif no_edit_service == 5:
                    cate_change()
                elif no_edit_service == 6:
                    add_tags()
                elif no_edit_service == 7:
                    delete_recipe()
                elif no_edit_service == 8:
                    duplicate_rec()
                else:
                    print("Enter the available service number")
            except:
                print("Enter valid input type")
        elif value == 5:
            if len(recipes)>0:
                statis_category()
                statis_time()
                top_ing_count()
                statis_ingredient()
            else:
                print("There is no recipes available to analyse")
        else:
            print("enter service number between 1-5")
    except:
        print("==SYSTEM ERROR==")
