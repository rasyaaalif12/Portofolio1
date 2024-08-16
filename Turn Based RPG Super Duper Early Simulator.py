# Turn Based RPG Super Duper Early Simulator 
# THE FIRST
# With a lot of for loop
# Also if else
# Also a lot of function
# No Class to make it harder
# Press Run to Play
#===============================================================================
# Import Library
import random
from tabulate import tabulate

#===============================================================================
## GACHA FUNCTION
rand_list=[]
def ini_function():
    for i in range(0,3):
        i=random.randint(0,9)
        rand_list.append(i)
    print(rand_list)
    global ini_out
    if rand_list[0]==7 and rand_list[1]==7 and rand_list[2]==7 :
        print('****LUCKY 7 ROLL****')
        ini_out=1
    elif sum(rand_list)==0:
        print('****MISS****')
        ini_out=2
    elif sum(rand_list)<=5:
        print('****BAD LUCK****')
        ini_out=3
    elif sum(rand_list)>5 and sum(rand_list)<=15:
        print('****MILD LUCK****')
        ini_out=4
    elif sum(rand_list)>15 and sum(rand_list)<=21:
        print('****GOOD LUCK****')
        ini_out=5
    elif sum(rand_list)>21 and sum(rand_list)<=27:
        print('****SUPER LUCK****')
        ini_out=6
    else:
        print('****')
    rand_list.clear()

def ini_enemy_function():
    for i in range(0,3):
        i=random.randint(0,9)
        rand_list.append(i)
    print(rand_list)
    global ini_enemy_out
    if rand_list[0]==7 and rand_list[1]==7 and rand_list[2]==7 :
        print('****UNLUCKY 7 ROLL****')
        ini_enemy_out=1
    elif sum(rand_list)==0:
        print('****MISS****')
        ini_enemy_out=2
    elif sum(rand_list)<=5:
        print('****BAD LUCK****')
        ini_enemy_out=3
    elif sum(rand_list)>5 and sum(rand_list)<=15:
        print('****MILD LUCK****')
        ini_enemy_out=4
    elif sum(rand_list)>15 and sum(rand_list)<=21:
        print('****GOOD LUCK****')
        ini_enemy_out=5
    elif sum(rand_list)>21 and sum(rand_list)<=27:
        print('****SUPER LUCK****')
        ini_enemy_out=6
    else:
        print('****')
    rand_list.clear()

#===============================================================================
## RANDOM NUMBER FUNCTION
def rand_function():
    rand_value=random.randint(1,10)
    return rand_value

#===============================================================================
## BAD ENDING
## BAD ENDING 1
def bad_ending1():
    print(f'''
    {hero_name} has given up, 
    {hero_name} has to cower in fear inside their room,
    Continuing their mundane life become a shut-in,
    Never trying to take another challenge that could change their life.
    ''')
    input('Press anything to continue: ')
    quit()

## BAD ENDING 2
def bad_ending2():
    print(f'''
    {hero_name} has died,
    {hero_name} has fought gallantly against the odds,
    As {enemy_name} lay waste to The Land Between,
    The World has turned into CHAOS. 
    ''')
    input('Press anything to continue: ')
    quit()

#===============================================================================
## GOOD ENDING
def good_ending1():
    print(f'''
    {hero_name} has won,
    {hero_name} has fought gallantly against the odds,
    {hero_name} will be remembered as a Brave Hero,
    As the one who defeats The Almighty {enemy_name}.
          ''')
    input('Press anything to continue: ')
    quit()

#===============================================================================
## ENEMY STATUS
def kadal_gurun_status():
    global enemy_stat
    enemy_stat={'HP': 20000,
                'ATT': 100,
                'DEF': 250,
                'MATT': 50,
                'MDEF': 200,
                }

#===============================================================================
## HERO STATUS
def hero_status():
    global hero_stat,hero_inv
    hero_stat={'HP': 6000,
               'MP': 200,
                'ATT': 200,
                'DEF': 250,
                'MATT': 150,
                'MDEF': 200,
                }
    hero_inv=[
        {   'Item Name':'Small Potion',
            'Total': 5,
            'Description': f"Heal {hero_name}'s wounds for SMALL-HEAL effect"
        },

        {
            'Item Name':'Mega Potion',
            'Total': 3,
            'Description': f"Heal {hero_name}'s wounds for HIGH-HEAL effect"
        },
        
        {
            'Item Name':'Small Ether',
            'Total': 2,
            'Description': f"Restore {hero_name}'s wounds for SMALL-RESTORE effect"
        },
        
        {
            'Item Name':'Mega Ether',
            'Total': 1,
            'Description': f"Restore {hero_name}'s wounds for HIGH-RESTORE effect"
        }
            ]

