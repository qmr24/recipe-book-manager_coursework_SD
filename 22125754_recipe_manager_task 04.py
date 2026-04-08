#Note: The code has been divided according to task numbers for clarity and ease of evaluation.
#These sections are intended for demonstration purposes and may not run as a complete standalone program.


recipes = {} #main recipes dictionary
rec_count = 1  #recipe count
units = ['g', 'kg', 'ml', 'l', 'cup', 'tbsp', 'tsp', 'piece'] #permissable ingredient units

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
        top_n = len(l)
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
    

