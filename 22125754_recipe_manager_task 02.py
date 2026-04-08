#Note: The code has been divided according to task numbers for clarity and ease of evaluation.
#These sections are intended for demonstration purposes and may not run as a complete standalone program.

recipes = {} #main recipes dictionary
rec_count = 1  #recipe count
units = ['g', 'kg', 'ml', 'l', 'cup', 'tbsp', 'tsp', 'piece'] #permissable ingredient units

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
                