#===============================================================================
## TURN COUNT
def turn_count():
    global turn_val
    while True:
        turn_val+=1
        if turn_val>0:
            break
    return
    
#===============================================================================
## COPY STAT
def copy_stat():
    global enemy_stat1,hero_stat1,hero_inv1
    enemy_stat1=enemy_stat.copy()
    hero_stat1=hero_stat.copy()
    hero_inv1=hero_inv.copy()
    return enemy_stat1['HP'],hero_stat1['HP'],hero_inv1

#===============================================================================
## KADAL GURUN ATTACK PATTERN
def attack_kadal_gurun():
    global temp_dmg
    temp_dmg+=int(((enemy_stat1['ATT']*8)-(hero_stat1['DEF']*0.5))+rand_function())
    if temp_dmg<0:
        temp_dmg=0
    input(f'{enemy_name} USES ATTACK!(Press anything to continue): ')
    input(f'{hero_name} RECEIVE {temp_dmg} DAMAGE! (Press anything to continue): ')
    return temp_dmg

def mega_attack_kadal_gurun():
    global temp_dmg
    temp_dmg+=int(((enemy_stat1['ATT']*10)-(hero_stat1['DEF']*0.5))+rand_function())
    if temp_dmg<0:
        temp_dmg=0
    input(f'{enemy_name} USES MEGA ATTACK!(Press anything to continue): ')
    input(f'{hero_name} RECEIVE {temp_dmg} DAMAGE! (Press anything to continue): ')
    return temp_dmg
    
def fire_kadal_gurun():
    global temp_dmg
    temp_dmg+=int(((enemy_stat1['MATT']*12)-(hero_stat1['MDEF']*0.5))+rand_function())
    if temp_dmg<0:
        temp_dmg=0
    input(f'{enemy_name} USES FIRE!(Press anything to continue): ')
    input(f'{hero_name} RECEIVE {temp_dmg} DAMAGE! (Press anything to continue): ')
    return temp_dmg

def mega_fire_kadal_gurun():
    global temp_dmg
    temp_dmg+=int(((enemy_stat1['MATT']*20)-(hero_stat1['MDEF']*0.5))+rand_function())
    if temp_dmg<0:
        temp_dmg=0
    input(f'{enemy_name} USES MEGA FIRE!(Press anything to continue): ')
    input(f'{hero_name} RECEIVE {temp_dmg} DAMAGE! (Press anything to continue): ')
    return temp_dmg

def scorch_kadal_gurun():
    global temp_dmg
    temp_dmg+=3000
    input(f'{enemy_name} USES SCORCHED EARTH!(Press anything to continue): ')
    input(f'{hero_name} RECEIVES {temp_dmg} DAMAGE!(Press anything to continue): ')
    return temp_dmg

#===============================================================================
## KADAL GURUN ATTACK PATTERN
def kadal_gurun_setup():
    global temp_dmg
    temp_dmg=0
## ACTION AFTER 15000 HP
    if enemy_stat1['HP']>15000:
        if ini_enemy_out==1:
            i=random.randint(0,100)
            if i>=0 and i<=100:
                temp_dmg+=999999
                input(f'{enemy_name} USES SCORCHED EARTH!(Press anything to continue): ')
                input(f'{hero_name} RECEIVES {temp_dmg} DAMAGE!(Press anything to continue): ')
                return temp_dmg
        if ini_enemy_out==2:
            i=random.randint(0,100)
            if i>=0 and i<=100:
                attack_kadal_gurun()
        elif ini_enemy_out==3:
            i=random.randint(0,100)
            if i>=0 and i<=60:
                attack_kadal_gurun()
            elif i>=61 and i<=90:
                fire_kadal_gurun()
            elif i>=91 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==4:
            i=random.randint(0,100)
            if i>=0 and i<=50:
                attack_kadal_gurun()
            elif i>=51 and i<=80:
                fire_kadal_gurun()
            elif i>=81 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==5:
            i=random.randint(0,100)
            if i>=0 and i<=40:
                attack_kadal_gurun()
            elif i>=41 and i<=70:
                fire_kadal_gurun()
            elif i>=71 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==6:
            i=random.randint(0,100)
            if i>=0 and i<=30:
                attack_kadal_gurun()
            elif i>=31 and i<=50:
                fire_kadal_gurun()
            elif i>=51 and i<=70:
                mega_fire_kadal_gurun()
            elif i>=71 and i<=100:
                mega_fire_kadal_gurun()


