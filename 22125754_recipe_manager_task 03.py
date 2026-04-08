#Note: The code has been divided according to task numbers for clarity and ease of evaluation.
#These sections are intended for demonstration purposes and may not run as a complete standalone program.


recipes = {} #main recipes dictionary
rec_count = 1  #recipe count
units = ['g', 'kg', 'ml', 'l', 'cup', 'tbsp', 'tsp', 'piece'] #permissable ingredient 
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