## ACTION AFTER 10000 HP
    elif enemy_stat1['HP']>10000:
        if ini_enemy_out==1:
            i=random.randint(0,100)
            if i>=0 and i<=100:
                temp_dmg+=999999
                input(f'{enemy_name} USES SCORCHED EARTH!(Press anything to continue): ')
                input(f'{hero_name} RECEIVES {temp_dmg} DAMAGE!(Press anything to continue): ')
                return temp_dmg
        if ini_enemy_out==2:
            i=random.randint(0,100)
            if i>=0 and i<=90:
                attack_kadal_gurun()
            elif i>90:
                mega_attack_kadal_gurun()
        elif ini_enemy_out==3:
            i=random.randint(0,100)
            if i>=0 and i<=50:
                attack_kadal_gurun()
            elif i>=51 and i<=90:
                fire_kadal_gurun()
            elif i>=91 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==4:
            i=random.randint(0,100)
            if i>=0 and i<=40:
                attack_kadal_gurun()
            elif i>=41 and i<=80:
                fire_kadal_gurun()
            elif i>=81 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==5:
            i=random.randint(0,100)
            if i>=0 and i<=30:
                attack_kadal_gurun()
            elif i>=31 and i<=70:
                fire_kadal_gurun()
            elif i>=71 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==6:
            i=random.randint(0,100)
            if i>=0 and i<=50:
                mega_attack_kadal_gurun()
            elif i>=51 and i<=100:
                mega_fire_kadal_gurun()

## ACTION LESS 10000 HP
    elif enemy_stat1['HP']<=10000:
        if ini_enemy_out==1:
            i=random.randint(0,100)
            if i>=0 and i<=100:
                temp_dmg+=999999
                input(f'{enemy_name} USES SCORCHED EARTH!(Press anything to continue): ')
                input(f'{hero_name} RECEIVES {temp_dmg} DAMAGE!(Press anything to continue): ')
                return temp_dmg
        if ini_enemy_out==2:
            i=random.randint(0,100)
            if i>=0 and i<=100:
                mega_attack_kadal_gurun()
        elif ini_enemy_out==3:
            i=random.randint(0,100)
            if i>=0 and i<=50:
                mega_attack_kadal_gurun()
            elif i>=51 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==4:
            i=random.randint(0,100)
            if i>=0 and i<=80:
                mega_attack_kadal_gurun()
            elif i>=81 and i<=100:
                mega_fire_kadal_gurun()
        elif ini_enemy_out==5:
            i=random.randint(0,100)
            if i>=0 and i<=70:
                mega_fire_kadal_gurun()
            elif i>=71 and i<=100:
                scorch_kadal_gurun()
        elif ini_enemy_out==6:
            scorch_kadal_gurun()

#===============================================================================
## HERO ATTACK PATTERN
def n_attack():
    temp_dmg=0
    if ini_out==1:
        temp_dmg+=999999
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! (Press anything to continue): ')
        return temp_dmg

    elif ini_out==2:
        temp_dmg+=int(((hero_stat1['ATT']*2)-(enemy_stat1['DEF']*1.5))+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! (Press anything to continue): ')
        return temp_dmg    

    elif ini_out==3:
        temp_dmg+=int(((hero_stat1['ATT']*4)-(enemy_stat1['DEF']*1.5))+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! (Press anything to continue): ')
        return temp_dmg    
                

    elif ini_out==4:
        temp_dmg+=int(((hero_stat1['ATT']*6)-(enemy_stat1['DEF']*1.5))+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! (Press anything to continue): ')
        return temp_dmg    

    elif ini_out==5:
        temp_dmg+=int(((hero_stat1['ATT']*8)-(enemy_stat1['DEF']*1.5))+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! (Press anything to continue): ')
        return temp_dmg    

    elif ini_out==6:
        temp_dmg+=int(((hero_stat1['ATT']*10)-(enemy_stat1['DEF']*1.5))+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! (Press anything to continue): ')
        return temp_dmg    

## X CHANCE FUNCTION
def x_chance():
    global courage_val
    temp_dmg=0
    i_list=[]
    for i in range(0,3):
        i=random.randint(0,3)
        i_list.append(i)
    print(i_list)
    if sum(i_list)==0:
        temp_dmg=0
        input('YOU SCREWED UP AND MISSED THE TIMING! ATTACK MISSES!')
        return temp_dmg
    
    elif sum(i_list)>0 and sum(i_list)<=3:
        temp_dmg+=int(((((hero_stat1['MATT']*9)-(enemy_stat1['MDEF']*1.5))*2))*courage_val+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        print(f'{hero_name} USING X SLASH!')
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! {enemy_name} RECEIVING A MILD DAMAGE! (Press anything to continue): ')
        courage_val=1
        return temp_dmg
        
    elif sum(i_list)>3 and sum(i_list)<=6:
        temp_dmg+=int(((((hero_stat1['MATT']*9)-(enemy_stat1['MDEF']*1.5))*3))*courage_val+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        print(f'{hero_name} USING X SLASH!')
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! {enemy_name} RECEIVING A HIGH DAMAGE! (Press anything to continue): ')
        courage_val=1
        return temp_dmg
            
    elif sum(i_list)>6 and sum(i_list)<=9:
        temp_dmg+=int(((((hero_stat1['MATT']*9)-(enemy_stat1['MDEF']*1.5))*4))*courage_val+rand_function())
        if temp_dmg<=0:
            temp_dmg=0
        print(f'{hero_name} USING X SLASH!')
        input(f'{hero_name} DEALING {temp_dmg} DAMAGE! {enemy_name} RECEIVING A CRITICAL HIT! (Press anything to continue): ')
        courage_val=1
        return temp_dmg
            
    else:
        print('****')

## COURAGE FUNCTION
def courage_function():
    courage=random.randint(2,4)
    input(f"{hero_name}'s MAGIC-ATTACK HAS BEEN INCREASED BY {courage} TIMES! {hero_name} IS FILLED WITH COURAGE! (Press anything to continue): ")
    return courage

#===============================================================================
## HEALING AND RECOVERY FUNCTION
def small_heal():
    global cure_val
    cure_val=int(hero_stat['HP']*0.025)
    if cure_val>(hero_stat['HP']-hero_stat1['HP']):
        cure_val=hero_stat['HP']-hero_stat1['HP']
        hero_stat1['HP']+=cure_val
    else:
        hero_stat1['HP']+=cure_val
        return

def medium_heal():
    global cure_val
    cure_val=int(hero_stat['HP']*0.2)
    if cure_val>(hero_stat['HP']-hero_stat1['HP']):
        cure_val=hero_stat['HP']-hero_stat1['HP']
        hero_stat1['HP']+=cure_val
    else:
        hero_stat1['HP']+=cure_val
        return

def high_heal():
    global cure_val
    cure_val=int(hero_stat['HP']*0.5)
    if cure_val>(hero_stat['HP']-hero_stat1['HP']):
        cure_val=hero_stat['HP']-hero_stat1['HP']
        hero_stat1['HP']+=cure_val
        return
    else:
        hero_stat1['HP']+=cure_val
        return

def small_res():
    global res_val
    res_val=int(hero_stat['MP']*0.025)
    if res_val>(hero_stat['MP']-hero_stat1['MP']):
        res_val=hero_stat['MP']-hero_stat1['MP']
        hero_stat1['MP']+=res_val
        return
    else:
        hero_stat1['MP']+=res_val
        return

def med_res():
    global res_val
    res_val=int(hero_stat['MP']*0.2)
    if res_val>(hero_stat['MP']-hero_stat1['MP']):
        res_val=hero_stat['MP']-hero_stat1['MP']
        hero_stat1['MP']+=res_val
        return
    else:
        hero_stat1['MP']+=res_val
        return

def high_res():
    global res_val
    res_val=int(hero_stat['MP']*0.5)
    if res_val>(hero_stat['MP']-hero_stat1['MP']):
        res_val=hero_stat['MP']-hero_stat1['MP']
        hero_stat1['MP']+=res_val
        return
    else:
        hero_stat1['MP']+=res_val
        return

#===============================================================================
## LIST OF ITEM (Could be added more)
def item_choice():
    while True:
        opt4_1=input('Which item do you want to use? (type the item name): ').title()
        global update
        if opt4_1=='Small Potion':
            small_heal()
            print(f"{hero_name} USES SMALL POTION! {hero_name}'s HP HAS BEEN HEALED BY {int(hero_stat1['HP']*0.025)} HP!")
            print(f'{hero_name}: {hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP')
            for update in hero_inv1:
                if update['Item Name']==opt4_1:
                    inv_loop()
            break
            
        elif opt4_1=='Med Potion':
            high_heal()
            print(f"{hero_name} USES MEDIUM POTION! {hero_name}'s HP HAS BEEN HEALED BY {int(hero_stat1['HP']*0.2)} HP!")
            print(f'{hero_name}: {hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP')
            for update in hero_inv1:
                if update['Item Name']==opt4_1:
                    inv_loop()
            break

        elif opt4_1=='Mega Potion':
            high_heal()
            print(f"{hero_name} USES MEGA POTION! {hero_name}'s HP HAS BEEN HEALED BY {int(hero_stat1['HP']*0.5)} HP!")
            print(f'{hero_name}: {hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP')
            for update in hero_inv1:
                if update['Item Name']==opt4_1:
                    inv_loop()
            break

        elif opt4_1=='Small Ether':
            small_res()
            print(f"{hero_name} USES SMALL ETHER! {hero_name}'s MP HAS BEEN RESTORED BY {int(hero_stat1['MP']*0.025)} MP!")
            print(f'{hero_name}: {hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP')
            inv_loop()
            for update in hero_inv1:
                if update['Item Name']==opt4_1:
                    inv_loop()
            break

        elif opt4_1=='Med Ether':
            high_res()
            print(f"{hero_name} USES MEDIUM ETHER! {hero_name}'s MP HAS BEEN RESTORED BY {int(hero_stat1['MP']*0.5)} MP!")
            print(f'{hero_name}: {hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP')
            inv_loop()
            for update in hero_inv1:
                if update['Item Name']==opt4_1:
                    inv_loop()
            break

        elif opt4_1=='Mega Ether':
            high_res()
            print(f"{hero_name} USES MEGA ETHER! {hero_name}'s MP HAS BEEN RESTORED BY {int(hero_stat1['MP']*0.5)} MP!")
            print(f'{hero_name}: {hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP')
            inv_loop()
            for update in hero_inv1:
                if update['Item Name']==opt4_1:
                    inv_loop()
            break

        else:
            item_choice()
        break
    return

#===============================================================================
## INVENTORY LOOP FUNCTION
def inv_loop():
    for x in hero_inv: 
        if x in hero_inv1:
            update['Total']-=1
            return
        else:
            update['Total']==1
            return

#===============================================================================
## SCREEN AND BARRIER CHECK FUNCTION
## SCREEN
def screen_check():
    global screen_val
    for i in range(screen_val):
        i+=1
        screen_val-=i
        if screen_val==0:
            hero_stat1['DEF']-=screen_stat
        elif screen_val>0:
            return
    return

## BARRIER
def barrier_check():
    global barrier_val
    for i in range(barrier_val):
        i+=1
        barrier_val-=i
        if barrier_val==0:
            hero_stat1['MDEF']-=barrier_stat
        elif barrier_val>0:
            return
    return  

#===============================================================================
## BATTLE HERO TURN
def battle_hero_turn():
    global turn_val,hero_inv1,screen_val,barrier_val
    hero_stat1
    enemy_stat1
# Checkpoint 1
    turn_count()
# Screen/Barrier Check
    screen_check()
    barrier_check()
# Checkpoint 2       
    rand_function()
    if enemy_stat1['HP']<=0:
        good_ending1()
    elif enemy_stat1['HP']>0:
        while True:
            print(f'''
-------------------------------------------------------------
                YOU'VE ENCOUNTERED {enemy_name}
                    {enemy_stat1['HP']} HP REMAINING
        
    


{hero_name}:{hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP,       Turn Count:{turn_val}
=============================================================
1. ATTACK           3.TRACE             5. TUTORIAL
2. SPELL            4.INVENTORY         6. GIVE UP
-------------------------------------------------------------
                ''')

            option=input(f'What will {hero_name} do? (1/2/3/4/5/6): ')
#===========================================================================================
### 1. ATTACK
            if option=='1':
                input(f"{hero_name} IS LAUNCHING AN ATTACK! (Press anything to continue): ")
                ini_function()
                enemy_stat1['HP']-= n_attack()
                return
            
#===========================================================================================
### 2. SPELL
            elif option=='2':
                print(f'''
=================================================================================================================================================
1. X-SLASH      Cost: 30 MP        Effect: Unleash a barrage of MAGIC slashes, {hero_name}'s trusty technique
2. COURAGE      Cost: 10 MP        Effect: Buff your MAGIC-ATTACK to SMALL effect. Removed after using MAGIC-ATTACK
3. CURE         Cost: 15 MP        Effect: Heal {hero_name}'s wounds for MEDIUM-HEAL effect
4. SCREEN       Cost: 10 MP        Effect: Create a SCREEN to dull physical damage for 3 turns 
5. BARRIER      Cost: 15 MP        Effect: Conjure a BARRIER to dull magic damage for 2 turns
6. Back
-------------------------------------------------------------------------------------------------------------------------------------------------
        ''')
                while True:   
                    spell_opt=input(f'Which SPELL are you gonna use? (1/2/3/4/5/6): ')
                    if spell_opt=='1':
                        if hero_stat1['MP']<30:
                            print(f'{hero_name} TRIES TO DO X-SLASH, BUT {hero_name} HAS NOT ENOUGH MP!')
                            
                        else:
                            print(f'{hero_name} USES X-SLASH!')
                            input('X SLASH CHANCE MODE (Press anything to roll): ')
                            enemy_stat1['HP']-=x_chance()
                            hero_stat1['MP']-=30

                    elif spell_opt=='2':
                        global courage_val
                        if hero_stat1['MP']<10:
                            print(f'{hero_name} TRIES TO MUSTER THE COURAGE, BUT {hero_name} HAS NOT ENOUGH MP!')
                        else:
                            if courage_val>1:
                                input('COURAGE IS STILL ACTIVE!')
                            else:
                                print(f"{hero_name} USES COURAGE! {hero_name}'s MAGIC DAMAGE HAS BEEN INCREASED!")
                                input('COURAGE CHANCE MODE (Press anything to roll): ')
                                courage_val=courage_function()
                                hero_stat1['MP']-=10

                    elif spell_opt=='3':
                        if hero_stat1['MP']<10:
                            print(f'{hero_name} TRIES TO USE CURE, BUT {hero_name} HAS NOT ENOUGH MP!')
                        else:    
                            if hero_stat1['HP']==hero_stat['HP']:
                                input(f"{hero_name}'s HP IS ALREADY FULL!")
                                rand_function()
                            else:
                                print(f"{hero_name} USES CURE! {hero_name}'s HP HAS BEEN HEALED!")
                                medium_heal()
                                hero_stat1['MP']-=10

                    elif spell_opt=='4':
                        if hero_stat1['MP']<10:
                            print(f'{hero_name} TRIES TO CREATE SCREEN, BUT {hero_name} HAS NOT ENOUGH MP!')    
                        elif screen_val>0:
                            input('SCREEN IS STILL ACTIVE!')
                        else:
                            input(f'{hero_name} USES SCREEN! PHYSICAL DAMAGE TO {hero_name} HAS BEEN DULLED! (Press anything to continue): ')
                            global screen_stat
                            screen_stat=int(hero_stat1['DEF']+(hero_stat1['DEF']*0.5))
                            screen_val=4
                            hero_stat1['DEF']+=screen_stat
                            hero_stat1['MP']-=10

                    elif spell_opt=='5':
                        if hero_stat1['MP']<15:
                            print(f'{hero_name} TRIES TO CONJURE BARRIER, BUT {hero_name} HAS NOT ENOUGH MP!')    
                        elif barrier_val>0:
                            input('SCREEN IS STILL ACTIVE!')
                        else:
                            input(f'{hero_name} USES BARRIER! MAGIC DAMAGE TO {hero_name} HAS BEEN DULLED! (Press anything to continue):')
                            global barrier_stat
                            barrier_stat=int(hero_stat1['MDEF']+(hero_stat1['MDEF']*0.5))
                            barrier_val=3
                            hero_stat1['MDEF']+=barrier_stat
                            hero_stat1['MP']-=15

                    elif spell_opt=='6':
                        rand_function()
                    else:
                        rand_function()
                    return
                    

#===========================================================================================
### 3. TRACE
            elif option=='3':
                print(f'1. {hero_name}       2. {enemy_name}')
                while True:
                    opt3=input(f'Which one are {hero_name} going to TRACE?(1/2): ')
                    if opt3=='1':
                        while True:
                            opt3_1=input(f"You are going to TRACE {hero_name}, are you sure?(Y/N): ").upper()
                            if opt3_1=='Y':
                                print(hero_stat1)
                                input(f'{hero_name} HAS BEEN TRACE-ed! (Press anything to continue): ')
                                break
                            elif opt3_1=='N':
                                break
                            else:
                                print('****')
        
                    elif opt3=='2':
                        while True:
                            opt3_2=input(f"You are going to TRACE {enemy_name}, are you sure?(Y/N): ").upper()
                            if opt3_2=='Y':
                                print(enemy_stat1)
                                input(f'{enemy_name} HAS BEEN TRACE-ed! (Press anything to continue): ')
                                break
                            elif opt3_2=='N':
                                break
                            else:
                                print('****')
                    break
                rand_function()


            
#===========================================================================================
### 4. INVENTORY
            elif option=='4':
                while True:
                    opt_4=input(f'{hero_name} is going to use item, do you want to continue?(Y/N): ').upper()
                    if opt_4=='Y':
                        print(tabulate(hero_inv1, headers='keys', tablefmt='psql' ))
                        print(f'{hero_name}: {hero_stat1['HP']}/{hero_stat['HP']} HP, {hero_stat1['MP']}/{hero_stat['MP']} MP')
                        while True:
                            item_choice()
                            break
                        hero_inv1=[i for i in hero_inv1 if i.get('Total')!=0]
                        input('Press anything to continue: ')
                        return
                    elif opt_4=='N':
                        break
                    else:
                        print('****')
                rand_function()


#===========================================================================================
### 5. TUTORIAL
            elif option=='5':
                print('''
There are 6 options to fight the ENEMY
1. ATTACK     --> ATTACK the ENEMY and dealing physical damage to the ENEMY
2. SPELL      --> as the HERO: 
                  Use OFFENSIVE SPELL to deal magical damage to the ENEMY, or
                  Use DEFENSIVE SPELL to guard the HERO against ENEMY's physical and magical damage
3. TRACE      --> Use TRACE to check HERO or ENEMY status: HP, MP, ATTACK, DEFENSE, MAGIC-ATTACK, MAGIC-DEFENSE
                  it wont cost HERO's turn
4. INVENTORY  --> Items could be accessed with INVENTORY
                  use anything necessary to reach your goal
5. TUTORIAL   --> TUTORIAL could help HERO's journey to remind the config
                  Confused HERO needs to clear their mind and retrace
6. GIVE UP    --> Use this option to starts the END of HERO's journeys early
''')
                input('Press anything to continue: ')
                rand_function()

#===========================================================================================
### 6. GIVE UP
            elif option=='6':
                while True:
                    give_opt=input('DO YOU WANT TO GIVE UP? ARE YOU SURE? (Y/N): ').upper()
                    if give_opt=='Y':
                        bad_ending1()
                    elif give_opt=='N':    
                        break
                rand_function()
            else:
                rand_function()

#===============================================================================
## BATTLE ENEMY TURN
def battle_enemy_turn():
    global turn_val,hero_inv1,temp_dmg
    hero_stat1
    hero_inv1
    enemy_stat1
# Checkpoint 1
    rand_function()
    input(f"{enemy_name}'s TURN (Press anything to continue): ")
    ini_enemy_function()
    return

#===============================================================================
## BATTLE NUMBER 1
def battle_1():
    global enemy_name,courage_val,turn_val,screen_val,barrier_val
    enemy_name='kadalgurun'
    courage_val=1
    turn_val=0
    screen_val=0
    barrier_val=0
    kadal_gurun_status()
    hero_status()
    copy_stat()
    while True:
        if hero_stat1['HP']<=0:
            input('BATTLE LOST!')
            bad_ending1()
        elif enemy_stat1['HP']<=0:
            input('BATTLE WON!')
            good_ending1()
        else:
            battle_hero_turn()
            if hero_stat1['HP']<=0:
                input('BATTLE LOST!')
                bad_ending2()
            elif enemy_stat1['HP']<=0:
                input('BATTLE WON!')
                good_ending1()
            else:    
                battle_enemy_turn()
                kadal_gurun_setup()
                hero_stat1['HP']-=temp_dmg

#===============================================================================
## PROGRAM START
hero_name='kadalsawah'
battle_1()